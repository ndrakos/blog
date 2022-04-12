---
layout: post
title:  "The Escape Fraction"
date:   2022-04-12
categories: reion
---

The LyC escape fraction, $$f_{\rm esc}$$, is one of the main quantities we need to calculate for the simulated galaxies (see <a href="https://ndrakos.github.io/blog/reion/Reionization_Modelling/">this post</a>).This quantity is the fraction of photons that escape galaxies to ionize intergalactic hydrogen, and is therefore a dimensionless number between 0 and 1.

## Current constraints

$$f_{\rm esc}$$ is the least constrained out of the three parameters needed to calculate $$\dot{n_{\rm ion}}$$. It is especially difficult to measure at the epoch of reionization, since neutral hydrogen absorbs LyC photons; in reality, it can't be measured **directly** except at low redshifts

Here is some information pulled from a couple papers:
- Negligible $$f_{\rm esc}$$ measured in deep stacks at z~0–1 (e.g., Siana et al. 2010; Rutkowski et al. 2016)
- Less than 5 per cent in the local Universe (Grimes et al. 2009; Vanzella et al. 2010; Leitherer et al. 2016; Naidu et al. 2018)
- $$f_{\rm esc}$$~10% at z~2.5–4 (Marchi et al. 2017; Steidel et al. 2018; Fletcher et al. 2019; P. A. Oesch et al. 2020).
- During EoR  $$f_{\rm esc}$$ must be >15–20 per cent for star-forming galaxies to reionize the universe (Ouchi et al. 2009b; Robertson et al. 2013, 2015; Finkelstein et al. 2019; Naidu et al. 2020).



## Models


### Constant escape fraction

It is common to assume the $$f_{\rm esc}$$ is a constant number in reionization studies (e.g., Robertson2015,  Ishigaki2018). This can be interperated as an average escape fraction.

### fesc depends on SFR surface density

I will largely follow <a href="https://ui.adsabs.harvard.edu/abs/2020ApJ...892..109N/abstract">Naidu et. al 2020</a>. They assume escape fraction solely depends on the SFR surface density:

$$f_{\rm esc} = a \times \left( \dfrac{ \Sigma_{\rm SFR} } {1000 M_\odot {\rm yr}^{-1} {\rm kpc}^{-2} } \right)^b$$

with $$a=1.6 \pm 0.3$$ and $$b=0.4 \pm 0.1$$



## Calculation


$$\Sigma_{\rm SFR} = \dfrac{SFR}{2 \pi R_{\rm gal}^2}$$

where $$R_{\rm gal}$$ is the effective radii of the galaxy (e.g. Shibuya2019). I calculate this from the galaxy catalog as $$R_{\rm gal} = \sqrt{q} R_{\rm eff}$$

Then I use the best fit parameters from Naidu2020 ($$a=1.6$$ and $$b=0.4$$), and constrain the values so that they fall between 0 and 1.


## Results

Here is what I get (using the test catalog, that only contains more massive galaxies)

<img src="{{ site.baseurl }}/assets/plots/20220412_f_esc.png">

This roughly agrees with the values above. I need to check what range of galaxy masses/luminosities they used in their measurements to make a fair comparison. For now, this seems pretty good though!



## Questions/Thoughts/Next steps

1. This obviously depends a lot on the galaxy effective sizes. There was some concern that my catalog has a (small number) of galaxies that have unrealistically small sizes for their brightness. This is something I want to look into a bit more, by plotting the SFR surface density. I might also do some comparisons to Shibuya et al. 2019.

2. Now I have all the ingredients to calculate the ionization contribution of the galaxies (modulo some debugging on the $$xi_{\rm ion}$$ values). I will go ahead soon and get the calculation for $$\dot{n_{\rm ion}}$$.

3. My end goal is to compare different galaxy surveys abilities to constrain reionization. I need to think about if I want to alter these models (either by considering alternate models, or by altering the values by e..g 10 percent and seeing how it affects things).
