---
layout: post
title:  "Check Image Artefacts"
date:   2021-12-03
categories: mocks
---

There are a few different image artefacts I want to check... PSF looks strong, also rings around galaxies..


## PSF

PSF looks really prominent...Could be because noise levels are too low (see previous post)... or because galaxy sizes aren't assigned properly... 

### Noise Levels


does PSF convolution depend on brightness of object???

Does it look better if I artificially increase the background by a factor of 5???


### Galaxy Sizes

triple check galaxy sizes make sense... are some just very compact? ... should there be a truncation in assigned galaxy sizes???
are the sizes assigned in the right units in galsim https://galsim-developers.github.io/GalSim/_build/html/units.html#size-units



## Rings

Some galaxies have rings around them...
