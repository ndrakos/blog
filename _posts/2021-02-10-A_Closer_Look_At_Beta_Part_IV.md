---
layout: post
title:  "A Closer Look At Beta Part IV"
date:   2021-02-10
categories: mocks
---

This is a continuation of this <a href="https://ndrakos.github.io/blog/mocks/A_Closer_Look_At_Beta_Part_III/">post</a>.


## Previous $$\beta-M_{\rm UV}$$

We have been having issues reproducing the expected $$\beta--M_{\rm UV}$$ trends. I fixed a problem where some galaxies were accidentally being assigned really high SFRs, but it didn't change the  $$\beta--M_{\rm UV}$$ problem.

As a reminder, here is a plot shown the issue (note that this plot, and all the following in this post are only for star-forming galaxies):

<img src="{{ site.baseurl }}/assets/plots/20200929_MUV.png">

The dotted lines are the expected trends from W18, and the solid lines are my mock galaxies.


## Reject/accept method

Since the age distributions I was using to assign galaxy ages weren't well motivated, I changed the SED assignment as follows:

Galaxy ages were selected uniformly between $$10^6$$ years and the age of the universe.

Once an SED was assigned, I chose two random numbers between 0 and 1, and then accepted/rejected the galaxy properties based on the PDF of (1) a gaussian centred at the expected mass-MUV and (2) a gaussian centred at the expected MUV-beta relation (with the standard deviations chosen to be consistent with the expected relations.) Ideally, this would reproduce the expected trends, but since the UV properties are non-linear and depend on a combination of many parameters, the UV properties are not uniformly distributed, and therefore we are not guaranteed to produce the target distributions.

The resulting relations are shown in this plot:

<img src="{{ site.baseurl }}/assets/plots/20210210_MUV.png">

This looks a lot better than before, particularly for low redshifts. However constraints for beta-MUV mainly at $$z=4$$ see for example W18 plot.


<img src="{{ site.baseurl }}/assets/plots/20210210_W18_fig9.png">


I am not **too** worried about the uptick in the trend, because I am hoping it is a mass resolution issue (these are the $$512^3$$ simulations)... these faint galaxies are much more massive than typical for their magnitudes, so might not follow the relation. E.g. the redshift 0 galaxies are incomplete below magnitudes of $$-17$$, which is where the $$\beta--M_UV$$ relation begins to turn up. However, this is something I need to check.

It is also interesting to look at the resulting age distributions:

<img src="{{ site.baseurl }}/assets/plots/20210210_age_dist.png">



## Dust

Overall, $$beta$$ should mainly depend on age, metallicity, and dust. Brighter, more massive galaxies are older, have higher metallicities and more dust and are therefore redder (shallower slopes).

To see the affect of dust, I set the dust parameter to zero, and otherwise kept the same method here is the resulting plot:

<img src="{{ site.baseurl }}/assets/plots/20210210_MUV_nodust.png">

Clearly this is a lot worse, with the galaxies being too bright with steeper UV slopes. Interestingly, the upturn in the relation is not as pronounced though, so maybe this is not solely a resolution issue. 
