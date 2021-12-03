---
layout: post
title:  "Check Image Noise Part II"
date:   2021-12-03
categories: mocks
---

In the <a href="https://ndrakos.github.io/blog/mocks/CheckImageNoise/">previous post</a>, I went through some checks on the image SNR for our DREaM catalogs, and concluded that the background noise was about 5x too low.

I think I figured out why!

## Assigning galaxy fluxes

I begin with AB magnitudes returned from FSPS, which are calculated based on the Roman filter transmission curves. I then convert these values to fluxes in the usual way. To put this into galsim, I then convert to photons/cm^2/s. Bruno uses this to assign a total brightness to each galaxy. The final image is converted back into nJy using the same conversion.

My method of converting galaxy fluxes to photon density did not properly take into account the filter information. It should be:

$$\int \frac{T(\nu)f_\nu}{h \nu } d\nu = \frac{f_\nu}{h} \int \frac{T(\nu)}{\nu } d\nu $$.

Therefore I was missing a factor of $$\int \frac{T(\nu)}{\nu } d\nu$$ in the assigned galaxy fluxes. This is filter dependent, but corresponds to a factor of ~0.15. Assigning this correctly will increase the background when we convert back to nJy by a factor of 6 or so!

In galsim, the conversion can be calculated as:

```
lam = filter.wave_list
T = filter.func(lam)
correction = np.trapz(-T*lam,1/lam)
```

<!---
This is not enough to account for the factor of 5 (it is a factor of about 1.3 in the H band), but it goes in the right direction.



## Zeropoints

The galsim code uses bandpass information in two places (1) when adding the PSF and (2) when calculating the sky level. I want to make sure that the sky level calculation is using the same zeropoint information as the galaxies (i.e. we agree when the flux is equivalent to one photon in the detector).


The zeropoints in galsim are treated as outlined <a href="
https://galsim-developers.github.io/GalSim/_build/html/_modules/galsim/roman/roman_bandpass.html">here</a>



The zeropoint in GalSim is defined such that the flux is 1 photon/cm^2/sec through the bandpass. This differs from an instrumental bandpass, which is typically defined such that the flux is 1 photon/sec for that instrument. The difference between the two can be calculated as follows:

# Shift zeropoint based on effective collecting area in cm^2.
area_eff = galsim.roman.collecting_area
delta_zp = 2.5 * np.log10(area_eff)





## SNR calculation

In the previous post I did a simple SNR calculation... double check 0.2 arcsec^2 is the right size

Slightly more careful method... take 10 aperatures placed by eye in background... find the average and std in each... From this calculate the average and std among the apertures (does this std agree with the Nsqrt(sigma)??)

Comparing this in all the filters to see if they all seem off by a factor of 5.




## Test a single galaxy

generate a galaxy with a given flux... run through... check it is the right total flux (after subtracting background)


## Other sources of error


are the other sources of error subdominant???
--->
