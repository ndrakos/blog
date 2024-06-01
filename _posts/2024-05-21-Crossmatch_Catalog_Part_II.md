---
layout: post
title:  "Check Extracted Catalog"
date:   2024-05-21
categories: cosmos_web
---

I want to compare the catalog from the Source Extracted Catalog to the input catalog, and see how well it recovered the flux and photometric fluxes. 




## Cross-Matching

In the  <a href="https://ndrakos.github.io/blog/cosmos_web/Crossmatch_Catalog/">previous post</a>, I outlined a method for crossmatching the SE++ catalog to the input catalog. My method gave the same IDs as astropy's cross-matching tool 99.9 percent of the time.
 However, my method has the advantage that I can build in other parameter for matching if needed!
 
Another important thing to note is that the SE++ catalog only includes 368099 of the 9004036 input sources (4 percent). 
 This is likely because (1) many of the input sources are very faint and (2) some of the galaxies will be obscured by foreground galaxies. 
 This also means that I might have a bunch of galaxies on top of each other, which could be a problem for my RA/Dec cross-matching!
 


## Photometry

If I plot input to output photometry I get the following:

<img src="{{ site.baseurl }}/assets/plots/20240521_SE_check.png">


This is pretty good, but not fantastic. It's a little hard to tell what's due to problems in the cross-matching, 
and what is due to problems in the SE++.

## Updated Cross-Matching

Updates to cross-matching procedure
- Only match to galaxies in input galaxy that are brighter than 30 mag in at least one band
- First find the 10 closest neighbours in position, then out of these 10, find the input galaxy that is closest in photometry
- I weight each band by max(0,30-flux)


Here is the updated flux plots

<img src="{{ site.baseurl }}/assets/plots/20240521_SE_check_2.png">

This does look better!

If we look at how many are detected in the SE catalog for both we find:

<img src="{{ site.baseurl }}/assets/plots/20240521_SE_check_dist.png">

This looks pretty similar, except in the updated matching there are less objects matched to very faint objects from the input catalog. 
Another thing is that the SE catalog is not complete even for bright galaxies! This is probably due to obscured galaxies by foreground objects. 


## Morphology

Lilan is doing a more careful morphology analysis, but SE++ does also return its own. 
I don't have any sort of read-me file for the catalog, so I guessed how the parameters are defined/what units they are in.

With the old cross-matching:

<img src="{{ site.baseurl }}/assets/plots/20240521_SE_check_morph_2.png">


With the new cross-matching


<img src="{{ site.baseurl }}/assets/plots/20240521_SE_check_morph_2.png">


These actually look really similar and not that great. I think I will have to dig into how all the parameters are defined.






