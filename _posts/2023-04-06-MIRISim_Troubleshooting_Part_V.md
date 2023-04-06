---
layout: post
title:  "MIRISim Troubleshooting Part V"
date:   2023-04-06
categories: cosmos_web
---

In this post I'm going to troubleshoot why my MIRI simulations don't have any visible sources.

This is a continuation of <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_I/">Part I</a>, <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_II/">Part II</a>, <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_III/">Part III</a>, and <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_IV/">Part IV</a>.



## Test 5

For Test 5, I will fix the units in the DREaM Scene.

In <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_III/">Part IV</a>, I found that the biggest difference was in the keyword "UNITS". For my test, the units were  uJy/arcsec^2, which is also what MIRISim assumes by default.

I had **not** properly set this in the DREaM sims. Looking at my code, it should actually be mJy/arcsec**2. This would mean the objects were 1000x fainter than they should be. I fixed the units, but things still look weird. Here is the only source I can easily pick out from the reduced data:

<img src="{{ site.baseurl }}/assets/plots/20230406_Test5.png">


I am returning to my earlier suspicions in <a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Scene_Part_II/">this post</a>, that there is something wrong with how I am creating the scene.

In the next post, I'm going to examine the scene in more detail, and figure out what's going on there.


## Next Steps

1. Go through the scene code again, really figure out if I am drawing on the galaxies correctly!
2. Use the test galaxy (<a href="https://ndrakos.github.io/blog/cosmos_web/MIRISim_Troubleshooting_Part_IV/">Part IV</a>) to really understand the pointings/whether I'm setting the WCS right. Run this example through the full MIRISim code, check the WCS of the final images.
