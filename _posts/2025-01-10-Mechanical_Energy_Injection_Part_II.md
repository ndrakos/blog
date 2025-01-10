---
layout: post
title:  "Mechanical Energy Injection Part II"
date:   2025-01-10
categories: sne
---


In this post I'm continuing my thoughts on how the  mechanical energy injected into the ISM from SNe to increase the LyC escape fraction, but taking an easier approach.

## Step 1

Let $$\xi$$ by the rate of SN in our blueberry sample compared to the field. This is something that we will directly measure with our sample.

Things we need to consider are how we will cut the data. For example, is this within a certain mass range?


## Step 2

A simplified model for how escape fraction is related to the "covering fraction", $$f_cov$$ as follows:

$$f_{\rm esc} = 1 - f_{\rm cov}$$

The covering fraction is an effective fraction describing how much of the galaxy is covered by optically thick neutral hydrogen. See <a href="https://www.aanda.org/articles/aa/full_html/2018/08/aa32759-18/aa32759-18.html">Gazagnes</a>, where they measured this fraction to understand the connection between the covering fraction and the escape fraction.

This model is probably much too simplified, and likely doesn't work in cases where there is complex geometry, but I'm going to use it as a starting point.

## Step 3

Finally, if we assume that if there is $$\xi$$ times the number of supernova, you can clear out $$\xi$$ times the amount of gas, you can find

$$f_{\rm cov, bb}= \frac{f_{\rm cov, field}}{\xi}$$

This assumes that SNe are primarily responsible for clearing out gas (e.g. ignores things like stellar winds, radiation pressure). It also assumes that SNe are just as effective at clearing out gas in blueberries than as in the field galaxies we are comparing it to. It might be the case that, e.g., compact galaxies are more efficient at clearing out gas.

## Step 4

Putting this together,

$$f_{\rm esc,bb} = 1 - f_{\rm cov,bb} = 1 - \frac{f_{\rm cov, field}}{\xi} = \frac{\xi - 1 + f_{\rm esc,field}}{\xi} $$


## Results

Here is my plot:


<img src="{{ site.baseurl }}/assets/plots/20250110_f_esc.png">



I don't trust this though. For example, when $$f_{\rm esc,field}=0$$, how could doubling the supernova cause the escape fraction to clear out by fifty percent? This seems like a flaw with step 3 in my calculations.


## Next steps:

1. Go through literature, see if I can find sanity checks.
2. Go through each of these steps and try to improve on my assumptions/simplifications.