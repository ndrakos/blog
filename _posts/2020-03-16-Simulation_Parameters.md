---
layout: post
title:  "Simulation Parameters"
date:   2020-03-16

categories: cosmo_sims
---


We will be basing the simulations off of what we need for the *WFIRST* ultra deep field <a href="https://ndrakos.github.io/blog/mocks/">mock catalogue</a>. Here is a summary of the simulation parameters.


## Simulation Parameters

I will use the results from <a href="https://ui.adsabs.harvard.edu/abs/arXiv:1807.06209"> Planck 2018</a> cosmology (last column of Table 2).

$$\Omega_b h^2 = 0.02242 = 0.04893$$

$$\Omega_0 = 0.3111$$

$$\Omega_\Lambda = 0.6889$$

$$H_0 = 67.66$$ km/s/Mpc$$

$$\sigma_8= 0.8102$$

$$n_s = 0.9665$$

As discussed in some previous posts, we will use a box size of $$115\, h^{-1} {\rm Mpc}$$ with $$2048^3$$ particles.
## Softening

Criteria for numerical parameters can be found in <a href="https://ui.adsabs.harvard.edu/abs/2003MNRAS.338...14P/abstract">Power et al. 2003</a>, but there is also an updated paper by <a href="https://ui.adsabs.harvard.edu/abs/2019MNRAS.487.1227Z/abstract">Zhang et al. 2019 </a> that suggest a smaller softening length than the former.

The criteria in the above depends on a specified halo size. I am going to use a softening length of $$1/50$$ the mean particle separation (this seems reasonable given discussion in Zhang et al. 2019).

Noting that the mean particle separation of particles is $$s = (V/N)^(1/3) = {\rm box size}/N^{1/3}$$, this gives a softening length of $$\epsilon = 1.12\, h^{-1} {\rm kpc}$$ for $$2048^3$$ particles. This is pretty similar to the softening that Bruno had decided on for hist simulation <a href="https://bvillasen.github.io/blog/astro/cosmology/wfirst/2017/07/11/sim_parameters.html">here</a>.


## MUSIC Parameter File

I will start at redshift $$z=100$$ (I don't actually have a good reason for choosing this?)

<object width="300" height="300" type="text/plain" data="{{site.baseurl}}/assets/files/wfirst2048_ics.conf" border="0" >
</object>

## Gadget Parameter File

With this cosmology, the mass resolution for $$2048^3$$ particles is $$1.53 \times 10^7 M_*/h$$.
<!---
[6.26145950e+10 7.82682437e+09 9.78353047e+08 1.22294131e+08 1.52867664e+07
-->

500 outputs

## To-Do


1) Try a sample run with $$256**3$$ particles and check everything looks good

2) Make sure I can run the sample run on Pleiades

3) Check how many nodes I can request at once on Pleiades (without being queued too long), and if I will run into problems with storing snapshots

4) Double check with Brant whether $$\sim 500$$ snapshots sounds reasonable
