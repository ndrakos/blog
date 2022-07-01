---
layout: post
title:  "Neutrino Positions in MUSIC"
date:   2022-07-01
categories: cosmo_ics
---

<a href="https://ndrakos.github.io/blog/cosmo_ics/MUSIC_code_breakdown/">This post</a> outlines the MUSIC code, and the changes I need to make to put in neutrinos. I also looked into detail on how to assign velocities.

In this post I'm going into more detail on position assignments.

## Calculating Neutrino Positions

Effectively, the neutrinos are calculated the same as the CDM particles, and then given an additional thermal velocity.

Important modifications: (1) initial density field of neutrinos should be set by neutrino power spectrum (e.g. using neutrino transfer function) and (2) we are doing the neutrinos on a more coarse grid.

The calculation is inserted into <code>main.cc</code> after calculating the dark matter density positions. I will calculate the density field, then the potential, and then the displacements.


## Refinement hierarchy

I need to define refinement_hierarchy object (in main, under section titles "determine the refinement hierarchy") for the coarse grid used for neutrinos.

I will define this object as <code>rh_Poisson_coarse</code>

In main, I wrote a function to calculate this:

```
void modify_grid_for_neutrinos( const refinement_hierarchy& rh_full, refinement_hierarchy& rh_nu, config_file& cf )
{
	unsigned lbasenu, lbase, lmax;
	lbase				= cf.getValue<unsigned>( "setup", "levelmin" );
	lmax				= cf.getValue<unsigned>( "setup", "levelmax" );
	levelnu				= cf.getValueSafe<unsigned>( "setup", "level_neutrinos", lbase );
	rh_nu = rh_full;
	for( unsigned i=lbase+1; i<=lmax; ++i )
	{
		rh_nu.adjust_level(i, levelnu, levelnu, levelnu, 0, 0, 0);
	}

}
```

The function <code>adjust_level</code> should "cut a grid level to the specified size", and its inputs are:
- ilevel: grid level on which to perform the size adjustment
- nx, ny,nz:  new extent in fine grid cells
- oax,oay,oaz:  new offset in units fine grid units




## Density Field

The density field is calculated in <code>densitites.cc</code> using the function <code>GenerateDensityHierarchy</code>. For the DM component, here is the relevant code in <code>main.cc</code>

```
grid_hierarchy f( nbnd );
tf_type my_tf_type = total;
GenerateDensityHierarchy(	cf, the_transfer_function_plugin, my_tf_type , rh_TF, rand, f, false, false );
coarsen_density(rh_Poisson, f, bspectral_sampling);
f.add_refinement_mask( rh_Poisson.get_coord_shift() );
normalize_density(f);
```

Here are all the inputs to <code>GenerateDensityHierarchy</code>, and what I need to change for neutrinos compared to calculating for dark matter or baryons.

Inputs to <code>GenerateDensityHierarchy</code>:
1. <code>config_file &cf</code> -- config file
- Same for CDM and baryons
- Does not need to change for neutrinos
2. <code>transfer_function *ptf</code> --  transfer function plugin  
- Same for CDM and baryons
- Set in function <code> select_transfer_function_plugin( cf )</code>
- Does not need to change for neutrinos
3. <code>tf_type type</code> -- This is the transfer function type
- Different for CDM (either the CDM or the total power spectra) and baryons (baryon power spectra)
- This should be set to neutrinos **I need to add this option to the code. Note CAMB should be able to calculate this.**
4. <code>refinement_hierarchy &refh</code> -- grid structure for the density convolution
- Same for CDM and baryons (rh_TF)
- I think, even though the grid will be more coarse for neutrinos, this can be left the same. e.g. "the density field will be averaged down after the convolution has been performed and the Poisson solver is invoked".
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


The rest I will keep mostly the same. Except:
1.  <code>rh_Poisson</code> -- grid struture for poisson solver.
- This I will change to rh_Poisson_coarse


### Potential

The potential for the CDM (and baryons) are calculated from the following:

```
grid_hierarchy u( f );	u.zero();
err = the_poisson_solver->solve(f, u);
```

<code>f</code> is the density, and <code>u</code> is the object that stores the potential.


I kept this same for neutrinos.


### Displacements

The displacements for CDM (and baryons) are calculated as:

```
grid_hierarchy data_forIO(u);
for( int icoord = 0; icoord < 3; ++icoord )
{
  the_poisson_solver->gradient(icoord, u, data_forIO );
  coarsen_density( rh_Poisson, data_forIO, kspace );
  the_output_plugin->write_dm_position(icoord, data_forIO );
}
```

Functions:
1. <code>data_forIO</code>
  - <code>u</code> -- the gravitational potential
2. <code>the_poisson_solver</code>
  - <code>icoord</code> -- equal to 0,1,2 and corresponds to the x,y,z component
3. <code>coarsen_density</code>
  - <code>rh_Poisson</code> -- grid struture for poisson solver. I will change this to <code>rh_Poisson_coarse</code>
  - <code>kspace</code> -- whether to do this calculation in kspace. I'll just keep this to false, which is what the cdm component uses.
4. <code>write_dm_position</code>: This is contained in the output.  **I need to write one for neutrinos**

## Testing code

I tested compiling this hacked version of <code>MUSIC</code>, <code>MUSICnu</code>, but with
- the neutrino tf_type set to cdm, because I haven't coded the neutrino bit yet
- write_dm_position instead of  write_neutrino_position

This compiled fine, which is good.


## Next Steps

1. Add the neutrino transfer function (I think this can just be done using the CAMB transfer function plug-in, already encor)
2. Add the velocity bit into the code (this has already been coded, just needs to be pasted in the right part)
3. Add code for Gadget outputs, as I outlined <a href="https://ndrakos.github.io/blog/cosmo_ics/MUSIC_code_breakdown/">here</a>

Once this is running, I can look at the power spectra of the neutrinos, and verify that the ICs look correct.
