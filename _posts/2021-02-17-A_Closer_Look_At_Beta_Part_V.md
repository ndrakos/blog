---
layout: post
title:  "A Closer Look At Beta Part V"
date:   2021-02-17
categories: mocks
---

See this post for <a href=https://ndrakos.github.io/blog/mocks/A_Closer_Look_At_Beta/>Part I</a> and this post for <a href="https://ndrakos.github.io/blog/mocks/A_Closer_Look_At_Beta_Part_IV/">Part IV</a>.


Here I am looking closer at the z=4 galaxies. To do this, I am taking all the galaxies between 3.99 and 4.01. This results in 1260 galaxies (1254 that are star-forming and 6 that are quiescent) for the 512 simulation.


## FSPS parameters

Here is the distribution of FSPS parameters for these galaxies:

<img src="{{ site.baseurl }}/assets/plots/20210217_SED_params_z4.png">


## MUV-beta

I plotted these z=4 galaxies on the $$M_UV$$--$$\beta$$ plots, coloured by different galaxy properties to see how they fall in this parameter space. We expect that $$\beta$$ should depend on age, metallicity, dust, and SFR.

The dotted lines are the expected relations. We can see that the points do roughly follow the expected relation, but when we take the mean beta value in bins of MUV, doesn't quite have the right trend.

Overall, from the plots below, seems like dust is the parameter that is going to matter the most.

### Galaxy Mass

<img src="{{ site.baseurl }}/assets/plots/20210217_MUV_testpoints_mass.png">

### Beta

<img src="{{ site.baseurl }}/assets/plots/20210217_MUV_testpoints_beta.png">

### Dust

<img src="{{ site.baseurl }}/assets/plots/20210217_MUV_testpoints_dust.png">

### SFR

<img src="{{ site.baseurl }}/assets/plots/20210217_MUV_testpoints_SFR.png">

### Age

<img src="{{ site.baseurl }}/assets/plots/20210217_MUV_testpoints_age.png">

### Metallicity
<img src="{{ site.baseurl }}/assets/plots/20210217_MUV_testpoints_met.png">
