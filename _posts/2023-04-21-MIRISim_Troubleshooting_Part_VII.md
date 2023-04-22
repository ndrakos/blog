---
layout: post
title:  "MIRISim Troubleshooting Part VII"
date:   2023-04-21
categories: cosmos_web
---

This is a continuation of <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_VI/">Part VI</a>/


## FITS Files

In the last post, I realized that if I just replaced the header of my scene (Scene A), this the test galaxy in <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_VI/">Test 4</a> (Scene B), I was able to see sources in my simulation. The header in Scene B is definitely wrong, but I thought this could be a good starting point to see where things are going wrong in Scene A.

Here are the headers for Scene A:

<img src="{{ site.baseurl }}/assets/plots/20230421_headerA.png">

and Scene B:

<img src="{{ site.baseurl }}/assets/plots/20230421_headerB.png">


Note that this is what the MIRISim documentation says:

<img src="{{ site.baseurl }}/assets/plots/20230421_documentation.png">


## Tests

1) I changed UNITS3 to CUNITS3. This didn't make any difference.

2) I multiplied the flux by 1000000 (in case units are wrong). There are possibly some sources, but it is hard to tell:

<img src="{{ site.baseurl }}/assets/plots/20230421_test.png">

3) I tried changing the units to say "arcsec" instead of degrees, and it made no difference

## Next steps

Overall I'm very puzzled about what's happening!

I will
1. Go through an example notebook, as pointed out in the MIRISim documentation
2. Try adding background + noise directly to the scene fits file, so I can visually see the galaxies better
3. Create the scene for the full DREaM catalog
