---
layout: post
title:  "Light Cone 512 Sims"
date:   2020-05-08

categories: mocks
---


In <a href="https://ndrakos.github.io/blog/mocks/Light_Cone_Tests/">this post</a>, I summarized the current method I have for generating light cones. However, my code was much to slow to run on the 500 snapshots I have for the $$512^3$$ simulation. Therefore, I have sped up the code significantly by (1) switching to using pandas data frames in python and (2) pre-calculating which snapshots have redshifts that overlap with the possible redshifts of the tiled simulation block, and only analyzing those.


# Results

Here are the results with 20 tiled boxes ($$z<1$$).

The positions of the halos in x-y-z space (downsampled to $$10^5$$ halos)

<img src="{{ site.baseurl }}/assets/plots/20200508_Lightcone_xyz.png">

The halo mass functions:


<img src="{{ site.baseurl }}/assets/plots/20200508_wfirst_HaloMassFunction.png">



# Next Steps

1) Finalize the abundance matching code, using these $$512^3$$ simulations, and populate the lightcone with galaxies.

- write a bit of code to read in IDs of subhalos on the lightcone, and include this in the SHAM procedure
- make sure the scatter model is working properly
- get stellar mass functions that evolve with redshift (right now I just have it for redshift zero)

2) Go through some of the potential problems in my light cone method, as outlined in the previous post
