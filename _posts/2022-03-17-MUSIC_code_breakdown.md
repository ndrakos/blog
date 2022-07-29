---
layout: post
title:  "MUSIC Code Breakdown"
date:   2022-03-17
categories: neutrinos
---

As outlined in <a href="https://ndrakos.github.io/blog/iso_ics/Neutrino_IC_Method_Overview/">this post</a>, I am planning to modify MUSIC to contain neutrinos using the method from <a href="https://ui.adsabs.harvard.edu/abs/2018JCAP...09..028B/abstract">Banjeree et al. 2018</a>.

In this post I'm going to breakdown the code structure of MUSIC and think about what I need to alter.




## Main File

The main function that needs to be altered is <code>scr/main.cc</code>.


### What cases are allowed

For now I am just going to code the *simplest* case for the neutrinos. Once I've trouble shooted, I can add more functionality if I want

* <code>baryons</code>: "if initial conditions for baryons shall be generated
  * set to no for now"
* <code>use_2LPT</code>: "if 2nd order Lagrangian perturbation theory shall be used to compute bool particle displacements and velocities"
  * Only allow 1LPT to start
* <code>use_LLA</code>: "if baryonic density field shall be computed using a second order bool expansion of the local Lagrangian approximation (LLA)"
  * No (does it matter if we don't include baryons?)
* <code> format	= gadget2</code>
  * I am only going to make this compatible with Gadget2.


### Breakdown of main function


Here are some important points of the code:

* line 305: Beginning of main()

**Initialization**

* line 422: Initialize Cosmology
  * **Will need to define a variable <code>do_neutrinos</code>**
* line 473: Determine run parameters.
  * **Check here that all the settings are compatible with neutrinos**
* line 485: Determine refinement hierarchy. Makes grid structure for Poisson solver and for density convolution.
* line 503: Initialize output plug-in
* line 511: Initialize random numbers (for gaussian field)
* line 520: Initialize Poisson Solver. Look at this in more detail!
* line 563: check if 2LPT is set. If it is go to line 874. Otherwise stay here for 1LPT


**1LPT branch**

* line 565: Enter 1LPT branch
* line 568: *Beginning of position calculations*
* line 588: Write dark matter mass
* line 589: Write dark matter density
* line 598: Write dark matter potential
* line 625: Write dark matter positions
  * **This is where I will write out neutrino mass, velocities and positions**
* line 636: Check to see if including baryons. If not go to line 705 (velocities)
* line 650: If not LLA, write baryon density
* line 680: Write baryon positions
* line 696: If LLA, write baryon density
* line 705: *Beginning of velocity calculations*
* line 707: *Option 1: not [(baryons and TF velocities) or SPH]*
* line 756: Write dark matter velocities
  * This is where I can write out neutrino velocities
* line 761: Write baryon velocities
* line 770: *Option 2: (baryons and TF velocities) or SPH*
* line 816: Write dark matter velocities
* line 864: Write baryon velocities

**2LPT branch**

* line 876: Enter 2LPT branch
* line 887: *Beginning of velocity calculations*
* line 906: If dark matter only, write dark matter density
* line 907: If dark matter only, write dark matter mass
* line 972: Write dark matter velocities
* line 974: *Case 1: (baryons and not TF velocities and not SPH)*
* line 977: Write baryon velocities
* line 985: *Case 2: (baryons and not TF velocities and not SPH)*
* line 1006: Write baryon potential
* line 1056: Write baryon velocities
* line 1064: *Beginning of position calculations*
* line 1083: If not dark matter only, write dark matter density
* line 1084: If not dark matter only, Write dark matter mass
* line 1154: Write dark matter position
* line 1161: *Option 1: baryons and not SPH*
* line 1174: If not LLA, Write baryon density
* line 1199: If LLA, Write baryon density
* line 1202: *Option 2: baryons and SPH*
* line 1215: Write baryon density
* line 1264: Write baryon position

**Finish output and cleanup**

## Output File

The functions for calculating DM positions, velocities, ect are in the output files. For our case, we want to write them for Gadget2, so the file we will need to alter is <code>output_gadget2.cc</code>.

I'll include functions for <code>write_nu_mass</code>, <code>write_nu_position</code> and <code>write_nu_velocity</code>.

Note that Gadget2 is not built to consider neutrino particles specifically. They have 6 different particle types. However, from the Gadget2 User Guide:

"The code distinguishes between different particle types. Each type may have a different gravitational softening. As far as gravity is concerned, all the types are treated equivalently by the code, the names 'Gas', 'Halo', 'Disk', 'Bulge', 'Stars', and 'Bndry', are just arbitrary tags, still reflecting GADGET-2’s origin as a tool to study colliding galaxies. However, the particles of the first type (‘Gas’) are indeed treated as SPH particles, i.e. they receive an additional hydrodynamic acceleration, and their internal entropy per unit mass is evolved as independent thermodynamic variable."

Therefore, I can decide that, e.g. Bndry can be used to mean neutrinos, and set the particles here.


## Extra Parameters

Will need to alter the parameter file as described below to take in the extra variables.

<code>[setup]</code>
* <code>neutrinos = yes/no</code>: whether or not the code should include neutrinos
* <code>level_neutrinos = int </code>: this is related to the coarse grid, used to generate neutrino particles
* <code> N_shell = int</code>
* <code> N_side = int</code>


<code>[cosmology]</code>
* <code>g_nu = int</code>: neutrino degeneracy; i.e. number of species
* <code>T_nu = float</code>: neutrino temperature today in Kelvin
* <code>mass_nu = float</code>: sum of the mass of neutrinos, in eV


Options that I am NOT considering: The non-degenerate case, other methods of discretizing the Fermi-Dirac distribution.


## Questions

Here are some questions that came up when reading the paper, and from talking to Bruno.


1. In B18 they say the "modify a version of N-GenIC that computes displacements and peculiar velocities accounting for the fact that in cosmologies with massive neutrinos the growth factor and growth rate are scale dependent". I need to look at the papers they referenced here, and make sure I don’t have to change anything with the way, e.g., σ8 is defined.
2. In B18 the authors turn off the short-range force for neutrinos at early times (they turn it on at z=9). This is because their method for generating initial conditions produces multiple neutrino particles in the same position, and when Gadget constructs its tree, particles at very close positions are randomized to complete the tree construction, leading to artifacts in the simulation. Should I just turn off the tree part of Gadget for now? I think Bruno said he won't be using a tree algorithm in Cholla.
3. Do I need to change the transfer function at all when including neutrinos?
4. Will the fast-moving neutrino particles cause a problem with the time-stepping in Gadget?
