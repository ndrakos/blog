---
layout: post
title:  "Neutrino Positions in MUSIC"
date:   2022-04-28
categories: cosmo_ics
---

<a href="https://ndrakos.github.io/blog/cosmo_ics/MUSIC_code_breakdown/">This post</a> outlines the MUSIC code, and the changes I need to make to put in neutrinos. I also looked into detail on how to assign velocities.

In this post I'm going into more detail on position assignments.

## Calculating

Effectively, the neutrinos are calculated the same as the CDM particles, and then given an additional thermal velocity.

Important modifications: (1) initial density field of neutrinos should be set by neutrino power spectrum and (2) we are doing the neutrinos on a more coarse grid.

## Density Field

The density field is calculated in <code>densitites.cc</code> using the function <code>GenerateDensityHierarchy</code>.

Here are all the inputs, and what I need to change for neutrinos compared to calculating for dark matter or baryons.

Inputs:
1. <code>config_file &cf</code> -- config file
- Same for CDM and baryons
- Does not need to change for neutrinos
2. <code>transfer_function *ptf</code> --  transfer function plugin  
- Same for CDM and baryons
- Set in function <code> select_transfer_function_plugin( cf )</code>
- Does not need to change for neutrinos
3. <code>tf_type type</code> -- This is the transfer function type
- Different for CDM (either the CDM or the total power spectra) and baryons (baryon power spectra)
- **I need to include a neutrino power spectrum here**
4. <code>refinement_hierarchy &refh</code> -- ???
- Same for CDM and baryons (rh_TF)
-?
5. <code>rand_gen &rand</code> -- random number generator kernel
- Same for CDM and baryons
- Does not need to change for neutrinos
6.  grid_hierarchy &delta -- This is an object which holds the density field
- This doesn't need to be changed. It's just where the density field will be stored.
7.  <code>bool smooth</code>
- False for CDM. True for baryons if SPH
- Set to False for neutrinos
8.  <code>bool shift</code>
- Set to true for baryons if SPH and the output format isn't glass
- Set to False for neutrinos

Then...

coarsen_density(rh_Poisson, f, bspectral_sampling);
f.add_refinement_mask( rh_Poisson.get_coord_shift() );
normalize_density(f);




### Potential

The potential for the CDM (and baryons) are calculated from the following:

```
grid_hierarchy u( f );	u.zero();
err = the_poisson_solver->solve(f, u);
```

<code>f</code> is the density, and <code>u</code> is the object that stores the potential.


### Displacements

The displacements for CDM (and baryons) are calulated as:

```
the_poisson_solver->gradient(icoord, u, data_forIO );
coarsen_density( rh_Poisson, data_forIO, kspace );
```

- <code>icoord</code> -- equal to 0,1,2 and corresponds to the x,y,z component
- <code>u</code>
- <code>data_forIO</code>
- <code>rh_Poisson</code>
- <code>kspace</code> -- boolean, set to false?

## Neutrino Assignment

For now I'm just going to assign Neutrinos using the DM transfer function... Really should be using the neutrino power spectrum to set this?


## Next Steps

I am pretty much at the point to run the hacked MUSIC code (blog post forthcoming).

Once this is running, I can look at the power spectra of the neutrinos, and verify that the ICs look correct. I've detailed the steps above that I'm not entirely confident about, so that is where I can start for troubleshooting if the power spectra isn't right.
