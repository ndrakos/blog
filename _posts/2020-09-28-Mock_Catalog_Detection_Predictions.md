---
layout: post
title:  "Mock Catalog Detection Predictions"
date:   2020-09-28
categories: mocks
---

The galaxies now have SEDs, and we have a method for determing if they are detected. Though there are a number of issues to sort out, we can make some preliminary predictions with this.

In general, I will calculate the desired quantities using only the detected galaxies, but then correct for the expected completeness. This will allow us to get a more accurate idea of the uncertainties on the measurements.


## Fraction of Detected Galaxies

If we plot the fraction of galaxies in the catalog that are detected, we get the following:

<img src="{{ site.baseurl }}/assets/plots/20200928_frac_detect.png">

While the redshift and mass trends make sense, the fraction of galaxies detected is higher than I had expected. I wonder if the galaxies are too bright... The UV magnitudes did seem brighter than expected, though this was mostly at low redshifts.


## Number of Detected Galaxies

With this, the number of galaxies we expect to predict is:

<img src="{{ site.baseurl }}/assets/plots/20200928_Ndetect.png">

And if we break that into star-forming and quiescent galaxies :

<img src="{{ site.baseurl }}/assets/plots/20200928_NdetectSF.png">


## Stellar Mass Function

We can also recover the stellar mass function.

I used only the detected galaxies, but then rescaled the SMF by $$1/x$$, where $$x$$ is the fraction of galaxies detected in that mass/redshift bin.

<img src="{{ site.baseurl }}/assets/plots/20200928_SMF.png">


## Luminosity Function


The predicted luminosity function is:

<img src="{{ site.baseurl }}/assets/plots/20200928_LF.png">

This doesn't look quite right... though the turn over could be because I am not resolving enough faint low-mass galaxies (right now the results are for the $$512^3$$ simulation)---see for example Fig 17. from W18

<img src="{{ site.baseurl }}/assets/plots/20200928_LF_W18.png">


I also plotted $$dN/dM_{\rm UV} to compare from the JADES predictions (Fig, 25 in W18).

<img src="{{ site.baseurl }}/assets/plots/20200928_dNdMUV.png">

<img src="{{ site.baseurl }}/assets/plots/20200928_dNdMUV_W18.png">
