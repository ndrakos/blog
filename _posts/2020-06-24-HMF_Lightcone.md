---
layout: post
title:  "HMF Lightcone"
date:   2020-06-22

categories: mocks
---

I want to check that the HMF recovered from the lightcone looks right.


## HMF from Snapshots

If I calculate the HMF from individual snapshots, and compare to theory, I get the following:

<img src="{{ site.baseurl }}/assets/plots/20200624_HMF.png">



## HMF from Lightcone

Now I want to calculate for redshift slices in my light cone.

One correction I have to make is for the volume. The survey volume is a pyramid with an angle $$\theta$$.
At redshift, $$z_i$$ (with corresponding comoving distance, $d_i$), the sides of the pyrimid are $$d_i \sin(\theta)$$, and therefore the volume is $$d_i^3 \sin(\theta)^2/3$$. Therefore redshift slices between $$z_i$$ and $$z_{i+1}$ have volumes $$\sin(\theta)^2 (d_{i+1}^3 - d_i^3)/3$$.

Here is the recovered HMFs (where I have taken the theory curve to be at the center of the redshift range):


<img src="{{ site.baseurl }}/assets/plots/20200624_HMF_lightcone.png">

They don't agree completely, which is probably partially due to the redshift ranges... here is another visualization:

<img src="{{ site.baseurl }}/assets/plots/20200624_HMF_lightcone_2.png">
