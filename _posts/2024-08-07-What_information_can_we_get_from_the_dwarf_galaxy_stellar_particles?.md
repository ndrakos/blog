---
layout: post
title:  "What information can we get from the dwarf galaxy stellar particles?"
date:   2024-08-07
categories: tidal_stripping
---

One of the thing I want to explore with the two-component stripping simulations is how to use the observable stars to get information about the merging system 


## Potential of the Satellite

If you look at all the particles (dark matter and stellar) in phase space, you get this:

<img src="{{ site.baseurl }}/assets/plots/20240807_phasespace_tot.png">

The star particles look very similar, but don't extend quite as far out in radius:

<img src="{{ site.baseurl }}/assets/plots/20240807_phasespace_stars.png">

Theoretically, the edge of this distribution should correspond to when the kinetic energy is equal to the potential energy. If the kinetic energy is higher, than the particles will be stripped off. 

If we instead change the y-axis in these phase-space plots to be the kinetic energy (1/2v^2), this is maybe a bit clearer:

<img src="{{ site.baseurl }}/assets/plots/20240807_phasespace_pot.png">

The bottom edge of this distribution should correspond to the gravitational potential of the system. 

My idea was that if we can determine the edge of this distribution, and fit a profile to it, we can get the full potential of the system.

However, if we compare the top right to the real potential, this doesn't seem to work well. 

Here is the potential corresponding to the system in the top left phase-space plot:

<img src="{{ site.baseurl }}/assets/plots/20240807_potential.png">

I would expect the green curve (considering all of the bound particles) to match with the bottom of the distribution. However, the potential (calculated from the particles) seems to be quite a bit deeper than indicated from the phase-space plot. 

I'm not sure why this is. It could simply be a resolution issue --- i.e. there are just very few particles that will fill out that section of the phase space plot. This seems unlikely given that the dark matter particles (of which there are quite a few more) have the same edge.
Its also possible that we need to take into account the local potential of the host, which is effectively a background potential. I think that is probably the more likely scenario, and I might try and calculate that later.


## Mass of the Satellite

Another thing we can do is try and calculate the total mass of the satellite given the dark matter component. 

Looking at the bound particles for M10_R2_00A at snapshot 10, we should get a total mass of 0.32 (0.05 in the stars and 0.27 in the dark matter). 


A simple virial theorem argument (originally used by Fritz Zwicky), which assumes that the density of the satellite is constant, gives:


$$M \approx \dfrac{5 R \langle v^2 \rangle}{3 G} $$

Assuming the edge of the system is at $$R\approx 5$$, and calculating the average velocity of all the particles inside gives a total mass of 0.2. This is lower than the true value of 0.3, but $$R=5$$ is honestly probably an underestimate, and the assumption it is uniform density isn't great.



## Pericenter

We also know that the average density of the satellite is related to the average density of the host at pericenter:

$$\bar{\rho}_{sat}(<r_{sat}) = \eta \bar{\rho}_{host} (<r_p)$$.

Using the (known) density profile of the host halo, and $$\eta= 2 - d\ln M / d\ln r $$ (from Tormen+1998), this gives

$$ \dfrac{M_{sat}}{r_{sat}^3} = 2\dfrac{M_{host}(<r_p)}{r_p^3} - \rho_{host}(r_p)$$

I solved this numerically (with Msat=0.2, r_sat=5), and got $$r_p=66$$, which is very close to the real value of 64!


## Pitfalls, assumptions, ect

Satellite assumptions
- We assume that we can get a pretty good measurement of $$v^2$$ 
- We assumed there is not a significant gas component
- We assumed the satellite was constant density

Host assumptions
- We assumed that we know the density profile of the host pretty well

Other
- we assumed that the equation, and eta value we used to relate the host and satellite holds. In particular, the prescription of $$\eta$$ we used neglects the centrifugal force
- In general, my main dissatisfaction with this result is that we didn't use the Energy Truncation picture at all in the calculation... but that isn't really a problem


