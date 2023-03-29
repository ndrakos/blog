---
layout: post
title:  "Reionization Shell Model Part III"
date:   2023-03-29
categories: reion
---

I am planning to calculate the reionized region around each galaxy in the DREaM catalog using a simple shell model.

This is a continuation from previous posts, <a href="https://ndrakos.github.io/blog/reion/Reionization_Shell_Model/">Part I</a> and <a href="https://ndrakos.github.io/blog/reion/Reionization_Shell_Model_Part_II/">Part II</a>.

## Summary of previous post

As outlined in the previous post, I calculated the volume around each galaxy to be:

$$ V(t) = f_{\rm esc}\dfrac{e^{- n_H C \alpha t}}{n} \int e^{ n C \alpha t} \dot{N}_{\rm ion} dt $$,

which gave values that I suspect are too large, as shown here:

<img src="{{ site.baseurl }}/assets/plots/20230328_Volume.png">

## Expected bubble size


Some relevant (this was from a quick search, not an in-depth literature review):

<a href = "https://ui.adsabs.harvard.edu/abs/2004Natur.432..194W/abstract">Wyithe & Loeb 2004</a>

<a href = "https://ui.adsabs.harvard.edu/abs/2005MNRAS.363.1031F/abstract">Furlanetto & Oh 2005</a>

<a href = "https://ui.adsabs.harvard.edu/abs/2018MNRAS.477.5406Y/abstract">Yajima et al 2018</a>

<a href = "https://ui.adsabs.harvard.edu/abs/2020ApJ...891L..10T/abstract"> Tilvi et al. 2020 </a>


The most relevant plot was in Yajima et al., which shoes the expected (physical) size of bubbles for individual galaxies:

<img src="{{ site.baseurl }}/assets/plots/20230329_Yajima.png">

Looking at these papers, It seems like ~1Mpc (physical), or ~10Mpc (comoving) is about the maximum size of bubble you should expect around an individual galaxy.

Therefore, my calculation is likely not realistic. I think that this might be because I used $$n_H$$ at the present day, when really it should be a function of redshift.

## Derivation

I had begun with this equation (from <a href="https://ui.adsabs.harvard.edu/abs/2018MNRAS.473.5308M/abstract">Magg et al. 2018.</a>.):

$$\dot{V} =  \dfrac{f_{\rm esc}\dot{N}_{\rm ion} (t)}{n_H} -  n_H C \alpha V $$

this equation says that the volume of ionized regions grows with ionizing radiation, and decreases with recombinations. Clearly, the mean hydrogen density, $$n_H$$, should be dependent on time.

Further, looking at Yajima et al., I think I should include the cosmic expansion (which was neglected in Magg+, since it cosmic timescales were large compared to the timescales they considered.)

Therefore, our equation becomes (where I have used primes to denote $$d/dz$$)

$$\dot{V} =  \dfrac{f_{\rm esc}\dot{N}_{\rm ion} (t)}{n_H(z)} + (3H(z) - n_H(z) C \alpha) V(t) $$
$$ - H(z) (1+z) V' =  \dfrac{f_{\rm esc}\dot{N}_{\rm ion} (z)}{n_H(z)} + [3H(z) - n_H(z) C \alpha] V(z) $$
$$ - H(z) (1+z) V' =  \dfrac{f_{\rm esc}\dot{N}_{\rm ion} (z)}{n_H^0 (1+z)^3} + [3H(z) - n_H^0 (1+z)^3 C \alpha] V(z) $$

I cant solve this as pretty as I did before, but I can use on ODE solver (either in python or write my own). This equation will also require calculating $$\dot{N}_{\rm ion}$$ and $$H(z)$$ at each time step in the ODE calculation. This may be significantly slower, so we might want to come up with approximations if the speed becomes prohibitive.


## Next steps

1. Write code to do this for the one galaxy, check the answer makes sense and the speed is okay
2. Once I think this makes sense, write code to do this for all galaxies
3. Plot the reionized regions, see if they agree with radiative transfer simulation findings. (i.e., is the percentage of ionized regions reasonable?)
