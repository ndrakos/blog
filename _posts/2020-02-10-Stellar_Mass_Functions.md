---
layout: post
title:  "Stellar Mass Functions"
date:   2020-02-10
categories: mocks
---


Abundance matching requires a stellar mass function (SMF) or luminosity function. For now, I am using the parameterization from <a href="https://ui.adsabs.harvard.edu/abs/2009MNRAS.398.2177L">Li & White 2009</a> which is a parameterization for the SMF made of three piece-wise Schechter functions to describe SDSS data at low redshift, shown in the figure below.

<img src="{{ site.baseurl }}/assets/plots/SMF_Li2009.png">


Eventually, this will need to be extended to larger redshifts. For example, in <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>, they use continuously evolving Schechter functions for both star-forming and quiescent galaxies for galaxies between redshifts $$0 \le z \le 10$$. Constraints from $$0 \le z \le 4$$ are from <a href="https://ui.adsabs.harvard.edu/abs/2014ApJ...783...85T"> Tomczak et al. 2014</a>. At higher redshifts, the SMF is no longer well constrained, and is instead inferred from UV luminosity functions.


## Things to sort out:

(1) Method for extending this to high redshifts ($$z=10$$) using UV luminosity functions

(2) How to include uncertainty in the SMF parameterization in abundance matching algorithm

(3) Are there any updated parameterizations since those given in <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>?
