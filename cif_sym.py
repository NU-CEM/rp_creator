import sys
import ase.io
import ase.spacegroup

filename_in = sys.argv[1]
sym_prec = float(sys.argv[2])

atoms = ase.io.read(filename_in)
print(ase.spacegroup.get_spacegroup(atoms,symprec=sym_prec))
