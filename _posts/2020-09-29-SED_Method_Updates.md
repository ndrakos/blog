---
layout: post
title:  "SED Method Updates"
date:   2020-09-28
categories: mocks
---

In <a href="https://ndrakos.github.io/blog/mocks/SED_Methods/">this post</a>, I outlined my methods for calculating SEDs for the galaxies in the mock catalog.

There were two main problems (1) the $$M_{\rm UV}$$--$$\beta$$ relationship was backwards and (2) there were some fairly blue quiescent galaxies in the UVJ diagram.

I am fixing of things in my previous implementation to try and address these issues.


## UV Continuum slope

Before I was using the redshift 0 SED to calculate $$\beta$$.

I am now using equation (1) from
<a href="https://ui.adsabs.harvard.edu/abs/2012MNRAS.420..901D/abstract">Dunlop et al 2012</a> to calculate the UV continuum slope:

$$\beta = 4.43(J125-H160)-2$$

with the SEDs calculated for redshift 7 (with FSPS filters wfc3_ir_f125w and wfc3_ir_f160w).

### Results

Here are the UV properties:

<img src="{{ site.baseurl }}/assets/plots/20200929_MUV.png">


This is slightly improved, but the trend is still backwards. Next I will make 2D histograms to figure out why the faint galaxies have such a small slope.




## UVJ Diagram

Before I was assigning galaxy ages from a gaussian, without any consideration to whether they were SF or not. I have updated my method of assigning ages. I also fixed it so that I am getting the rest-frame U, V and J magnitudes to check the SF/Q classifications x

As before, I will assign ages based on a weak gaussian in $$\log_10{a/{\rm yr}}$$ with a standard deviation of 0.7. The gaussian will be truncated between 6 and $$\log_10{t_{\rm age}/{\rm yr}-10^6}$$ for both SF and Q galaxies

For SF galaxies, as before, the Gaussian is centered at 9.3.

Since Quiescent galaxies should be older, I will center the ages for this on 13.3 Gyr; this difference of 4 Gyr was motivated by <a href="https://ui.adsabs.harvard.edu/abs/2015Natur.521..192P/abstract">this paper</a>.

I'm not entirely happy with this method, but it is an improvement from my previous method of assigning ages. I couldn't find any better models for what the age distributions of galaxies should look like (as a function of redshift and possibly mass).

### Results


Here is the UVJ diagram, with objects below redshift 0.5. I also added the  <a href="https://ui.adsabs.harvard.edu/abs/2009ApJ...691.1879W/abstract">Williams et al. 2009</a> selection box.


<img src="{{ site.baseurl }}/assets/plots/20200929_UVJ.png">


This looks much better with the different age distribution, but once I put on the selection box, you can see there is still a discrepancy. I want to use a better motivated age distribution. Maybe I can constrain the SF galaxy ages using the UV properties, and then use the same (shifted) distribution for the quiescent galaxies.
