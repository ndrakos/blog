---
layout: post
title:  "MIRISim Scene Part III"
date:   2023-04-13
categories: cosmos_web
---

When troubleshooting why my MIRI simulations aren't working, I decided the problem is with how I am creating the scene (see <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_V/">"MIRISim Troubleshooting Part V"</a>).

When creating the scene, I noted at the time the sources looked strange, but thought it might just have had to do with the way the data was displayed (see <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Scene_Part_II/">MIRISim Scene Part II</a>)

In this post, I am going to revisit this issue.


## Stamps


```
Previous code for adding stamps of each galaxy:

pos = positions[i]
stamp_size = int(np.ceil(radius[i]*3)*oversample) #pixels
stamp_size = max(stamp_size,5)

#Make Stamp
table['r_eff'] = np.array([radius[i]]) * u.arcsec#effective half-light radius
table['n'] = np.array([sersic_index[i]])
table['x_0'] = np.array([stamp_size/2.0]) * u.arcsec
table['y_0'] = np.array([stamp_size/2.0])* u.arcsec
table['ellip'] = np.array([ell[i]])
table['theta'] = np.array([position_angle[i]])
table['amplitude'] = np.array(flux)*u.mJy/A[i]# Surface brightness at r_eff
sersic_stamp = make_model_sources_image((stamp_size,stamp_size), model, table,oversample=oversample)


#Make hdul
myra = ra_list[i]; mydec = dec_list[i]
size_arcsec = stamp_size/oversample # size of stamp in arcsec
mybounds = [myra - size_arcsec/3600/2, myra+ size_arcsec/3600/2, mydec-size_arcsec/3600/2, mydec+size_arcsec/3600/2]
stamp_hdul = create_hdul(mybounds, size_arcsec/stamp_size/3600 )
stamp_hdul[0].data = sersic_stamp.T
stamp_hdul.writeto('teststamp.fits', overwrite=True)
```


I don't think that "make_model_sources_image" knows the arcsec/pixel scale, so it wasn't properly converting the image.

Therefore, I rewrote this to give the size of the galaxy in pixels (I also changed oversample from 10 to 2):


```
pos = positions[i]
myrad = radius[i]*oversample/pixscale # pixels
stamp_size = max(int(np.ceil(myrad*5)),5)

#Make Stamp
table['r_eff'] = np.array([myrad]) * u.pix #effective half-light radius
table['n'] = np.array([sersic_index[i]])
table['x_0'] = np.array([stamp_size/2.0]) * u.pix
table['y_0'] = np.array([stamp_size/2.0])* u.pix
table['ellip'] = np.array([ell[i]])
table['theta'] = np.array([position_angle[i]]) *u.rad #radians
table['amplitude'] = np.array(flux)*u.mJy/A[i]# Surface brightness at r_eff [mJy/arcsec**2]
sersic_stamp = make_model_sources_image((stamp_size,stamp_size), model, table,oversample=oversample)


#Make hdul
myra = ra_list[i]; mydec = dec_list[i]
size_arcsec = stamp_size/(oversample/pixscale) # size of stamp in arcsec
mybounds = [myra - size_arcsec/3600/2, myra+ size_arcsec/3600/2, mydec-size_arcsec/3600/2, mydec+size_arcsec/3600/2]
stamp_hdul = create_hdul(mybounds, size_arcsec/stamp_size/3600 )
stamp_hdul[0].data = sersic_stamp.T
stamp_hdul.writeto('teststamp.fits', overwrite=True)

```

Here is an example galaxy in both of these versions:

<img src="{{ site.baseurl }}/assets/plots/20230413_stamp.png">

Note that on the left, the galaxy stamp is 180x180 pixels, and in the right, the stamp is 522x522 pixels. I think that I was therefore mapping the galaxy stamps to the wrong number of pixels.


For this test galaxy, it has a (pixel) half-light radius of 104. Exploring a bit how big I should make the stamp, I have plotted the total flux (i.e. summing up over all pixels in the stamp) as a function of the stamp size.

<img src="{{ site.baseurl }}/assets/plots/20230413_stampsize.png">

From this, I decided to make stamps about 10x the half-light radius of the source.


Running all of the (test) galaxies, I find the following:

<img src="{{ site.baseurl }}/assets/plots/20230413_sources.png">


And looking at the test galaxy, and how big I expect the stamp to be I find:

<img src="{{ site.baseurl }}/assets/plots/20230413_sources_stamp.png">

Now I am fairly positive the locations and sizes of the galaxies are set correctly!


## Next Steps

1. Test if this fixes my whole issue
2. Rerun this for the full catalog
