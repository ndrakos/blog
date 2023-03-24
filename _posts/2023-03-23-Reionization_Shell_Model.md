---
layout: post
title:  "Reionization Shell Model"
date:   2023-03-23
categories: reion
---

I am planning to calculate the reionized region around each galaxy in the DREaM catalog using a simple shell model, following <a href="https://ui.adsabs.harvard.edu/abs/2018MNRAS.473.5308M/abstract">Magg et al. 2018.</a>.

In the post, I will outline the method for this.


## Overview of equation from Magg et al. 2018

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
$$\dot{e^{n C \alpha t} V) = e^{n C \alpha t} \dfrac{\dot{N}_{\rm ion}}{n}$$
$$ V(t) = \dfrac{e^{- n C \alpha t}{n} \int e^{ n C \alpha t} \dot{N}_{\rm ion} dt $$

Therefore, we need to know  $$\dot{N}_{\rm ion}$$ as a function of time for each galaxy.
