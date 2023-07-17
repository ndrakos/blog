---
layout: post
title:  "Lyman Alpha Emitters"
date:   2023-05-23
categories: reion
---

One of the goals of this project is to find out where the Lyman Alpha Emitters are located.

I will start by following an approach similar to Yajima+2018, Cen+2000. These are my notes on how to do the calculation.


## Lyman alpha Luminosity


Can estimate the Lyman alpha Luminosity using (eq 5 of Yajima+2018):

$$L = 0.68 (1-f_{\rm esc}) f_{esc, Ly\alpha} \epsilon_{Ly\alpha} \dot{N}_{\rm ion}$$

- I'm not sure where 0.68 comes from.
- $$(1-f_{\rm esc})$$ are the photons that *don't* escape to reionize the Universe, but instead are absorbed by the ISM.
- $$f_{esc, Ly\alpha}$$ is the escape fraction of Ly$$\alpha$$ from the galaxy. Yajima adopts a value of 0.6. I need to think about where this comes from, and if it should be different for the two cases.
-  $$\epsilon_{Ly\alpha}=10.2$$ eV is the energy of a Ly$$\alpha$$ photon
- $$\dot{N}_{\rm ion}$$ is the rate of ionizing photons produced by the galaxy, which I already calculated from the galaxy spectra.


If we use the assumption $$f_{esc, Ly\alpha}=0.6$$ this is straight-forward to calculate, and then we can calculate how much this is affected by the surrounding bubble to get a measured brightness


## Transmission

Optical depth can be calculated as follows, where I have divided the integral into two parts; one for outside the bubble, and one for inside the bubble. The first term should really dominate the calculation.


$$ \tau (\lambda_{obs}, z) = \int_{z_r}^{z_s} dz' c \dfrac{dt}{dz'} n_H(z') \sigma_{Ly\alpha} [\lambda_{obs} / (1+z')] + \int_{z_s}^{z} dz' c \dfrac{dt}{dz'} n_{H}(z') x_{HI}  \sigma_{Ly\alpha} [\lambda_{obs} / (1+z')] $$

- $$cdt/dz$$ is the line element in the given cosmology
- $$n_H(z')$$ is the hydrogen density, which I used in the previous calculation
- $$x_{HI}$$ is the neutral fraction. It is assumed to be 1 outside the bubble. Inside the bubble, it can be calculated as shown below.
- $$\sigma_{Ly\alpha}$$ is the  scattering cross-section for HI gas. This calculation is also shown below
- $$z_r$$ is the reionization redshift, but is not sensitive to this. Both Cen+ and Yajima+ set this equal to 6. I will set it equal to where Q=0.
- $$z_s$$ is the redshift at the edge of the bubble


Calculation for the neutral fraction inside the bubble:

$$x_{HI} = 1.5 \times 10^{-5} \left( \dfrac{C}{3} \right) \left( \dfrac{r}{kpc} \right)^2 \left( \dfrac{\dot{N}_{\rm ion}}{10^50 s^{-1}} \right)^{-1} \left( \dfrac{1+z}{8} \right)^3 $$

- $$C$$ is the clumping factor,
- $$\dfrac{\dot{N}_{\rm ion}$$ is the rate of ionizing photons produced. Yajima+ does not multiply this by the escape fraction, but I think it should be (though I believe this term is so subdominant, I doubt it will matter)
- $$r$$ is the (proper) distance from the galaxy.

Calculation for scattering cross-section (from Verhamme+2006):

$$\sigma_{Ly\alpha} [\lambda]= 1.041\times 10^{-13} \left( \dfrac{T}{10^4 {\rm K} }\right)^{-1/2} \dfrac{H(x,a)}{\sqrt(\pi)} $$

- Yajima+ sets $$T=10^4$$ K, where Cenn+ uses a different temperature outside the bubble. I will just keep it constant as well.
- $$\dfrac{H(x,a)$$ is the Voigt function (eq 8 in Yajima+). This is a function of the wavelength.


## 
