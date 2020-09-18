---
layout: post
title:  "FSPS Free Parameters"
date:   2020-09-18
categories: mocks
---


In the <a href="https://ndrakos.github.io/blog/mocks/FSPS_UV_Properties/">last post</a>, I outlined some potential free parameters in generating spectra, and detailed how to calculate the resulting UV properties.

In this post, I will vary the free parameters to get a sense of how they affect the UV properties.



## Baseline

As in the previous post , I will consider a galaxy of mass $$10^8 M_\odot$$ at redshift zero. The age of the universe should be about 13.8 Gyr, which sets <code>tage</code>=13.8

For the potential free parameters, I assign them baseline values of <code>logzsol</code>=0, <code>sf_start</code>=10, <code>tau</code> = 1, <code>dust2</code>=0, <code>gas_logz</code>=-2.


## Results

<img src="{{ site.baseurl }}/assets/plots/20200918_SED_freeparams.png">

The results don't seem to be sensitive to <code>gas_logu</code> (the gas ionization parameter), so I think I'll just set this to -2.

I am surprised about how insensitive the results are to <code>tau</code>, which is the efolding time for star formation. Here, we have varied it from 0.1 to 100 Gyr, which is the range allowed in FSPS. These timescales are fairly long, so that is probably why... My default parameters have star formation beginning at 10 Gyr, leaving the total time for star formation to be less than 4 Gyr.
