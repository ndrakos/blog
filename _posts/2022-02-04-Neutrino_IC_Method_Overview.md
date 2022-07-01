---
layout: post
title:  "Neutrino IC Method Overview"
date:   2022-02-08
categories: cosmo_ics
---

In this post, I will outline the methods in <a href="https://ui.adsabs.harvard.edu/abs/2018JCAP...09..028B/abstract">Banarjee et al 2018 </a> (B18) for setting up neutrino ICs.


## Method

In this method, the neutrinos are treated as a separate $$N$$-body species.  In addition to a bulk velocity determined by the power spectrum, each neutrino particle is also given a random thermal velocity by sampling the Fermi-Dirac distribution.

Specifically, for every point on the grid where the ICs are generated, the magnitude of velocity for each neutrino is calculated from dividing up the Fermi-Dirac distribution, and the directions given by dividing up the spherical velocity shell into equal area elements.

There are then multiple neutrinos for every grid point that sample this distribution, and the neutrinos are the same at every grid point. They are purposely constructed NOT to have a randomness in the distribution.

### Assign velocity magnitude

The neutrino distribution at redshift $$z$$ is given by:

$$f(p) = \dfrac{4 \pi g_\nu}{(2 \pi \hbar)^3} \dfrac{1}{\dfrac{pc}{e^{k_B T_\nu (1+z)}} + 1} $$

where $$p$$ is the magnitude of the momentum, $$g_\nu$$ is the magnitude of the degeneracy, and $$T_{\nu} = 1.95$$ K is the neutrino temperature today. The velocity distribution is $$v \propto p^2 f(p)$$.

Typically, you would sample randomly from this distribution. This is NOT what they do in this paper, as that method suffers heavily from shot noise. Instead, they sample velocity in a regular manner, that is replicated at every point on the grid used to generate the ICs.


#### Step 1: Divide the Fermi-Dirac distribution into shells

They divide the distribution into $$N_{\rm shell}$$ equal-mass shells as follows:

$$\dfrac{\int_{p^i_{\rm min}}^{p^i_{\rm max}} p^2 f(p) dp }{\int_{0}^{p_{\rm max}} p^2 f(p) dp} = \dfrac{1}{N_{\rm shell}}$$

where $$p_{\min}^i$$ and $$p_{\max}^i$$ are the minimum and maximum momentum of the shell. $$p_{\max}$$ is  a free parameter that is chosen as a "reasonable" value to truncate the distribution.

B18 also considers dividing the distribution into non-equal mass shells. This allows for better resolution of slow-moving shells. They found that it is important to sample these shells to match the cross spectrum (how correlated the clustering of neutrinos are with respect to CDM) at low-redshifts. This is slightly more complicated, as each "particle" will have a different mass. For now, I will only consider the equal-mass case, but I should probably update this later, to get better agreement with the cross spectrum.

#### Step 2: Set the magnitude of velocity for each shell

The magnitude for each shell is given by:

$$\langle p_i \rangle = \sqrt{\dfrac{   \int_{p^i_{\rm min}}^{p^i_{\rm max}} p^4 f(p) dp }{  \int_{p^i_{\rm min}}^{p^i_{\rm max}} p^2 f(p) dp }}$$.

###  Assign angular direction

Each shell is divided into equal area elements. They used the algorithm HEALPIX, but any algorithm that uniformly divides a unit sphere would work.

The number of elements per sphere are $$12 N_{\rm side}^2$$. As discussed in B18, if $$N_{\rm side}$$ is small (i.e 1 or 2), there are some residual anisotropies in the distribution, which they correct by rescaling the velocities.


### Final steps

Therefore there are $$12 \times N_{\rm side}^2 \times N_{\rm shell}$$ neutrino particles per gridpoint, with the number of neutrino IC gridpoints being defined as $$N_{\rm grid}^3$$. This results in a total number of $$12 \times N_{\rm side}^2 \times N_{\rm shell} \times N_{\rm grid}^3$$ neutrino particles.

Particles are displaced off of grids using Zeldovich approximation, and the masses are adjusted to give correct $$\Omega_\nu$$ for the simulation box.



## Choosing parameters

There are four free parameters in the procedure outlined above:
$$p_{\rm max}$$, $$N_{\rm shell}$$, $$N_{\rm side}$$, $$N_{\rm grid}$$
There are also parameters associated with the neutrino model. I will only consider the degenerate neutrino mass scenario, where all the individual mass eigenstates are equal in mass.

$$p_{\rm max}$$ is not specified in the paper, but is chosen to be "reasonable". In the fiducial case in B18 they have $$N_{\rm shell}=10$$, $$N_{\rm side}=2$$, $$N_{\rm grid}=128$$ (resulting in $$1002^3$$ particles), and break the Fermi-Dirac distribution into unequal mass shells.

In general, $$N_{\rm grid}$$ is chosen to be more coarse than $$N$$ (the number of dark matter particles are $$N^3$$), but so that the total number of particles are roughly the same for CDM particles and neutrino particles (same order of magnitude).

At higher redshifts, they found $$N_{\rm side}$$ was important to match the power spectrum, and found good agreement with $$N=4$$. At lower redshifts $$N=2$$ seemed to work fine. I will keep $$N_{\rm side}=3$$, so I don't have to bother correcting the velocity anisotropies.  

They found that at high redshifts the matter spectrum was insensitive to $$N_{\rm shell}$$, while low redshifts required $$N_{\rm shell}$$ large enough to sample the low-velocity shells to reproduce the cross spectrum. To keep the number of particles small, for now I will use $$N_{\rm shell}=5$$, but I will probably need to increase this later, and switch to an un-equal mass scheme.




## Things to think about

### Zeldovich

I am not sure whether the Zeldovich approximation is a typical thing done to all the particles, or if I have to implement this specifically for the neutrino particles. This will require me reviewing how MUSIC works.

### Change to un-equal mass scheme

As outlined above, I probably need to change to an unequal mass scheme. I will test this later on the cross spectrum, once I verify that I have the procedure working.

### Is there anything else to worry about when modifying MUSIC to include this species?

In B18 they say the "modify a version of N-GenIC that computes displacements and peculiar velocities accounting for the fact that in cosmologies with massive neutrinos the growth factor and growth rate are scale dependent". I need to look at the papers they referenced here, and make sure I don't have to change anything with the way, e.g., $$\sigma_8$$ is defined.

### Running in Gadget

An advantage to this method is that it doesn't require modifications to the $$N$$-body code, only a separate population of particles.

One exception to this, is that the authors turn off the short-range force for neutrinos at early times (they turn it on at $$z=9$$). This is because their method for generating initial conditions produces multiple neutrino particles in the same position, and when Gadget constructs its tree, particles at very close positions are randomized to complete the tree construction, leading to artifacts in the simulation.

I am unsure of (1) how to implement this in gadget (2) how straightforward it will be to but it into Cholla and (3) whether there is a way around this. This is something I will need to think about once I get the Gadget simualations running.
