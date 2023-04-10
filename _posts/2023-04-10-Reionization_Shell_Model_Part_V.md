---
layout: post
title:  "Reionization Shell Model Part V"
date:   2023-04-10
categories: reion
---

In this post, I want to double check that I am normalizing the mass of the galaxies properly.

## FSPS

FSPS returns spectrum normalized so that 1  $$M_{\odot}$$ of mass is formed over the star formation history.

To scale it properly, you have to multiply the spectrum by the current mass, and then divide by the fraction of mass surviving at that point in the galaxies history (given by the FSPS parameter <code>stellar_mass</code>, which I will call $$x$$).

Looking at my code, I am normalizing the spectrum by the mass of the galaxy at redshift $$z_{red}$$, not by the mass at the "age" of the galaxy. Therefore, my galaxies are too massive at $$z>z_{red}$$!

Consider a galaxy at $$z=z (a)$$ and mass $$M=M(a)$$. I want to know the mass at $$z(t)>z (a)$$

For a delayed-tau model, the mass formed should be (found by integrating over $$te^{-t/\tau}$$):

$$M_{form}(t) \propto \tau^2 - (\tau^2 + t\tau) \exp^{-t/\tau}$$


Therefore the FSPS spectrum can be scaled by:

$$\dfrac{ M_{form}(t) }{ M_{form}(a) } \dfrac{M(a)}{x(t)} $$




## Results



This didn't change the ionization history (<a href="https://ndrakos.github.io/blog/reion/Reionization_Shell_Model_Part_II/">here</a>) or sizes (<a hfref="https://ndrakos.github.io/blog/reion/Reionization_Shell_Model_Part_IV/">here</a>) of these galaxies by much from previous posts:

<img src="{{ site.baseurl }}/assets/plots/20230410_Nion.png">

<img src="{{ site.baseurl }}/assets/plots/20230410_Volume.png">



## Next Steps

1. Write code to do this for all the galaxies, make sure it is fast enough.
2. Plot the ionized regions, see if this agrees with what is expected
