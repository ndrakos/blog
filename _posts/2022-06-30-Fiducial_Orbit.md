---
layout: post
title:  "Fiducial Orbit"
date:   2022-06-30
categories: tidal_stripping
---

Now that I have the <a href="https://ndrakos.github.io/blog/tidal_stripping/Double_Alpha_Profile_Stability/">fiducial ICs</a> for the double-component sims set-up and stable, I'm going to decide on the initial orbit.

Our work will be closely related to the work by Ogiya2018. The main differences are that (1) we are also varying the slope of the stellar component and (2) we are focusing on how particles are removed in energy space.

Therefore, our fiducial orbit can be similar to the one used in Ogiya2018.

## Host Halo

In my version of Gadget, with the fixed potential, I need to set
1. <code>NFW_Mvir</code>: The host to satellite mass ratio
2. <code>NFW_C</code>: The concentration of the host.
3. <code>SAT_C</code>: The concentration of the satellite (assuming the scale radius of the satellite is 1). The code sets the virial radius of the host, $$R\_vir = SAT_C * NFW\_Mvir^{1/3}$$

I will use the same values in the Ogiya paper: 224, 5.8 and 11.2

In simulation units, the host has mass $$M=224$$, virial radius $$R_{\rm vir} = 68.02$$,   scale radius $$R_s = 11.72$$ and characteristic density $$\\rho_0 = 0.01038$$. 


## Orbital parameters


The initial frame of the satellite was set to be x,y,z,vx,vy,vz = (559 kpc, 0, 0, 0, 20.6 km/s, 0). This is more tightly bound, and more radial than a typical orbit (it is in the 1.2th percentile of the energy/circularity of orbital parameters in simulations), but Ogiya shows this can describe the dark matter deficient galaxy they are studying.

In the simulation units, $$G=1$$, $$r_{\rm unit}=r_s$$ and $$M_{\rm unit} = M_{\rm sat}$$. Then, the velocity unit is $$v_{\rm unit} = \sqrt{ G M_{\rm sat}/r_{s}}$$.

In Ogiya's paper, the virial radius of the satellite is 77.3 kpc, and it has a concentration of 11.2. Therefore,  $$r_{\rm unit}=6.9$$ kpc. The mass of the satellite is $$4.9 × 10^10$$ solar masses, which means the velocity unit is $$v_{\rm unit} = 165.12 $$.

In simulation units x,y,z,vx,vy,vz = (80.9, 0, 0, 0, 0.12, 0)

## Time Outputs

I want to run this for at least 5 orbits, and have 10 outputs per orbit.

First, I need to calculate the orbital time. I have some code to integrate a point mass in an NFW profile. This gave an orbital period of 112.51 (in simulation units). Therefore, I will print out snapshots every t=11.25, for 50 snapshots.
