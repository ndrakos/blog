---
layout: post
title:  "Reionization Modelling"
date:   2022-02-21
categories: reion
---


This post will summarize my initial plans for including reionization modelling with the DREaM galaxy catalog. A lot of the background in this post is from <a href="https://ui.adsabs.harvard.edu/abs/2021arXiv211013160R/abstract">Robertson 2021</a>.


## Production of ionizing photons

The production of ionizing photons from galaxies can be expressed as:

$$\dot{n}_{\rm ion} =  f_{\rm esc} \xi_{\rm ion} \rho_{\rm UV} $$

where $$\dot{n}_{\rm ion}$$ is the comoving ionizing emissivity, $$f_{\rm esc}$$ is the escape fraction of Lyman continuum (LyC) photons, $$\xi_{\rm ion}$$ is the ionizing photon production efficiency, and $$\rho_{\rm UV}$$ is the comoving UV luminosity density.


### UV Luminosities

$$\rho_{\rm UV}$$ can be calculated to from the abundances and luminosities of the galaxies in DREaM, and was already done in the original DREaM paper.


### Intrinsic production rate


$$\xi_{\rm ion}$$ should depend on age, metallicity, SMF and binarity. It can be measured directly from the galaxy SED, as outlined in <a href="https://ui.adsabs.harvard.edu/abs/2020ApJ...892..109N/abstract">Naidu et. al 2020</a>.

Usually $$\xi_{\rm ion}$$ is defined in terms of the rate of ionizing photons, $$N(H^0)$$, per unit UV luminosity, measured at 1500 Angstroms. $$\xi_{\rm ion}$$ can be calculated by integrating the flux produced below the Lyman limit to get $$N(H^0)$$, and then normalizing by the SED-flux at 1500 Angstroms:

$$\xi_{\rm ion} = \frac{N(H^0)}{L_{1500}} [\rm s^{-1} erg^{-1} s^{-1} Hz^{-1}]$$
