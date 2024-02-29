# RP generator

Script to generate (disordered) Ruddlesden Popper structure with any n-value. 
Multiple n-values will create a disordered Ruddlesden Popper structure.

For example:
- `rp_generator -n 5 6` will create 5 perovskite layers + rocksalt layer + 6 perovskite layers + rocksalt layer.
- `rp_generator -n 3` will create the standard RP material A<sub>4</sub>B<sub>3</sub>X<sub>10</sub>.

Creates material in a high-symmetry tetragonal structure.
After creating you will need to relax to find the equilibrium structure. 
Importantly, you must allow the atomic positions **and** cell volume to relax.
You most likely also want to use the `rattle` option to allow for distortions to lower symmetry.

Use with caution as it is still being tested.
