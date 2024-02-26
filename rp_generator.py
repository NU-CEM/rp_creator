import argparse
from ase import Atoms
from ase import Atom
import numpy as np
# makes from I4/mmm tetragonal structure.
# make sure you relax with varying cell size
# make sure you relax with random displacement

def get_chemical_formula(A,B,X,n_list):
    
    x = str(np.sum(n_list+1))
    y = str(np.sum(n_list))
    z = str(np.sum(3*(n_list)+1))

	return A+x+B+y+X+z

def perovskite_unit(A,B,X):
	return Atoms([A,B,X], positions=[(0,0,0),(0.5,0.5,0.5),(0.5,0.5,0),(0.5,0,0.5),(0,0.5,0.5)])


def rocksalt_unit(A,X):
	return Atoms([A,X], positions=[(),()])

def create_rp_structure(A,B,X,n_list):
	for number_of_layers in n_list:
		for layer_count in range(number_of_layers):
			# create perovskite layer here

		# create RockSalt layer here

	return Atoms

def rattle_structure(Atoms):

def save_structure(Atoms):




if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Script to generate (mixed) Ruddlesden Popper structure')
	parser.add_argument('n', help='the number of perovskite layers between each rocksalt layer. Multiple n values will create a mixed Ruddlesden Popper structure with various n-values as specified.',type=int, nargs="+" )
	parser.add_argument('--a_length', help="specify the in-plane primitive lattice vector a",type=float, default=)
	parser.add_argument('--b_length', help="specify the in-plane primitive lattice vector b",type=float,default=)
	parser.add_argument('--perovskite_spacing', help="specify the distance between perovskite-perovksite layers",type=float)
	parser.add_argument('--rocksalt_spacing', help="specify the distance between rocksalt layers",type=float)
	parser.add_argument('--A', help="element on A-site",type='str',default='Ba')
	parser.add_argument('--B', help="element on B-site",type='str',default='Zr')
    parser.add_argument('--X', help="element on X-site",type='str',default='S')
    parser.add_argument('--random', help="apply random displacement to all atoms", type=bool, default=False)

    args = parser.parse_args()


    if rattle:
    	RP_atoms = rattle_structure()

    save_structure(RP_atoms)

