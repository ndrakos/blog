---
layout: post
title:  "General model for two-component satellite"
date:   2022-03-18

categories: tidal_stripping
---

Bradley has been analyzing a simulation of a tidally stripped two-component model. The simulation I had given him was for two Hernquist profiles added together (<a href="https://ndrakos.github.io/blog/tidal_stripping/Two_Component_System/">see this post</a>). Now that he has the methodology for this analysis working, I want to start to think about setting up more realistic initial conditions.

## Free parameters

There are many things we can change in the simulation runs:

1. model/parameters describing dark matter component of satellite
2. model/parameters describing stellar component of satellite
3. model/parameters describing background host potential
4. orbital parameters


## The model describing the satellite (dark matter + stellar component)

Tidal stripping of two components is likely dependant on the central density of the systems; namely, how cuspy versus cored the centre of the systems are.

For this reason, I will use the general profile form:

$$\rho(r) = \dfrac{\rho_s}{(r/r_s)^\alpha (1 + r/r_s)^{\beta - \alpha}}$$

Here, the parameters $$\alpha$$ and $$\beta$$ control the inner and outer slopes of the density profile, respectively. An NFW profile has ($$\alpha$$, $$\beta$$)=(1,3) and Hernquist profiles have  ($$\alpha$$, $$\beta$$)=(1,4).

Some relevant references:

- <a href="https://ui.adsabs.harvard.edu/abs/2018MNRAS.480L.106O/abstract">Ogiya 2018</a> uses two component models to study dark matter deficient galaxies (DMDGs). He uses the general profile form above for the dark matter halo, varying $$\alpha$$, and he uses a Hernquist profile for the stellar component. Go finds that he is able to reproduce observations of DMDGs when  (i) the DM halo has a central density core and (ii) the satellite is on a tightly bound and quite radial orbit.

- <a href="https://arxiv.org/abs/2203.02513">Errani et al. 2022</a>, use a cuspy NFW-ish profile and a King model to demonstrate the possible origin of a stellar stream from a dark matter dominant galaxy.

For this project we will mostly be focusing on the dynamics of a two component system in energy space, but likely geared more towards DMDGs. Discussion of dark matter dominant galaxies could also be interesting! Therefore, I plan to use a two-component model where both components can be described by the general profile listed above. This will allow us to change the relative "cuspy-ness" of both the stellar and dark matter component.

One thing to note is that we will have to truncate the particle distribution in cases where the mass profile diverges (e.g. NFW profiles), as is typical when setting up ICs from distribution functions. This would introduce an extra parameter.

## Fiducial satellite parameters

Here is a set of fiducial parameters for the satellite, which we can vary for the different simulations (inspired by <a href="https://ui.adsabs.harvard.edu/abs/2018MNRAS.480L.106O/abstract">Ogiya 2018</a>). Most notably, we will probably change $$\alpha$$ from $$0.1$$ to $$1$$ for both the inner and outer components. For now we will keep $$\beta=4$$, so to avoid the divergent masses when setting up the ICs.


- $$\alpha_{dm}$$ = 0.1
- $$\beta_{dm}$$ = 3
- $$\alpha_{stars}$$ =  1
- $$\beta_{stars}$$ = 4
- $$r_{s,dm}/r_{s,stars} = 10
- $M_{dm}/M_{stars}$ =  200
