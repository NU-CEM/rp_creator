"""Converts a FHI-aim geometry.in file with primitive cell to a .cif file with conventional cell"""
import sys
import spglib
import ase
import ase.io

filename_out = sys.argv[1]

atoms = ase.io.read("geometry.in")
spg_cell = (atoms.cell, atoms.get_scaled_positions(), atoms.numbers)
new_unit_cell, new_scaled_positions, new_numbers = spglib.standardize_cell(spg_cell, to_primitive=False, symprec=5e-3)
conventional_atoms = ase.Atoms(new_numbers, cell=new_unit_cell, scaled_positions=new_scaled_positions)

ase.io.write(filename_out,conventional_atoms)

