---
layout: post
title:  "Galaxy Clustering Lightcone"
date:   2020-09-14
categories: mocks
---

In a <a href="https://ndrakos.github.io/blog/mocks/Galaxy_Clustering/">previous post</a> I outlined how to calculate the two-point correlation function (2PCF) on a simulation volume (note there were some errors in that post). Here I am going to go through calculating the 2PCF on the light cone.


## Generating a Random Distribution

The survey is a pyramid of height $$d_{\rm max}$$ and length/width of $$d_{\rm max} \sin \theta$$, where $$\theta$$ is the survey volume (see <a href="https://ndrakos.github.io/blog/mocks/HMF_Lightcone/">this post</a>).

I generated uniformly distributed points in this volume by

(1) picking a comoving distance $$d = d_{\rm max} {\rm rand}^{1/3}$$, where $${\rm rand}$$ is a random number between 0 and 1.

(2) picking $$y$$ and $$z$$ coordinates as $$y_rand = d \sin(\theta) ({\rm rand}-0.5)$$

(3) Convert these to RA, DEC and distance as in <a href="https://ndrakos.github.io/blog/mocks/Halo_Lightcone_Catalogue/">this post</a>

Is this correct? Should they be uniformly distributed in comoving coordinates?

## Results

I am using the package Corrfunc. Corrfunc has instructions on how to calculate the projected correlation function for mock catalogs  <a href="https://corrfunc.readthedocs.io/en/master/modules/converting_rp_pi_mocks.html">here</a>.

I took all the galaxies in different redshift bins and plotted the correlation functions.

Here are the results:


<img src="{{ site.baseurl }}/assets/plots/20200914_Clustering.png">


I should double check all the input parameters, and also figure out how to put error bars on these. I also want to check the lowredshift results against SDSS measurements.
