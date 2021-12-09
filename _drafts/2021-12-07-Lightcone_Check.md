---
layout: post
title:  "Lightcone Check"
date:   2021-11-30
categories: mocks
---

When Mark was looking at grism predictions for DREaM, he made the following plot:

<img src="{{ site.baseurl }}/assets/plots/20211130_check.png">

This shows that there are some discretizations in the galaxy redshifts that look artificial.

I plotted the spacing of the boxes used to construct the lightcone, and the individual snapshot redshifts. The artificial clustering seems to at the redshifts of the snapshots. I am looking into this further to see if there is a bug in my lightcone code.

<img src="{{ site.baseurl }}/assets/plots/20211130_check2.png">

## Reproducing the problem

After much fiddling, I was able to get a scatter plot that demonstrates this issue. The plot below shows the lowest mass galaxies, in the tiled boxes 20-25 (out of 60 total boxes).

<img src="{{ site.baseurl }}/assets/plots/20211130_Check_discretization.png">


## The potential source of the issue?

When creating the lightcone, I interpolate the position of the halos using merger trees, and then determine if/where they cross the observer's lightcone. In cases where the halo is not found in the subsequent snapshot, I extrapolate the position using $$r_{j+1} = r_{j} + dt*v_{j}$$.

Looking through my code, I was using co-moving positions, $$r$$, but physical velocities, $$v$$. Therefore, I need to use $$r_{j+1} = r_{j} + dt*v_{j}/a_{j}$$. This means that the velocities used in the extrapolations were too small, and this could create extra clustering around snapshots. This would be most noticeable in lower mass halos, which are less likely to have a descendant in the subsequent snapshot.

## Rerunning the lightcone

I got this running on lux. This required changing the structure of the parallelization of the code, and breaking it into chunks so that it could run on fewer nodes, over shorter periods of time.

Here are boxes 20 and 21:

<img src="{{ site.baseurl }}/assets/plots/20211130_Check_discretization_2.png">

There is still some clustering in the redshift, but it is no longer AS lined up with the redshifts of the snapshots... could be real clustering?
