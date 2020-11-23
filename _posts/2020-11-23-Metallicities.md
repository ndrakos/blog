---
layout: post
title:  "Metallicties"
date:   2020-11-23
categories: mocks
---

<!---
Mannucci2010 https://ui.adsabs.harvard.edu/abs/2010MNRAS.408.2115M/abstract
Hunt2016a https://ui.adsabs.harvard.edu/abs/2016MNRAS.463.2002H/abstract
Hunt2016b https://ui.adsabs.harvard.edu/abs/2016MNRAS.463.2020H/abstract

-->

Here I am checking to see whether the metallicities assigned to the mock galaxies make sense.

### Metallicity Model

The metallicities were assigned from the fundamental metallicity relation from W18 (eq 15):

$$12 + \log_{10}(O/H)
\approx \log_10(Z_{\rm ISM}/Z_{\odot}) + 8.7
= -0.14 \log10(\psi/M_{\dot} {\rm yr}^{-1}) + 0.37 \log10(M/M_\odot) + 4.82

The stellar masses in the mock catalog are assigned from abundance matching, and the SFRs are assigned from <a href="https://ui.adsabs.harvard.edu/abs/2017A%26A...602A..96S/abstract">Shreiber et al. 2017</a>.


## Results

Here is the metallicity-mass relation for all the star-forming galaxies in the mock catalog (I found very little difference when I did a redshift cut):

<img src="{{ site.baseurl }}/assets/plots/20201123_MassMet.png">


For comparison, here are results from <a href="https://ui.adsabs.harvard.edu/abs/2010MNRAS.408.2115M/abstract">Mannucci et al. 2010</a>:

<img src="{{ site.baseurl }}/assets/plots/20201123_MannucciFig1.png">


And from W18:

<img src="{{ site.baseurl }}/assets/plots/20201123_W18Fig20.png">


My metallicities seem a bit


## A Closer Look at SFRs

I also took a closer look at the SFRs. Here is the (equations 10 and 12 for star-forming (SF) and quiescent (Q) galaxies, respectively):

<img src="{{ site.baseurl }}/assets/plots/20201123_SFR_vs_M.png">


For comparison, consider the following plots for the cosmic star formation rate density and the sSFR:

<img src="{{ site.baseurl }}/assets/plots/20201123_SFR_vs_z.png">

and from Williams:

<img src="{{ site.baseurl }}/assets/plots/20201123_W18Fig1819.png">

These agree pretty well (though I think I must have a unit problem in the top plot... I will look into this)
