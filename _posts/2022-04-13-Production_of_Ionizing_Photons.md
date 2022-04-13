---
layout: post
title:  "Production of Ionizing Photons"
date:   2022-04-13
categories: reion
---

As described in <a href="https://ndrakos.github.io/blog/reion/Reionization_Modelling/">this post</a>), we want to calculate the production of ionizing photons.



## Calculation

The production of ionizing photons is given by:

$$\dot{n_{\rm ion}} = f_{\rm esc} \xi_{\rm ion} \rho_{\rm UV}$$

where $$\rho_{\rm UV}= \int_0^{\infty} \phi(L) {\rm d}L$$.


Using the values from the catalog this can be rewritten as:

$$\dot{n_{\rm ion} = \dfrac{\sum f_{\rm esc} xi_{\rm ion}  L_{\rm 1500}  }{V}$$,

where $$xi_{\rm ion}$$ is in units [Hz/ergs] and $$L_{\rm 1500}$$ is in units ergs/Hz/s (I need better notation here).  $$L_{\rm 1500}$$ can be calculated from the UV magnitude.


## Results

Here is what I get (using the test catalog, that only contains more massive galaxies)

<img src="{{ site.baseurl }}/assets/plots/20220413_ndot.png">


If I compare this to Fig 7. From Naidu2020,

<img src="{{ site.baseurl }}/assets/plots/20220413_NaiduFig7.png">

you can see that I have roughly the right shape, but my rate is much smaller, and drops off faster. I am, however, using a truncated catalog that only contains the most massive galaxies.


## Next Steps

I'm going to calculate all of this for the full DREaM catalog, and see if my numbers make more sense (I probably should make the same mass cuts to see if I get the same numbers as in e.g. Naidu2020).

If they work, great! Otherwise I'll need to troubleshoot all the ingredients a bit more carefully. In particular, I need to dig into $$\xi_{\rm ion}$$ a bit more, since those calculations seemed like they might be a little off.
