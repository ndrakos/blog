---
layout: post
title:  "Neutrino Transfer Function"
date:   2022-07-25
categories: neutrinos
---


To assign neutrino positions, neutrinos are placed on a coarse grid, then displaced using LPT. This requires a transfer function.


## CAMB

I will use the Code for Anisotropies in the Microwave Background (CAMB). MUSIC has a plugin to read CAMB outputs. The different transfer variables are listed <a href="https://camb.readthedocs.io/en/latest/transfer_variables.html">here</a>.


## Python Version

There is now a python wrapper for CAMB. I pip installed CAMB to play around with (see the example notebook <a href="https://camb.readthedocs.io/en/latest/CAMBdemo.html">here</a>).


Here is some code for generating transfer functions in python:

```
import camb

pars = camb.CAMBparams()
pars.set_cosmology(H0=70, ombh2=0.022, omch2=0.122)
pars.InitPower.set_params(ns=1)
pars.set_matter_power(redshifts=[zstart], kmax=kmax)

results= camb.get_results(pars)
trans = results.get_matter_transfer_data()
kh = trans.transfer_data[0,:,0] #get kh - the values of k/h at which they are calculated

delta_cdm = trans.transfer_data[model.Transfer_cdm-1,:,0] #Deltac/k^2
delta_b = trans.transfer_data[model.Transfer_b-1,:,0]
delta_nu = trans.transfer_data[model.Transfer_nu-1,:,0]
delta_tot = trans.transfer_data[model.Transfer_tot-1,:,0]
```



## Fortran version

To actually run this in MUSIC, I'll just use the fortran version, since it automatically creates the correct output files needed for MUSIC.

To install and compile:

```
git clone https://github.com/cmbant/CAMB.git --recurse-submodules
cd CAMB/fortran
make
```


To run the code:
```
./camb ../inifiles/params.ini
```

The params.ini file is pretty straightforward to modify. I can set the cosmological parameters in here.



## Modification to MUSIC Code

As mentioned above, MUSIC already as a CAMB plugin. <code>transfer_camb.cc</code> contains machinery for reading in the transfer functions from camb output. I just needed to change it so that it stores the neutrino transfer function, rather than discard it as a dummy variable. This just meant reading through the code, and adding neutrinos in the same way cdm particles were treated throughout.

I also needed to add neutrinos to the tf_type types in <code>transfer_function.hh</code>.

This compiled fine.


## Next steps


Make sure initial positions all make sense
1. Fix the Gadget output so that it has <code>write_neutrino_position</code> properly written
2. Check I am getting the correct number of dark matter particles and neutrinos
3. Plot the power spectrum of the MUSIC ICs, and make sure this matches the input

Make sure initial velocities make sense
4. Look into the bulk velocity assignment for neutrinos
5. Assign velocities to neutrinos in MUSIC
6. Check the initial velocity distribution

Try in Gadget
7. Make sure the code runs in Gadget
8. Check the evolution of the power spectrum, and that it makes sense


## Possible Complications

- Each neutrino has a bulk velocity determined by the power spectrum, plus an extra thermal velocity from the Fermi-Dirac distribution. CAMB doesn't seem to output the velocity transfer functions for neutrinos. Since the initial velocity should be the *bulk* velocity, plus the extra thermal velocity, I need to figure out how to implement this.
- From Elbers et al 2021: CAMB and Class... "but the neutrino related transfer functions (e.g. density and velocity) are not converged and can be very inaccurate (Dakin et al. 2019)."
