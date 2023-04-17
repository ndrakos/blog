---
layout: post
title:  "Reionization Shell Model Part VI"
date:   2023-04-17
categories: reion
---

In the <a href="https://ndrakos.github.io/blog/reion/Reionization_Shell_Model_Part_V/">last post</a>, I showed my calculation for the bubble size of one galaxy. The sizes of the test galaxies I looked at seemed reasonable.

This post is about running on the full catalog (with $$f_{esc}=0.2$$)

## Timing

It took me about 2 hours on 2 processors to run on the test galaxies on my computer.

The test catalog has 42075 galaxies, compared to $$\approx 3.3 \times 10^7$$ in the full DREaM catalog.

That means I expect it to take approximately 3000 CPU hours to run the bubble calculation on the full catalog. If I want it to take less than I day, I will need to use a couple hundred processors, so this is completely doable.

## Results

Here are the galaxies between redshift~6  (between z=5.5 and 6.5)


<img src="{{ site.baseurl }}/assets/plots/20230417_Topology6.png">

and at redshift~7

<img src="{{ site.baseurl }}/assets/plots/20230417_Topology7.png">


Note that:
- these are only the test galaxies. Therefore there are about 1000x more galaxies in the full catalog
- these should be the brightest galaxies, with the largest bubbles
- I did not take a cross-section to get the circle radii, but just used the radii of the full bubble in the plots


I think these look roughly okay. I need to plot with the full catalog to get a better sense.

## A comment on the Naidu model

Since the Naidu model assumes that the escape fraction is a function of the SFR surface density, it should actually be a time-varying quantity. Therefore, I need to figure out how to calculate the escape fraction for each galaxy as a function of time, not just use a constant value as I did here.


## Next Steps

1. Run this on lux on the full catalog
2. Figure out better ways to plot this
3. Write some code to calculate the ionized volume given the bubble sizes
4. Calculate bubble sizes given the time-varying $$f_{esc}$$ values from Naidu et al. 
