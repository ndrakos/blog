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

In this post I am checking to see whether the mock galaxy metallicities agree with observations.

### Metallicity Model

The metallicities were assigned from the fundamental metallicity relation from W18 (eq 15):

$$  \log_{10}(Z_{\rm ISM}/Z_\odot)  + 8.7 \approx 12 + \log_{10}({\rm O}/{\rm H}) = -0.14 \log10( \psi /M_{\odot} {\rm yr}^{-1} ) + 0.37 \log10(M/M_\odot) + 4.82$$

This depends on galaxy stellar masses and SFRs; the stellar masses were assigned from abundance matching, and the SFRs were assigned from <a href="https://ui.adsabs.harvard.edu/abs/2017A%26A...602A..96S/abstract">Shreiber et al. 2017</a>.


## Results

Here is the metallicity-mass relation for all the star-forming galaxies in the mock catalog (I found very little difference when I did a redshift cut):

<img src="{{ site.baseurl }}/assets/plots/20201123_MassMet.png">


For comparison, here are results from <a href="https://ui.adsabs.harvard.edu/abs/2010MNRAS.408.2115M/abstract">Mannucci et al. 2010</a>:

<img src="{{ site.baseurl }}/assets/plots/20201123_MannucciFig1.png">


And from W18:

<img src="{{ site.baseurl }}/assets/plots/20201123_W18Fig20.png">


My metallicities seem a bit low... i.e. at masses of $$10^9$$ my median metallicities are ~8 versus ~8.5 in the Manncci et al 2010 plot. This could be because I'm including higher redshift galaxies; I did not find much a redshift dependance, but I have very little low redshift galaxies because of the narrow size of the survey. My results do agree well with the mock galaxies at higher redshifts in the W18 plot.


## Star Formation Rates

I also took a closer look at the SFRs (assigned from Shreiber et al. 2017 equations 10 and 12 for star-forming (SF) and quiescent (Q) galaxies, respectively):

<img src="{{ site.baseurl }}/assets/plots/20201123_SFR_vs_M.png">


For comparison, consider the following plots for the cosmic star formation rate density and the sSFR:

<img src="{{ site.baseurl }}/assets/plots/20201123_SFR_vs_z.png">

and from Williams:

<img src="{{ site.baseurl }}/assets/plots/20201123_W18Fig1819.png">

The sSFRs agree pretty well, but there are issues with star formation density. The first is probably a unit problem (it is off by ~7 orders of magnitude). The second issue might be more of a problem; star formation rate density does not decrease as it should with redshift. Therefore, it seems that there is too much star formation at high redshifts.
