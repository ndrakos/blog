---
layout: post
title:  "MIRISim Troubleshooting Part VI"
date:   2023-04-19
categories: cosmos_web
---

I believe I fixed the sized of the sources in <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Scene_Part_III/">my last post, MIRISim Scene Part III"</a>.

I'm going to run MIRISim and double check


## Test 6

This will be the same as <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_III/">Part V</a>, but with the "test" scene from the previous post


Here is the cutout of the scene:


<img src="{{ site.baseurl }}/assets/plots/20230419_Test5sources.png">


And here is one observation, after the pipeline:

<img src="{{ site.baseurl }}/assets/plots/20230419_Test5.png">

There are still no sources!

## Troubleshooting


1. Try without background

Maybe the background is too high (or in different units than the sources)? I tried running it without adding a background, and it did not help.

2. Set WCS in cutout

Looking at the test in <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_IV/">Part IV</a>, that object had the WCS defined in DS9, where ours does not.

I fixed this by deleting a keyword in the header: <code>del hdu_cutout.header['WCSAXES']</code>

However, this did not fix things.

3. Use the same WCS as in Test 4

I imported the header from <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_IV/">Test IV</a>, and just replaced the header with this.

This seemed to result in sources!

<img src="{{ site.baseurl }}/assets/plots/20230419_Test5WCS.png">

Note that this WCS
- has the wrong pointing
- has the wrong pixel to size mapping
- has the wrong units

I need to dig into all of these in more detail, and see where things are going wrong


## Next Steps

1. Alter the heading manually, make sure everything is set correctly
2. Make a scene for the whole DREaM catalog
