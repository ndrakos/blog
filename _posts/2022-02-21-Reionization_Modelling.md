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


### Lyman continuum escape fraction

The LyC escape fraction, $$f_{\rm esc}$$ is the fraction of photons that escape galaxies to ionize intergalactic hydrogen. This is the least constrained quantity out of $$f_{\rm esc}$$,  $$\xi_{\rm ion}$$ and $$\rho_{\rm UV}$$

<a href="https://ui.adsabs.harvard.edu/abs/2020ApJ...892..109N/abstract">Naidu et. al 2020</a> suggests a model in which $$f_{\rm esc} = a \Sigma^{b}_{\rm SFR}$$ (see their equation 8). For now I will consider this model.

## IGM ionized fraction

Reionization can be expressed as the volume-filling fraction of ionized gas:

$$\dfrac{{\rm d} Q_{\rm HII}}{{\rm d}t} = \dfrac{\dot{n}_{\rm ion}}{\langle n_H \rangle} - \dfrac{Q}{\bar{t}_{\rm rec}} $$


$$\dot{n}_{\rm ion}$$: can be calculated as described above

$$\langle n_H \rangle = X_p \Omega_b \rho_c$$ is the co-moving density of hydrogen, where $$X_p$$ is the primordial mass-fraction of hydrogen. Should just be able to calculate from $$\Lambda$$CDM parameters.

$$t_{\rm rec}$$ is the recombination time of ionized hydrogen in the IGM, and is given by Eq 3 in Naidu et al. 2020. There are some assumptions they make when calculating this paramter.

## Future considerations

I am going to begin by calculating the above values, and making sure they are reasonable. However, I want to consider variations to these models. Here are some notable ones:

1. $$\xi_{\rm ion}$$ should be dependent on the exact SED modelling. For now I will use the SED modelling I had originally used in DREaM, but I need to look more into how much variations on this could influence results.

2. The <a href="https://ui.adsabs.harvard.edu/abs/2020ApJ...892..109N/abstract">Naidu et. al 2020</a> model is not firmly established. I might look at other models (e.g. constant fesc), and calculate how well various surveys can constrain this scenario.

3. The value for $$t_{\rm rec}$$ depends on things like the inhomogenity of the IGM. I will explore some of the assumptions here in more detail.
