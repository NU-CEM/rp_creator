#!/usr/bin/env python 

import argparse
import numpy as np
import ase
import spglib

from ase import Atoms
from ase import io
from spglib import standardize_cell


"""Script to generate (disordered) Ruddlesden Popper structure with any n-value. 
Multiple n-values will create a disordered Ruddlesden Popper structure.
For example, `rp_generator -n 5,6` will create 5 perovskite layers + rocksalt layer + 6 perovskite layers + rocksalt layer.
Whilst `rp_generator -n 3` will create the standard RP material A4B3X10.
Creates phase in a high-symmetry tetragonal structure.
After creating this structure you will need to relax to find the equilibrium structure. 
Importantly, you must allow the atomic positions and cell volume to relax.
You most likely also want to use the `rattle` option to break symmetry and allow for distortions to lower symmetry.

Use with caution as this hasn't been thoroughly tested.
"""

def perovskite_atoms(A,B,X,cell_length):
    """Returns single perovskite layer"""
    
    return Atoms([A,B,X,X,X], 
           scaled_positions=[(0.5,0.5,0.5),(0,0,0),(0.5,0,0),(0,0,0.5),(0,0.5,0)],
           cell=[cell_length,cell_length,cell_length,90,90,90])

def rocksalt_atoms(A,X,cell_length):
    """Returns rocksalt layer"""
    
    return Atoms([A,X], 
           scaled_positions=[(0,0,0),(0.5,0.5,0)],
           # note that the third parameter for cell can be set to any positive number 
           cell=[cell_length,cell_length,1,90,90,90])

def save_structure(atoms_object,n_array,A,B,X,filetype='cif'):
    """Save structure as cif"""

    ase.io.write('RP_{}_{}.{}'.format(''.join(map(str,n_array)),A+B+X,filetype), atoms_object,format=filetype)

def create_disordered_rp(n_array,A='Ba',B='Zr',X='S',cell_length=5,rattle=False,save=True,filetype='cif',primitive=True):
    """Returns (disordered) RP phase as an ASE atoms object.
    """

    # if the number of n-values is odd then we must double the array to make even.
    # This is to ensure that when pbc is applied
    # the neighbouring perovskite slabs are correctly offset from one-another
    if len(n_array) % 2 == 1:
        n_array = np.concatenate((n_array,n_array))

    # we need to create structure and apply pbc before adding in the perovskite and rocksalt layers
    total_length = np.sum(n_array)*1*cell_length + len(n_array)*0.5*cell_length 
    rp_structure = Atoms(cell=[cell_length,cell_length,total_length,90,90,90],pbc=[True,True,True])

    # create perovskite and rocksalt layer
    perovskite_layer = perovskite_atoms(A,B,X,cell_length)
    rocksalt_layer = rocksalt_atoms(A,X,cell_length)

    # for each slab of perovskite
    for number_of_layers in n_array:
        
        # for each perovskite layer within the slab
        for _ in range(number_of_layers):
            
            # add a perovskite layer to the rp_structure
            rp_structure += perovskite_layer
            # translate the perovskite and rocksalt layers along c-axis ready for next insertion
            perovskite_layer.translate(np.dot([0,0,1],perovskite_layer.cell))
            rocksalt_layer.translate(np.dot([0,0,1],perovskite_layer.cell))
        
        # after creating perovksite slab, add a rocksalt layer
        rp_structure += rocksalt_layer
        # translate the perovskite and rocksalt layers along c-axis ready for next insertion
        # also translate the rocksalt and perovskite layers in the ab-plane
        rocksalt_layer.translate(np.dot([0.5,0.5,0.5],perovskite_layer.cell))
        perovskite_layer.translate(np.dot([0.5,0.5,0.5],perovskite_layer.cell))

    if rattle:
        rp_structure.rattle(stdev=0.05, seed=1)

    if primitive:
        spg_cell = (rp_structure.cell, rp_structure.get_scaled_positions(), rp_structure.numbers)
        spg_cell_primitive = standardize_cell(spg_cell, to_primitive=True, symprec=5e-3)
        primitive_cell, primitive_positions, primitive_numbers = spg_cell_primitive
        rp_structure = Atoms(primitive_numbers, cell=primitive_cell, scaled_positions=primitive_positions)
        
    if save:
        save_structure(rp_structure,n_array,A,B,X,filetype=filetype)

    return rp_structure


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Script to generate (disordered) Ruddlesden Popper structure')
    parser.add_argument('-n', help='the number of perovskite layers between each rocksalt layer.',type=int, nargs="+" )
    parser.add_argument('-a', '--cell_length', help="the cell length of a single perovskite unit",type=float, default=5.0)
    parser.add_argument('-A', help="element on A-site",type=str,default='Ba')
    parser.add_argument('-B', help="element on B-site",type=str,default='Zr')
    parser.add_argument('-X', help="element on X-site",type=str,default='S')
    parser.add_argument('-r', '--rattle', help="apply small random displacement to all atoms", type=bool, default=False)
    parser.add_argument('-s', '--save', help="save structure as file", type=bool, default=True)
    parser.add_argument('-f', '--filetype', help="filetype to save as", type=str, default='cif')
    parser.add_argument('-p', '--primitive', help="generate primitive cell", type=bool, default=False)

    args = parser.parse_args()

    create_disordered_rp(np.array(args.n),
                         A=args.A,
                         B=args.B,
                         X=args.X,
                         cell_length=args.cell_length,
                         rattle=args.rattle,
                         save=args.save,
                         filetype=args.filetype,
                         primitive=args.primitive)


