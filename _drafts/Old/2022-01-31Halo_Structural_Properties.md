---
layout: post
title:  "Halo Structural Properties"
date:   2022-01-31
categories: iso_ics
---


Here is a summary of my halo property measurements for comparison with Justin's results. (See <a>previous post</a>)

## Defining halo particles and frames...

I will consider 3 sets of particles..

(1) Halo A
(2) Halo B
(3) All particles

In all the cases, I will find the center of the halo...


## Halo structural properties


### Characteristic radii

Will consider... r2, rvir, rpeak

r2...

Virial radius not well defined in simulations...

rpeak is the radius at...

r_peak,v_peak = halos.find_r_peak(myr, G,  m,  minr, maxr, numbins)



PLOT


### Shape properties

Have the following code to get axis ratios:


a,b,c,d = halos.principle_axis_ratios_iterative(data,m)


PLOT


### Concentrations

Will consider two definitions

(1) rvir/r2

(2) vpeak/vvir


PLOT
