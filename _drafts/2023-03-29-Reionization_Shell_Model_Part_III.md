---
layout: post
title:  "Reionization Shell Model Part III"
date:   2023-03-29
categories: reion
---

I am planning to calculate the reionized region around each galaxy in the DREaM catalog using a simple shell model, following <a href="https://ui.adsabs.harvard.edu/abs/2018MNRAS.473.5308M/abstract">Magg et al. 2018.</a>.

This is a continuation from a previous post, <a href="">Part I</a>.

## Expected bubble size


## Calculate the volume around individual galaxies

As outlined in the previous post, we expect the volume around each galaxy to be

$$ V(t) = f_{\rm esc}\dfrac{e^{- n C \alpha t}}{n} \int e^{ n C \alpha t} \dot{N}_{\rm ion} dt $$

<img src="{{ site.baseurl }}/assets/plots/20230328_Volume.png">

These numbers seem too big to me.

Was using $$n=\langle n_H \rangle$$... the comoving... need to use the current number density... i.e., multiple by $$n = \langle n_H \rangle (1+z)^3$$. Then, the (physical) radius of the bubbles are:

<img src="{{ site.baseurl }}/assets/plots/20230329_Volume.png">

Things to note
1) these are on the larger side, but I am looking at galaxies in my "test" catalog, which only contains the brightest sources
2) the bubble size of these individual galaxies eventually decreases... this is liekly because of the declining SFRs. 

## Next steps

1. Dig into the literature, and see what the expected volumes should be
2. Double check the derivation of this equation, and make sure the values I'm using make sense. Should any be time dependent?
3. Once I think this makes sense, write code to do this for all galaxies
4. Plot the reionized regions, see if they agree with radiative transfer simulation findings. (i.e., is the percentage of ionized regions reasonable?)
