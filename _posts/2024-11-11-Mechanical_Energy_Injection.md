---
layout: post
title:  "Mechanical Energy Injection"
date:   2024-11-11
categories: sne
---




In this post I'm summarizing my thoughts on how much mechanical energy would be needed to be injected into the ISM from SNe to increase the LyC escape fraction. 


## Mechanical Energy

References:
<a href=https://ui.adsabs.harvard.edu/abs/2024arXiv240912118F/abstract">Flury et. al 2004</a>

In the Flury+2024 paper, they calculate the mechanical energy as 

$$E_{\rm mech}(t) = \int_0^t L_{\rm wind}(t') + L_{\rm SNe}(t') dt'$$

where $$t$$ is the age of the stellar population,
and they use model mechanical luminosities $$L_{\rm mech}$$ (stellar and SNe mass loss rates scaled by wind terminal velocities vinf)
from the Starburst99 SED fits

We could possibly do domething similar, but it might be easier to just assume supernova inject an energy of $$\approx 10^{51}$$ ergs or something, and then just multiply the number of SNe. We might want to introduce some sort of "efficiency factor" here for how much SNe energy is converted into mechanical energy.

## Escape Fraction and Optical Depth

References:  <a href="https://arxiv.org/abs/2008.06059">Chisholm+2019</a>, <a href="https://ui.adsabs.harvard.edu/abs/2016A%26A...585A..48G/abstract">Grazian+2016</a>


The observed flux is related to the intrinsic flux as

$$f_{\rm obs} = f_0 e^{-\tau}$$,

where $$\tau$$ is the optical depth. If we ignore scattering (is this reasonable?),

$$f_{\rm esc} = e^{-\tau}$$

This means if we can relate mechanical energy to optical depth, we can connect it to escape fractions.

Note that ionizing radiation has two main sinks (1) neutral hydrogen gas and (2) dust. Sometimes escape fractions just include the first (the "relative" escape fraction), and this can be multiplied by the fraction unabsorbed by dust to get the absolute escape fraction.

We can also write $$\tau_{\rm eff} = \tau_{\rm gas} + \tau_{\rm dust}$$

## Optical Depth and Column density

Supernova can change the optical depth by
- Decreasing the column density NHI through ionization or changing the density/gemoetry (e.g. shockwaves, cavities). This will decrease the optical depth $$\tau_{\rm gas}$$
- Destroying dust grains. This will decrease the optical depth  $$\tau_{\rm dust}$$

Therefore, we can say

$$\Delta \tau_{\rm eff} = \Delta N_{\rm HI} \sigma_{\rm HI} + \Delta N_{\rm dust} \sigma_{\rm dust} $$

If we can find out how the energy from a supernova changes the HI and dust column densities, we can find the change in the optical depth, and therefore the change in the escape fraction.


## Conclusions?

Maybe what we want to do is find simulation papers and try and estimate how supernova explosions will decrease dust and HI column densities. I need to try and do some literature search, but here is a starting point on dust destruction: <a href="https://www.nature.com/articles/s41467-024-45962-0">Kirchschlager+2024</a>.

