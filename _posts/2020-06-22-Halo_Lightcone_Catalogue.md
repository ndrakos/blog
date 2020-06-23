---
layout: post
title:  "Halo Lightcone Catalogue"
date:   2020-06-22

categories: mocks
---


Previously, I created a lightcone from AHF halo catalogues, consisting of 3D positions and redshifts for each host halo, in a volume of $$(60*115,115,115)\, {\rm Mpc/h} $$. I want to create a halo catalogue, that also includes all the subhalos, for the halos that fall in the survey volume.


## Subhalos

We are interpolating to find the positions and velocities of each host halo between snapshots $$j$$ and $$j+1$$. I am not doing the same thing with the subhalos, because I was worried that interpolating positions and velocities for the subhalos might cause them to be off-set from their host halos in an unphysical way. My solution is to find all the subhalos in each host at snapshot $$j+1$$, and then place them in the host halo, and give them same offset in position and velocity from their host that they have in snapshot $$j+1$$ (currently we are taking the properties of the halo at snapshot $$j+1$$... later we might use some other criteria to decide whether to take properties from $$j$$ or $$j+1$$).



## Survey volume

Out survey volume is approximately 1 square degree. I want to convert the $$(x,y,z)$$ positions of each
(sub)halo to an angular position.

I can calculate a distance, RA and Dec for each halo as follows:

$$d = \sqrt(x*x + y*y + z*z)$$
$$RA = \arctan(y/x)$$
$$Dec = \arcsin(z/d)$$

Then, I only consider (sub)halos with $$RA<1$$ and $$Dec<1$$ degree. Further, I only take halos with $$d<60*115$$; this is because the lightcone is not complete for distances larger than this (this doesn't actually make a difference, because there aren't halos out that far). Finally, I recenter the survey by rotating the $$(x,y,z)$$ coordinates by angles $$(psi,phi,theta) = (-0.5,0,0.5)$$; now, the x-axis corresponds to the distance from the observer.

Here is a resulting scatter plot of the halo catalogue in the (new) cartesian coordinates (for the $$512^3$$ simulation):

<img src="{{ site.baseurl }}/assets/plots/20200622_HaloLightCone.png">
