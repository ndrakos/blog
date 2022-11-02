---
layout: post
title:  "Check DREaM Colours"
date:   2022-11-01
categories: cosmos_web
---

Steve is looking into galaxy colours in different simulation data sets. There are a couple places where DREaM looks a little different from other simulations, so I am double checking my flux calculations in this post.

In the following, I will select galaxies with F200W between 24 and 28.

## Check Transmission Curves

I had included the jwst filters manually in FSPS. According to the FSPS documentation, "The filter can be of any resolution, and need not be properly normalized".

Here are the transmission curves I have in FSPS:

<img src="{{ site.baseurl }}/assets/plots/20221101_fsps_filters.png">

These look about right.

## Colours

Next, I'm going to look at the average colour versus redshift in the catalog, and see if I get the same thing as Steve.

Here are the colours. Blue is from the original catalog, orange is from the extra catalog (that contains the F410M filter; I plotted both just to double check they were consistent).

<img src="{{ site.baseurl }}/assets/plots/20221101_Colours.png">

These actually look like the other mocks, and not quite what Steve got. So I think things are fine with the DREaM colours, and I'm not sure why our answers are different!
