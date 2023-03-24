---
layout: post
title:  "Reionization Shell Model"
date:   2023-03-23
categories: reion
---

I am planning to calculate the reionized region around each galaxy in the DREaM catalog using a simple shell model, following <a href="https://ui.adsabs.harvard.edu/abs/2018MNRAS.473.5308M/abstract">Magg et al. 2018.</a>.

In the post, I will outline the method for this.


## Overview of Calculation (from Magg et al. 2018)

$$ \dot{N}_{\rm ion} = V n^2 C \alpha + \dot{V} n$$


Here are the values they used:
- $$V$$ is the volume of the ionized region; this is the unknown.  Since ionized regions are small compared to cosmological scales, we can neglect cosmological expansion and redshifting of ionizing photons
- $$\dot{N}_{\rm ion}$$ is the rate of ionizing photons; I have already calculate the instantaneous value for each galaxy
- $$n=0.75 \rho_b/m_p$$ is the current average hydrogen number density; I think this is the same as the comoving $$\langle n_H \rangle$$ value I used in other calculations
- $$C=3$$ is the clumping value. They note that the solution is not sensitive to this choice. I used $$C=3$$ for the $$n_{\rm ion}$$ calculations as well, but noted I might update it to be time-dependent later.
- $$\alpha = 2.6e{-13} {\rm cm}^3 {\rm s}^{−1}$$; This is similar to the value I used for calculating $$n_{\rm ion}$$, though I modelled it with a dependence on temperature.


For calculating the ionizing fraction, I just took the instantaneous ionizing photon rates for galaxies, and solved the ODE as a function of redshift. It is more complicated here, because I want to solve the ODE for each galaxy.


Note that we can rewrite the ODE above as:

$$\dot{V} + [ n C \alpha] V = \dfrac{\dot{N}_{\rm ion}}{n}$$

$$d/dt ({e^{n C \alpha t}} V) = e^{n C \alpha t} \dfrac{\dot{N}_{\rm ion}}{n}$$

$$ V(t) = \dfrac{e^{- n C \alpha t}}{n} \int e^{ n C \alpha t} \dot{N}_{\rm ion} dt $$

Therefore, we need to know  $$\dot{N}_{\rm ion}$$ as a function of time for each galaxy.

## How does Ndot evolve in time?

HereI consider one example galaxy in the catalog. Note that FSPS will return the spectrum as a function of galaxy age age.

Here is the intrinsic spectrum as a function of age, expressed in age of the Universe [Gyr]. This galaxy started forming at ~3.7 Gyr (z~1.8), and is currently at a redshift of ~0.01


<img src="{{ site.baseurl }}/assets/plots/20230323_fnu_vs_t.png">


Here is $$\dot{N}_{ion}$$ as a function of time for this galaxy

<img src="{{ site.baseurl }}/assets/plots/20230323_Ndot_vs_t_1.png">

We are  more interested in the high-z galaxies, so here are 20 galaxies that are located at redshift ~6

<img src="{{ site.baseurl }}/assets/plots/20230323_Ndot_vs_t.png">


## How to proceed?

It seems like it would be feasible to calculate this for every galaxy. I will need to parallelize as before, but I don't see it taking much longer than calculating $$\dot{N}_{\rm ion}$$ as I had before. The slow part is running FSPS, but I won't need to make any extra calls to this.

Next steps:
1. double check that these numbers make sense.
2. Calculate the volume, using the integral above for 1 galaxy, check it looks reasonable
3. write code to do this for all galaxies
4. plot the reionized regions, see if they agree with radiative transfer simulation findings. (i.e., is the percentage of ionized regions reasonable?)
