---
layout: post
title:  "Stellar Mass Functions"
date:   2020-02-10
---


Abundance matching requires a stellar mass function (SMF) or luminosity function. For now, I am using the parameterization from <a href="https://ui.adsabs.harvard.edu/abs/2009MNRAS.398.2177L">Li & White 2009</a> which is parameterization for the SMF made of three piece-wise schechter functions to describe SDSS data at low redshift.

<img src="{{ site.baseurl }}/assets/plots/SMF_Li2009.png">

Eventually, this will need to be extended to larger redshifts. For example, in <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>


Things to sort out:

(1) How to extend this to high redshifts (z=10)?
(2) How to include uncertainty in SMF parameterization in abundance matching
(3) Are there any updated parameterizations since those given in Williams et al.?
