---
layout: post
title:  "Dust Properties"
date:   2021-02-03
categories: mocks
---



1. E(B-V)... balmer decrement
2. look into reddy 2018...https://ui.adsabs.harvard.edu/abs/2018ApJ...853...56R/abstract
3. don't include dust , see if big influence on beta-MUV





One think I want to double check is whether the dust properties I have assigned to the mock galaxies are reasonable; this is especially important as this should influence the UV slope, $$\beta$$ (along with age and metallicity).

Specifically, I am assigning the $$V$$ band optical depth, $$\tau_{V}$$

## Method


I am using the method outlined <a href="https://ndrakos.github.io/blog/mocks/SED_Methods_Part_II/">here</a> to assign the dust opacity, which is the same method used in W18.

This is a semi-analytic model that depends on metallicity, star formation rate and galaxy size.

Updates? see sec 3.4.3 in W18... note that I am not truncating it at 4 anymore...


I have checked the SFR, metallicities and galaxy sizes in previous posts to ensure that they all looked reasonable. One thing I haven't looked at yet is whether the dust properties make sense.


## Results

I couldn't find any data on what the V band opacity trends should be, but there are plenty of constraints that involve the dust mass of galaxies.

To get the dust mass.. fsps provides with <code>dust_mass</code>. This isn't documented, but it seems to compute for a grid of ages from t=0 to maximum age of the isochrone; therefore I think I want to take the last item.





https://www.aanda.org/articles/aa/pdf/2016/03/aa27746-15.pdf


figs 10-13
https://ui.adsabs.harvard.edu/abs/2017A%26A...606A..17M/abstract


https://ui.adsabs.harvard.edu/abs/2018MNRAS.478.4905A/abstract

look into Naveen Reddy's papers for comparison to observations
https://arxiv.org/pdf/2005.01742.pdf
