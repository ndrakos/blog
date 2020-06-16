---
layout: post
title:  "Two Component System"
date:   2020-06-15

categories: tidal_stripping
---


Peter said he was interested in doing his Lamat project on tidally stripped halos. I would like him to look a bit into how multi-component systems are stripped in energy space, but I am not sure how hard this will be to set up. Here I am going to test whether I can get the ICs work (I will then update my code online that makes ICs, and he could use that to set-up the simulations).

## The Model

I need to think more about what is a realistic model to use. I am most interested in dwarf galaxies that have a dark matter and stellar component. Potentially this could be extended later to include a disk as well (<a href="">Widrow et al. 2005</a> is probably one of the most useful references for this).

For now I am going to simply use two Hernquist models, as these have nice analytic forms:

$$\rho = M_{\rm tot}a/2\pi r (r+a)^3$$)

Here is how this looks (parameters indicated):


<img src="{{ site.baseurl }}/assets/plots/20200615_Model.png">

If I can get this working, I'll give a bit more thought into the best models/parameters to use.

## Assigning Particle Positions and Velocities

I have pretty detailed notes on created isolated ICs <>here<>.

I am going to use N particles for the dark matter component, and N particles for the stellar component. I wish to assign positions and velocities to each particle so that they remain stable. The difficulty with the two-component system is that the potential of each component effects the other, so the density profiles intereact in complicated ways. It's therefore not obvious to me how to gaurentee the individual profiles remain stable, even if the system is constructed so that the total density profile is stable... This is something I need to play around with a bit.

First, the positions are selected from the mass profile... This step is unchanged, and I can select positions for each component.

Secondly, the energies are selected from the distribution function...

The distribution function is given by....


I will break this DF up so that ... now the potential is due to the total system... and can be calculated....
y

## Run in Isolation


<img src="{{ site.baseurl }}/assets/plots/20200615_IC_Stability.png">
