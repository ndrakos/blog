---
layout: post
title:  "Neutrino Velocity Assignment Test"
date:   2022-03-10
categories: neutrinos
---

In this post, I am testing I have the algorithm working for assigning neutrino particles velocities (see <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_IC_Method_Overview/">this post</a>).



## Python code

Here is my python code:

<object width="500" height="300" type="text/plain" data="{{site.baseurl}}/assets/files/assign_velocity.txt" border="0" >
</object>


## Test velocity magnitudes

This shows the division of the Fermi-Dirac distribution ($$f(p)$$) into equal-mass shells. The solid vertical lines show the edges of the shells, and the dotted lines are the momentum value (in dimensionless units $$pc/kT$$) for each shell.

<img src="{{ site.baseurl }}/assets/plots/20220310_velocityshells.png">


## Test directions

Here are the directions for each $$12N_{\rm side}^2$$ particles for each momentum. The plot shows the x,y,z components on a unit sphere.

<img src="{{ site.baseurl }}/assets/plots/20220310_velocitydirections.png">


## Conclusions

This all looks good! There are then $$N_{\rm shell} \times 12N_{\rm side}^2$$ neutrino particles for every grid point. For now I tested the code Python, but I'm going to convert it to C, since that is what MUSIC is written in. We will have to decide if we are using healpix to divide the unit sphere into equal area elements, or if we don't want to include that dependance in the code.
