---
layout: post
title:  "A Closer Look At Beta"
date:   2020-12-11
categories: mocks
---

In this post I take a closer look at the spectra to double check my  $$\beta$$ calculation is correct.


## Sample

I am using the catalog and $$\beta$$ calculation from <a href="https://ndrakos.github.io/blog/mocks/SED_Method_Updates/">here</a>.

I am taking all galaxies with redshifts $$z<0.05$$. There are 16 galaxies in this redshift range for this catalog.

## Results

Here are where the 16 galaxies lie in mass--$$M_{UV}$$--$$\beta$$ space

<img src="{{ site.baseurl }}/assets/plots/20201211_MUV_testpoints.png">

Here are the spectra, $$f_{\lambda}$$ (not normalized properly, but that doesn't matter for the slope).

<img src="{{ site.baseurl }}/assets/plots/20201211_MUV_testpoints_spectra.png">


## Conclusions

I can't see any issues here... the $$\beta$$ values look like they agree with the spectra.

One thing I should be careful of is the effect of mass completeness. There are no galaxies below masses of $$\sim 10^8$$ in this catalog. That means I am missing the fainter objects, which should have steeper slopes (lower $$\beta$$ values).
