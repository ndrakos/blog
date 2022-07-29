---
layout: post
title:  "Neutrino Implementation in C"
date:   2022-03-21
categories: neutrinos
---


This post contains code to  assign velocity to the particles in C. I did this in a <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_Velocity_Assignment_Test/">previous post</a> in python, but we need it in a form that will be incorporated into MUSIC, and eventually Cholla.

Note that I am embarrassingly rusty at C, and I am not sure how efficiently I coded this! It does give the same answer as the python code though.

## Code

<object width="500" height="300" type="text/plain" data="{{site.baseurl}}/assets/files/neutrino.txt" border="0" >
</object>

## A note on the velocity directions

To assign velocity directions, we need a way to divide the sphere into equal area elements. For the python code I used the package "healpy" which is the python version of Healpix to do this.

In the C version, I created a lookup table for $$N_{\rm side}=2,3,4,5,6$$ (note the number of directions at each grid point will be $$12 N_{\rm side}^2$$).

For Cholla, we need to decide between the following options:
1. Keep the lookup table approach. How large do we need $$N$$ to be?  In the Banjeree et. al paper they considered vales 1-4 for this variable.
2. Install a code like Healpix, and make it a required dependant package
3. Write our own code to divide up the unit sphere into equal area elements.
