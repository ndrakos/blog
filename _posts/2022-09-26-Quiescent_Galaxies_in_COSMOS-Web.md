---
layout: post
title:  "Quiescent Galaxies in COSMOS-Web"
date:   2022-09-26
categories: cosmos_web
---


In this post, I'm going to look at how many quiescent galaxies COSMOS-Web will be able to detect (as predicted from the DREaM catalogs). I will consider a galaxy detectable if it is brighter than 28 mag in at least one of the COSMOS-Web NIRCAM filters.


## Completeness and Number Counts

Here are the stellar mass functions of *detectable* quiescent galaxies, with the underlying model (from Williams et al. 2018) shown with dotted lines. Note that the DREaM catalog extends down to $$10^5$$ solar masses, and that COSMOS-Web will be complete above $$10^9$$ or so.

<img src="{{ site.baseurl }}/assets/plots/20220926_QG_LF.png">

Here are the number counts:

| Redshift    | Number of Quiescent Galaxies (above mass $$5\times 10^9$$) | Detectable Quiescent Galaxies  (above mass $$5\times 10^9$$)|
| ----------- | ----------- |----------- |
| 1  | 287195 (5350)|   16678 (5350)|
| 2  | 3844   (3164)|   3791  (3164)|
| 3  | 1070    (881)|   1060   (881)|
| 4  | 482     (398)|   472    (398)|
| 5  | 114      (91)|   111     (91)|
| 6  | 49       (38)|   49      (38)|
| 7  | 11       (10)|   10      (10)|
| 8  | 5         (5)|   5        (5)|
| 9  | 1         (1)|   1        (1)|
| 10 | 1         (1)|   1        (1)|

There are a couple of things I didn't expect here! The first is that at a depth of 28 mag, all of the quiecent galaxies above $$5\times 10^9$$ solar masses will be detected. The other thing I didn't expect is that since all the quiescent galaxies are expected to be very massive at high redshift galaxies, we could detect **all** the quiescent galaxies in the field at high redshift. Note that quiescent galaxies very well might not actually exist at redshifts ~10. However, it seems likely that COSMOS-Web will contain the highest-redshift quiescent galaxy detected.



## Number Densities

Here is the number density as a function of redshift (similar to Fig. 7 in Merlin et. al 2019). Error bars are just the Poisson noise.

<img src="{{ site.baseurl }}/assets/plots/20220926_QGs.png">

The dashed lines show 1/V(>z) (truncating at a redshift of 12) for different survey volumes. 100 arcmin^2  should be similar to CEERS, and 300 arcmin^2 should be similar to JADES.


If I overlay this on top of the Merlin plot I find the following:

<img src="{{ site.baseurl }}/assets/plots/20220926_QGscompare.png">


The DREaM catalog contains a higher number density of high-redshift quiescent galaxies than other simulated data sets, but it is still consistent with observations.
