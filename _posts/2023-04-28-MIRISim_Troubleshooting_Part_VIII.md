---
layout: post
title:  "MIRISim Troubleshooting Part VIII"
date:   2023-04-28
categories: cosmos_web
---

This is a continuation of <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_VII/">Part VII</a>


## Delete rotation keywords

When playing around with MIRISim, I noted that the output log said "Rotation keywords found. Derotating the cube"

I was not sure HOW MIRISim was treating this, so I deleted the following keywords in my FITS file:

<code> del hdu_cutout.header['PC1_1']; del hdu_cutout.header['PC1_2']; del hdu_cutout.header['PC2_1']; del hdu_cutout.header['PC2_2']; </code>

This actually seemed to help fix things! Here is the raw Miri Data:

<img src="{{ site.baseurl }}/assets/plots/20230428_Test8.png">

Now there are clearly sources, but (1) they look much too bright and/or compact and (2) I haven't checked that their positions are correct yet.


## Quick Test on Brightness

I am pretty sure that the units should be <code>mJy/arcsec**2</code>, but I changed <code>UNITS</code> to <code>uJy/arcsec**2</code>, to check how things look. I'm worried MIRISim isn't taking units into account internally.

Here is the raw data when I change that key word:

<img src="{{ site.baseurl }}/assets/plots/20230428_Test8B.png">

It looks identical! Which makes me suspect that MIRISim is not converting units. I will change everything to be in uJy, and arcsec, which I suspect MIRISim assumes.

## Next Steps

The sources are now appearing, some of the next steps are

1. Change the scene to be in uJy and arcsec
2. Figure out how to match the final output to the input sources, to make sure the positions are correct. This will involve properly running the final step of the MIRISim simulation to update the WCS.
3. Run the full DREaM source catalog (right now I am using the Test Catalog)

4. Check the rotation/offset of the pointing is correct (I might need to talk to some of the observers for this!)

5. Check the flux/noise level of sources is correct.
