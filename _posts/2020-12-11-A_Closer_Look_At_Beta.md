---
layout: post
title:  "A Closer Look At Beta"
date:   2020-12-11
categories: mocks
---

In this post I take a closer look at the spectra to double check my  $$\beta$$ calculation is correct.


## Sample

I am using the catalog from <a href=https://ndrakos.github.io/blog/mocks/SED_Methods_Part_II/>here</a>and $$\beta$$ calculation from <a href="https://ndrakos.github.io/blog/mocks/SED_Method_Updates/">here</a>.

I am taking all galaxies with redshifts $$z<0.06$$. There are 25 galaxies in this redshift range for this catalog.

## Results

Here are where the 16 galaxies lie in mass--$$M_{UV}$$--$$\beta$$ space

<img src="{{ site.baseurl }}/assets/plots/20201211_MUV_testpoints.png">

Here are the spectra, $$f_{\lambda}$$ (not normalized properly, but that doesn't matter for the slope).

<img src="{{ site.baseurl }}/assets/plots/20201211_MUV_testpoints_spectra.png">


## Conclusions

I can't see any issues with the $$\beta$$ assignment... the values look like they agree with the spectra.

I am going to look closer at the very bright orange point, as it seems unrealistic. Maybe the SFR is not assigned correctly? Or the scatter was too far off the relation, and I need to change the scatter relation?

One thing I should be careful of is the effect of mass completeness. There are no galaxies below masses of $$\sim 10^8$$ in this catalog. That means I am missing the fainter objects, which should have steeper slopes (lower $$\beta$$ values).
