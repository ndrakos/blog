---
layout: post
title:  "Crossmatch Catalog Part III"
date:   2024-05-31
categories: cosmos_web
---


In  <a href="https://ndrakos.github.io/blog/cosmos_web/Crossmatch_Catalog/">Part I</a> and   
<a href="https://ndrakos.github.io/blog/cosmos_web/Crossmatch_Catalog_Part_II/">Part II</a> 
I was looking at how well the SE++ catalog recovered the input galaxy properties.

Here I'm looking more closely at the images, and trying to verify the galaxies have the right RA and dec assigned. 


## Plotting the galaxies on top of the image

The easiest way to compare the sources to the image is to make region file from catalog, then just load in DS9.
I drew each galaxy as an ellipse, with its size as the half-light radius, the shape of the ellipse scaled according to the galaxy ellipticity. 
I used the position angle to give a tilt to the ellipse. 

Here is the whole catalog, with the B1 tile shown underneath:

<img src="{{ site.baseurl }}/assets/plots/20240531_sources.png">

It looks like the SE++ catalog only contains B tiles (and is missing B9).


Here is a zoom-in:

<img src="{{ site.baseurl }}/assets/plots/20240531_sourceszoom.png">


I think it looks pretty decent, but there are some obvious mis-identified galaxies.



## Updated ellipticity

One thing I realized while putting this together was that I was using the wrong "ellipticity" parameter in the SE catalog.
Here's an update of the recovered versus input parameter plot:

<img src="{{ site.baseurl }}/assets/plots/20240531_morph.png">


## To-Do

Here's what's left on my to-do list for this:

- Figure out why some tile file sizes are different (different “PXSCLRT” parameters)
- See if Marko will rerun SE++ with updated F444w catalogs (and for full field)
- Solidify cross-matching procedure 
- Post these results, see what people think (it will be easier to conclude things once I have some redshift information)


