---
layout: post
title:  "The Intrinsic Production Rate"
date:   2022-04-121
categories: reion
---


The ionizing photon production efficiency, $$\xi_{\rm ion}$$, is one of the main quantities we need to calculate for the simulated galaxies (see <a href="https://ndrakos.github.io/blog/reion/Reionization_Modelling/">this post</a>). In <a href=
"https://ndrakos.github.io/blog/reion/The_intrinsic_production_rate/">Part I</a> I outlined my calculation, and the initial results.

The solution in my previous post wasn't quite right, so this post includes some corrections, though there is still something wrong!

## Calculation

The production efficiency can be calculated as:

$$\xi_{\rm ion} = \frac{N_{\rm ion}}{L_{1500}} [\rm Hz/erg ]$$

The rate of ionizing photons is in units [photons/s] *not* [photons/s/Hz] as I said in the previous post.

Therefore the calculation should be

$$N(H^0) = \int_{\nu_{912}}^{\infity} \dfrac{L_\nu}{h \nu}  {\rm d} \nu = \int_{0}^{912} \dfrac{L_\nu}}{h \lambda} {\rm d} \lambda$$


Additionally, $$L_{1500}$$ should be in units of [ergs/s/Hz]. This means I can read this directly from $$L{\rm nu}$$, and don't need to integrate anything. However, in practice, I take the average $$L_\nu}$$ value between 1450 and 1550 Angstroms. 


## Generating the spectrum

I was using the rest-frame spectra. This includes dust, IGM absorption. I should be using *intrinsic* rest-frame spectra; i.e. the number of photons created before being absorbed by the IGM, or attenuated by dust.

To fix this I set the following:

1. <code>add_igm_absorption=False</code>: this turns off the IGM absorption
2. <code>add_agb_dust_model=False</code>: this turns off the AGB circumstellar dust model
3. <code>add_dust_emission=False</code>: switch to turns off the Draine & Li 2007 dust emission model.
4. <code>dust_type=0</code>; <code>dust_index=0</code>: This sets the dust attenuation curve to a power law, with index 0


## Some plots

Here are the values calculated for all the galaxies:

<img src="{{ site.baseurl }}/assets/plots/20220421_xi_ion_scatter.png">

The star-forming galaxies are too low, but the quiescent look okay.

Here are what the spectra look like for 10 example galaxies

<img src="{{ site.baseurl }}/assets/plots/20220421_xi_ion_scatter.png">

One potential problem could be the interpolation to find the flux at 912 Angstroms?
