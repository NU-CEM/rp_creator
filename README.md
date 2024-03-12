# RP generator

Script to generate (disordered) Ruddlesden-Popper structure with any n-value. 
Multiple n-values will create a "disordered" Ruddlesden Popper structure.

⭐ Creates material in a high-symmetry tetragonal structure.  
⭐ After creating you must relax the atom positions **and** lattice parameters to find equilibrium structure.  
⭐ You may also want to use the `rattle` option to allow for distortions to lower symmetry.  
⭐ Can be saved any structure format supported by [ASE](https://wiki.fysik.dtu.dk/ase/).  
⭐ Can be created as conventional or primitive cell.  
⭐ Requires [Numpy](https://numpy.org/), [ASE](https://wiki.fysik.dtu.dk/ase/) and [spglib](https://spglib.readthedocs.io/en/stable/index.html): `conda install --channel conda-forge numpy ase spglib`

## Help

To see which command line options are available run `python rp_generator.py --help`. If you find unexpected behaviour please contact Lucy at l.whalley@northumbria.ac.uk. You can also [raise an issue](https://github.com/NU-CEM/rp_generator/issues), although I may take longer to respond to this.

## Examples

- `python rp_generator.py -n 5 6 -a 5` will create 5 perovskite layers + rocksalt layer + 6 perovskite layers + rocksalt layer.
- `python rp_generator.py -n 3 -a 5` will create the standard RP material A<sub>4</sub>B<sub>3</sub>X<sub>10</sub>.

In both examples the lattice parameter of a single cubic perovskite unit is set to 5 Ångström.

![Picture of structures formed in example](./example_structures.png)



