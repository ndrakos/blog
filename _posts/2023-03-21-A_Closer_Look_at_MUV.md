---
layout: post
title:  "A Closer Look at MUV"
date:   2023-03-21
categories: reion
---

In this post, I want to go over intrinsic/dust-corrected $$M_{\rm UV}$$ versus the observed value.

DREaM gives the observed value, while I use the intrinsic to calculate the number of ionizing photons produced by each galaxy.

## Intrinsic production rate of ionizing photons

The intrinsic production rate of ionizing photons of an individual galaxy, $$\dot{N}_{\rm ion}$$, can be obtained from integrating over the intrinsic SED

$$\dot{N}_{\rm ion} = \int_{\nu_{912}}^{\infty} \dfrac{L_\nu}{h \nu}  {\rm d} \nu = \int_{0}^{912} \dfrac{L_\nu}{h \lambda} {\rm d} \lambda$$

Calculating $$\dot{N}_{\rm ion}$$ was outlined in Posts <a href="https://ndrakos.github.io/blog/reion/The_intrinsic_production_rate/">I</a>, <a href="https://ndrakos.github.io/blog/reion/The_Intrinsic_Production_Part_II/">II</a> and <a href="https://ndrakos.github.io/blog/reion/The_Intrinsic_Production_Part_III/">III</a>


In practice, $$\dot{N}_{\rm ion}$$ is not directly observable due to (1) absorption of ionizing photons by the IGM and (2) attenuation by dust. Therefore, it is typically calculated as:

$$\dot{N}_{\rm ion} = \xi_{\rm ion} L_{1500}$$

## Comparison between intrinsic and observed UV Luminosity

The intrinsic UV luminosity is higher than the measured value (note these are only the most massive galaxies in the DREaM catalog):

<img src="{{ site.baseurl }}/assets/plots/20230321_MUV.png">


I'm not sure how dust corrections are done in practice. Naidu2020 mentions they corrected "for dust using the UV continuum prescription of Bouwens et al. (2014).", but it wasn't obvious to me how this is done.

For this work, I'm going to use the intrinsic $$L_{1500}$$, and not worry about correcting the $$M_{\rm UV}$$ values. This might be something I look into more in the future.  
