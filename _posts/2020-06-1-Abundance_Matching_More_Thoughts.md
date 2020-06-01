---
layout: post
title:  "Abundance Matching More Thoughts"
date:   2020-06-01

categories: mocks
---

I have been thinking a bit about the plot below---why does the SMF not quite match at the high mass end?

<img src="{{ site.baseurl }}/assets/plots/20200528_AbundanceMatching.png">


Thinking about this more, this is because once scatter is added to the $$v_{\rm peak}$$ values, the HVF of the simulation data changes. This is not what I want.

Therefore, as an update to the method, rather than match the scattered $$v_{\rm peak}$$ values to the galaxy mass exactly (by solving $$\int_x^\infty n(x') dx' = \int_{M_*}^\infty \phi (M_*') dM_*’$$), I instead randomly generate $$M_{\rm gal}$$ values from the SMF, and then rank order the resulting masses---this ensures the SMF is preserved.

This requires setting a minimum mass in the SMF: Therefore, I only consider $$v_{\rm peak}$$ values above $$2.1 \, \rm{dex}$$ (this value was chosen, since for the $$512^3$$ simulation the HVF looks incomplete below this limit). Then, solving $$\int_x^\infty n(x') dx' = \int_{M_*}^\infty \phi (M_*') dM_*’$$, this sets the minimum galaxy mass to be $$9.79$$.

## Current Abundance Matching Implementation


**BASIC ABUNDANCE MATCHING PROCEDURE**

1. Get the minimum galaxy mass (corresponding to the minimum $$v_{\rm peak}$$ value)

2. Randomly generate $$N$$ $$M_{\rm gal}$$ values so that they match the SMF (where $$N$$ is the number of halos with $$v_{\rm peak}$$ above the minimum value)

3. Rank-order the galaxy masses, and assign them to each halo (so that the halo with the largest $$v_{\rm peak}$$ has the largest galaxy masses)

**GENERATE A MAPPING IN THE SCATTER**

1. Randomly generate $$10^7$$ $$v_{\rm peak}$$ values from the HVF function (I am using a minimum $$v_{\rm peak}$$ value of 1.5 dex for this step)

2. Loop through different fixed scatter values in $$v_{\rm peak}$$: I am using 100 values linearly spaced between 0 and 0.5.

3. For a given scatter value, add guassian errors to the $$v_{\rm peak}$$ values

4. Perform abundance matching (as outlined above) using these scattered values

5. Bin the resulting masses, and measure the scatter in $$M_{\rm gal}$$ as a function of $$v_{\rm peak}$$

6. Repeat steps 3-5 for each scatter value

**ABUNANCE MATCHING WITH SCATTER**

1. Choose a constant scatter in $$M_{\rm gal}$$

2. For each vpeak value use the mapping from above to get the corresponding scatter in $$v_{\rm peak}$$

3. Add scatter to the $$v_{\rm peak}$$ values, and use these scattered values to perform the abundance matching step

## Results

Here is the updated plot:

<img src="{{ site.baseurl }}/assets/plots/20200601_AbundanceMatching.png">


The SMF looks better, but the stellar mass --- $$M_{\rm peak}$$ relation looks worse... I think this is just resolution issues though, and I expect it will look better with the 1024 simulations.
