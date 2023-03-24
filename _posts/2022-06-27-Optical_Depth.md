---
layout: post
title:  "Optical Depth"
date:   2022-06-27
categories: reion
---

In this post, I calculate the Thompson scattering optical depth for the DREaM Catalog

## Calculation


Thompson Optical Depth (from eq6 of Naidu et al.):

$$ \tau = c \bar{n_H} \sigma_T \int_0^z f_e Q_{H_{II}} \dfrac{(1+z')^2}{H(z)} dz'$$

where

- $$c$$: speed of light
- $$\bar{n}_H$$: comoving hydrogen density ($$1.9 \times 10^{-7} \rm{cm}^3$$)
- $$\sigma_T$$: electron Thomson scattering cross-section ($$6.6524587158 \times 10^{-29 \rm{m}^2}$$)
- $$f_e$$ = number of free electrons for every hydrogen nucleus in the ionized IGM, $$f_e = (1+(1−X)/4X)$$
- $$Q_{H_{II}}$$: Ionized fraction (calculated as <a href="https://ndrakos.github.io/blog/reion/IGM_Neutral_Fraction/">here</a>)
- $$H(z)$$: Hubble parameter

## Results

Here is the plot, compared to the Planck 2019 data:

<img src="{{ site.baseurl }}/assets/plots/20220627_optical_depth.png">

Looks good!
