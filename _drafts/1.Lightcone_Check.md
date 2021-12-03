---
layout: post
title:  "Lightcone Check"
date:   2021-11-30
categories: mocks
---

When Mark was looking at grism predictions for DREaM, he made the following plot:

<img src="{{ site.baseurl }}/assets/plots/20211130_check.png">

This shows that there are some discretizations in the redshift location of the galaxies that look artificial.

I plotted the spacing of the boxes used to construct the lightcone, and the individual snapshot redshifts. The artificial clustering seems to be around the snapshots. I am looking into this further to see if there is a bug in my lightcone code.

<img src="{{ site.baseurl }}/assets/plots/20211130_check2.png">

## Reproducing the Problem

After much fiddling, I was able to get a scatter plot that demonstrates this issue. The plot below shows the lowest mass galaxies, in the tiled boxes 20-30.

<img src="{{ site.baseurl }}/assets/plots/20211130_Check_discretization.png">

There seems to be extra clustering around the redshifts corresponding to the discrete snapshots.

## The potential source of the issue?

When creating the lightcone, I interpolate the position of the halos using merger trees, and then determine if/where they cross the observer's lightcone. In cases where the halo is not found in the subsequent snapshot, I extrapolate the position using $$r_{j+1} = r_{j} + dt*v_{j}$$.

Looking through my code, I was using co-moving positions, $$r$$, but physical velocities, $$v$$. Therefore, I need to use $$r_{j+1} = r_{j} + dt*v_{j}/a_{j}$$. This means that the velocities used in the extrapolations were too small, and this could create extra clustering around snapshots. This would be most noticeable in lower mass halos, which are less likely to have a descendant in the subsequent snapshot.

## Running on Lux
