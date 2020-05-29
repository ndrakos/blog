---
layout: post
title:  "Stellar Mass Functions"
date:   2020-05-21

categories: mocks
---


For my mock catalogs, I plan to use the stellar mass functions (SMFs) from <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>.


## Procedure From Williams et al. 2018

They use continuously evolving Schechter functions for both star-forming and quiescent galaxies, presumably out to redshift $$\sim 15$$, though there really aren't any observational constraints at redshifts that high.

### Star-Forming Galaxies

Their double-schechter parameters for the star-forming SMF is given in their Table 1.

The SMF measurements for $$0 \le z \le 4$$ are taken from the data presented <a href="https://ui.adsabs.harvard.edu/abs/2014ApJ...783...85T"> Tomczak et al. 2014</a>. At higher redshifts, the SMF is no longer well constrained, and is instead inferred from UV luminosity functions. Williams et al. use measurements from from <a href="https://ui.adsabs.harvard.edu/abs/2015ApJ...803...34B/abstract">Bouwens et al. 2015 </a> for $$4 \leq z \leq 8$$ and  <a href="https://ui.adsabs.harvard.edu/abs/2018ApJ...855..105O/abstract">Oesch et al. 2018 </a> for $$z=10$$. Beyond redshift 10, the SMFs are an extrapolation.

One caveat to this SMF is that they are not modelling the dusty star-forming galaxies currently missed in the UV-selected samples, and therefore underrepresent the high-mass end of the $$2<z<3$$ mass functions If these objects exist, they should be revealed by *JWST*, and this will help constrain their number density evolution.



### Quiescent Galaxies

Their double-schechter parameters for the quiescent SMF is given in their Table 3.

The SMFs for the quiescent galaxies are also based off the Tomczak data, and extrapolated to higher redshifts, though the extrapolation is in agreement with the few constraints for quiescent galaxies at $$z>3.5$$.


## Plots

Here are the SMFs for the star-forming galaxies (top) and quiescent galaxies (bottom)

<img src="{{ site.baseurl }}/assets/plots/20200521_SMF_Williams.png">


## Future Things to Check

I want to check that there aren't any significant updates to observations that will greatly effect the SMFs. Here I've compiled a list of some possibly relevant recent papers.

1) Recent work by <a href="https://ui.adsabs.harvard.edu/abs/2020ApJ...893..111L/abstract">Leja et al. 2020</a> suggests that SMFs may be underestimated. However, they only look at redshifts $$0.2<z<3$$, so Williams results are still more useful for us. However, it would be nice to compare their SMFs (and references therein; cf their Fig 11.), and see how much it affects the mock catalog results in the relevant redshift range.

2) There are also more recent number density measurements of quiescent galaxies <a href="https://ui.adsabs.harvard.edu/abs/2019A%26A...631A.157D/abstract">Díaz-García et al. 2019</a> out to redshift $$z=1$$.

3) Another thing to check is whether we can recover the correct stellar-to-halo mass relation after abundance matching. The newest constraints for these are from <a href="https://ui.adsabs.harvard.edu/abs/2020A%26A...634A.135G/abstract">Girelli et al. 2020</a>, which goes out to redshift $$z=4$$.
