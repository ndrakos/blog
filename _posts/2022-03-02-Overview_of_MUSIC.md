---
layout: post
title:  "Overview of MUSIC"
date:   2022-03-02
categories: cosmo_ics
---

In this post, I will outline the basic algorithm in the code in MUSIC (<a href="https://ui.adsabs.harvard.edu/abs/2011MNRAS.415.2101H/abstract">Hahn and Abel 2011</a>), and think about what needs to be altered to add neutrino ICs. MUSIC uses a nested grid, which we don't really care about for our applications, so I will ignore that.

## MUSIC algorithm

### Compute density field

The IC density field is created from the convolution of a Gaussian random field and the real-space power spectrum:

$$\delta(\mathbf{r}) = T(|\mathbf{r}|) * \mu(\mathbf{r})$$

This is the Gaussian overdensity field, and is the source field of the displacements, but NOT the density field measured after displacing the particles.

$$\mu(\mathbf{r})$$ is typically sampled from a Gaussian distribution with zero mean and unit variance.


### Compute position and velocity fields

To get positions and velocities from the density field, Poisson's equations are solved. They use second order Lagrangian Perturbation Theory (LPT) to do this (Note: Zel'dovich approximation refers to the first-order Lagrangian Perturbation theorem)


## How neutrinos fit in

I summarized the method for adding neutrino ICs in <a href="https://ndrakos.github.io/blog/iso_ics/Neutrino_IC_Method_Overview/">this post</a> (B18): the neutrinos are initially placed on a coarse grid, with $$N_n$$ particles per grid point. They are assigned velocities from the Fermi-Dirac distribution. The particles are displaced off the grid using a Zel-dovich approximation.

The velocities can be generated as described in the neutrino post, and the positions can be generated in the same way as the dark matter particles. Since MUSIC uses second-order LPT, we will also do that for the neutrinos. This should be straightforward, since I can just use the code that already exists for the LPT.

I assume we use the density field from the dark matter particles (since neutrino distribution will initially be uniform). In B18, it seems like they generated $$N_n$$ neutrino particles and one cold dark matter particle at every grid point before applying LPT.



## Next Steps

There are a couple of things I can do next:

1. Go through the actual MUSIC code, and exactly where/how this can be implemented.

2. Test out the algorithm for assigning velocities (sampling the distribution + HEALPIX algorithm or similar), and make sure I have this working. I could either try this in Python, or code it in C, since that is what I'll need to do for MUSIC.
