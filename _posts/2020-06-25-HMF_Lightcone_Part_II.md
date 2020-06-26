---
layout: post
title:  "HMF Lightcone Part II"
date:   2020-06-25

categories: mocks
---

In my <a href="https://ndrakos.github.io/blog/mocks/HMF_Lightcone/">last post</a>, I wanted to check if the HMF recovered from my lightcone looked right. In the last post, I didn't properly account for the redshift range in the theoretical curve (since the halos are binned in redshift). In this post I fix that, and also think a bit more about whether the recovered HMF is okay.


## Fixed Theoretical Prediction

To get the HMF between redshifts $$z_{i}$$ and $$z_{i+1}$$, I calculated

$${\rm HMF}(M,z_i<z<z_{i+1}) = \dfrac{\int_{z_i}^{z_{i+1}} {\rm HMF}(M,z'){\rm d}z'}{z_{i+1}-z_i}$$

Which gives the following:

<img src="{{ site.baseurl }}/assets/plots/20200625_HMF_lightcone.png">



## Low Mass Issues

I seem to be missing some of the low mass halos at all redshifts.

In <a href="https://ndrakos.github.io/blog/mocks/Light_Cone_Tests/">this post</a> I had listed some assumptions/possible problems with the implementation I had the time.

One thing that I still haven't looked into is how to count halos that don't have a progenitor; since I am interpolating positions between snapshots $$j$$ and $$j+1$$ to find when a halo crosses the backwards light cone, if a halo in $$j+1$$ doesn't have a progenitor in snapshot $$j$$, it can't cross the light cone, and won't be in the survey. I am guessing this will mostly affect low mass halos.

I accounted for these halos by extrapolating for their positions at redshift $$j$$, and here is my recovered HMF:

<img src="{{ site.baseurl }}/assets/plots/20200625_HMF_lightcone_2.png">

which looks great!

## Other Potential Problem: Periodic Boundary Conditions


One thing I realized while adding in the extrapolation, is that I am not accounting for the periodic boundary conditions. Given a halo was at position $$r_j$$ in snapshot $$j$$ and position $$r_{j+1}$$ in snapshot $$j+1$$, I am assuming it travelled between these two positions, and not allowing for it to have arrived in the new position by travelling through the simulation box. This might not be too much of a problem, since I have so many snapshots, so halos probably rarely pass through the box

I will fix this by:

$$r_{j} \rightarrow r_{j} + {\rm boxsize}\dfrac{({\rm sign}(v_{j}) - {\rm sign}(x_j -x_{j+1}))}{2}$$

This will ensure that, e.g. if there is a positive $$x$$ velocity, the $$x$$ position will increase. The positions of the progenitor halos are now potentially outside the simulation box.

Then, once I have found where the halo has crossed the lightcone, $$r_e$$, I can make sure the periodic boundary conditions are implemented by:

$$r_e \rightarrow r_e \% {\rm boxsize}$$
