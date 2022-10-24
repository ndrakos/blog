---
layout: post
title:  "Testing Neutrinos in Gadget"
date:   2022-09-16
categories: neutrinos
---

I have been working IC code with dark matter particles. I also have sorted out how to add neutrinos as a second species. In this post I'll what they look like in Gadget.



Note softening lengths + treeallocfactor "if there are many particle pairs with identical or
nearly identical coordinates, a higher value may be required."

## Testing in Gadget

I ran this in Gadget... Left neutrinos as a separate particle... To keep the number of neutrinos and dark matter particles approximately the same, i used... This is still slightly more particles than is quick to run on my laptop, so I moved to lux...

### Density Field

<img src="{{ site.baseurl }}/assets/plots/20220909_Snapshot.png">


### Power Spectrum


<img src="{{ site.baseurl }}/assets/plots/20220909_PowerSpectrum_DM.png">


### Conclusions

Looks like it is working okay... will want to

## Next Steps
