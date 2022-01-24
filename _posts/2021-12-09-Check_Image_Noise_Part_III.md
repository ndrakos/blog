---
layout: post
title:  "Check Image Noise Part III"
date:   2021-12-09
categories: mocks
---

In <a href="https://ndrakos.github.io/blog/mocks/CheckImageNoise/">Part I</a> I argued that the noise level in the images was a factor of ~5 too low.

In <a href="https://ndrakos.github.io/blog/mocks/CheckImageNoise/">Part II</a> I proposed a solution.

In the current post, I will verify that this solution works.


## The test images

I am starting with a cropped (2048x2048 pixel) image of the H158 filter (no PSF). I have fixed the conversion in translating the galaxy fluxes to and from photon counts, as outlined in <a href="https://ndrakos.github.io/blog/mocks/CheckImageNoise/">Part II</a>. The fluxes of individual galaxies should be the same, but the SNR should decrease, and the depth of the image should be ~30 mag.


Here is the image before (left) and after (right) the correction:

<img src="{{ site.baseurl }}/assets/plots/20211209_correction.png">




## Checking galaxy fluxes

The image cutout corresponds to the bottom left corner of the FITS map image, so it was very easy to look up the galaxy properties (thanks Ryan!)I am checking galaxy 3865765, which should have an H158 magnitude of 18.66:

<img src="{{ site.baseurl }}/assets/plots/20211209_testgalaxy.png">



I estimated the background flux by taking a circular aperture of radius 0.5 arsec placed in the background of the image, and finding the average value in the aperture.

To roughly calculate the magnitude of the galaxy, I drew an ellipse around the galaxy in DS9 as shown below:

<img src="{{ site.baseurl }}/assets/plots/20211209_testgalaxy_select.png">

Then the flux of the galaxy was calculated as the (sum of the pixel values)- (the average background pixel value)X (area of ellipse)

In both panels, got a total flux of about 141000 nJy (143502.15 in the left panel, 140836.70 in the right panel). This corresponds to a magnitude of   $$-2.5\log_{10}(141000*1e-9/3631) = 18.5$$.

This is a good check that the galaxy fluxes are correct!



## Checking the SNR


Using the same rough calculation as outlined <a href="https://ndrakos.github.io/blog/mocks/CheckImageNoise/">Part I</a>, I calculate the standard deviation in the background pixels are about 0.03 nJy in the left, and 0.2 nJy in the right. Using a circular aperture of radius 0.5 arcsec, this gives me 5 sigma depths of 31.2 (left) and 29.1 (right)


Using a more careful approach, I used sigma clipping in astropy to get the background, and then found the std of the background. i.e:

```
stats.sigma_clipped_stats(flux.array, sigma=2, maxiters=5)
```

returns the mean, median and standard deviation in the background pixels. For the left and right images, I get (9.81447, 9.800997, 0.06486408) and (61.49829, 61.49397, 0.2043947).

Assuming a circular aperture of radius 0.2 arcsecs^2, this corresponds to $$ 0.2/0.11^2 =  16.5$$ pixels.

Then, using

$$-2.5\log_{10}\left(\dfrac{5 \sqrt{N} \sigma *10^{-9}}{3631 \rm{Jy}}\right) $$

I get 5 sigma depths of 31.1 (left) and 29.8 (right).

Redoing this with the PSF images, I get depths of 30.5 (left) and 29.7 (right).


Overall, the SNR is dependant and the aperture, and how I measure the noise. But to me, the updated version looks much more reasonable, and agrees closer with the Hubble example in <a href="https://ndrakos.github.io/blog/mocks/CheckImageNoise/">Part I</a>

<!---
(9.887569, 9.856411, 0.1084179)
(61.57623, 61.5661, 0.23153158)-->
