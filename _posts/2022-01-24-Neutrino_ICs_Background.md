---
layout: post
title:  "Neutrino ICs Background"
date:   2022-01-24
categories: cosmo_ics
---



The plan for this project is to figure out how to put massive neutrinos in cosmological ICs, following <a href="https://ui.adsabs.harvard.edu/abs/2018JCAP...09..028B/abstract">Banarjee et al 2018 </a> (B18).

This post will review some of the motivation and background, mainly from B18.



## Motivation

Neutrinos are one of the most abundant particles in the universe, and their number density is about equivalent to photons. Current constraints on the cosmic neutrino temperature imply that massive neutrinos are highly non-relativistic today, and can gravitationally cluster. Neutrino oscillation experiments constrain the mass square differences between neutrinos, but can't determine the absolute mass scale, or the total mass of the three eigenstates. There are bounds on sum of neutrino masses from astronomical sources include CMB lensing, Ly-alpha forest power spectrum, galaxy-galaxy lensing and BAO; almost all of the astronomical constraints are based on measuring the small scale damping of the power spectrum. Massive neutrinos damp power spectrum on scales before the free streaming scale, and this damping proportional to the total energy density in neutrinos.


Both the clustering and power spectra are well understood on linear scales (i.e. large scales and early times), but we need to run simulations to understand on non-linear scales. However, there are a lot of technical problems to adding neutrinos to simulations. B18 offers a possible straight-forward solution.


## Adding Neutrinos to Simulations

Unlike cold-dark-matter, neutrinos have high thermal velocities. Broadly, there are two approaches to add neutrinos to simulations:

### 1) Treat neutrinos as a linear fluid on a grid, coupled to the N-body evolution of CDM particles


Pros: Good for intermediate scales, high redshifts, and captures CDM component evolution quite well

Cons: Quasi-linear methods break down when over-densities in the neutrino fluid are of order 1. Neutrino component becomes inaccurate once there is significant clustering.


### 2) Treat neutrinos as a different species of particles with different a different mass

Each neutrino has a bulk velocity determined by the power spectrum, plus an extra thermal velocity from the Fermi-Dirac distribution.

Pros: Fully non-linear.

Cons: Shot-noise in the power spectrum. Neutrinos have large thermal velocities at high-redshifts, and cross the simulation box multiple times. They quickly lose memory of ICs, and distribute randomly in the box. The assumption that the number of particles in a region represent the physical density breaks down, and the number of neutrinos in a region is just described by Poisson statistics.

B18 proposes a method to remove the shot-noise by changing the way the ICs are set-up.


## Questions

1) Will this method also work for warm/hot dark matter simulations? The streaming length of WDM is smaller than that of neutrinos.

2) When running hydro simulations do you need to do anything different to create the particle ICs?

3) What are the things we want to test in simulations? What is the division for what e.g. Bruno will do versus me?

## Next Step

Go through the calculations for adding in the neutrinos in B18.
