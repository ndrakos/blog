---
layout: post
title:  "Galaxy Morphologies"
date:   2021-02-05
categories: mocks
---

I want to assign galaxy sizes, shapes and Sérsic indicies.

## Size

I have already outlined my method for assigning galaxy size, $$R_{\rm eff}$$ <a href="https://ndrakos.github.io/blog/mocks/Galaxy_Sizes_Part_II/">here</a>. This method depends on redshift, halo size and whether the galaxy is star-forming.

Note that this size is the projected galaxy size.

## Shape and Sérsic Indicies

I am going to follow W18's method of assigning shapes and Sérsic indicies, which was based on data from <a href="https://ui.adsabs.harvard.edu/abs/2014ApJS..214...24S/abstract">Skelton et al. 2014</a> and <a href="https://ui.adsabs.harvard.edu/abs/2012ApJS..203...24V/abstract">van der Wel et al. 2012</a>.

Using Christina's code, I selected projected axis ratios $$q=b/a$$ and sersic indicies $$n$$ based on these distributions. Here are my resulting assignments:

<img src="{{ site.baseurl }}/assets/plots/20210205_Morphology.png">

This agrees with Fig. 16 in W18:

<img src="{{ site.baseurl }}/assets/plots/20210205_W18Morphology.png">



## Inclination Angles?

We have assigned a projected size and projected shape. To make images, we will also have to assign inclination angles---if we have a 3D angle this will also give the intrinsic size and shape.

Is this something we want/will need? We could potentially assign angles uniformly in 3D space. While this isn't entirely accurate, it probably won't be a problem for our application.


## Potential Issues

### Other Correlations?

Our method assigns shapes and Sérsic indicies based on redshift and whether a galaxy is star-forming. However, it will not capture any other correlations (i.e. between halo properties and galaxy properties, or based on the star formation rates).

This paper indicates that galaxy shapes actually aren't very correlated with halo shape.
<a href="https://ui.adsabs.harvard.edu/abs/2017MNRAS.472.1163C/abstract">Chisari et al. 2017</a>, but galaxy orientations are. 



### Extrapolations to Higher Redshifts

Another potential issue is that there is no high redshift data, so there is an assumption that the highest redshift galaxies have the same distribution as those at the deepest measurements.. I'm not too worried about this though.
