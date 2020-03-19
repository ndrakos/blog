---
layout: post
title:  "Test Simulation"
date:   2020-03-18

categories: cosmo_sims
---


Here I'm testing my simulation setup on my laptop using $$128^3$$ particles.

## Parameters

I am using the set-up discussed <a href="https://ndrakos.github.io/blog/cosmo_sims/Simulation_Parameters/">here</a> with the following modifications:

1) $$128^3$$ particles corresponds to level 7 in the MUSIC ICs

2) The softening length is now $$\epsilon = 17.96 \, h^{-1} {\rm kpc}$$

3) TimeOfFirstSnapshot = 0.047619 (redshift 20)

4) TimeBetSnapshot = 1.06278 (I think this corresponds to 50 snapshots between redshift 20 and 0, according to my previous post, but I will check this)

## Results

I did end up with 50 snapshots, so I think I did interpret the parameter TimeBetSnapshot correctly (yay!). The files are each 58.7 Mb, so I assume $$2048^3$$ particles will have snapshots that are $$~.25$$ Tb each


Here is a rough animation of the simulation (Note to self: I used the command "ffmpeg -f image2 -r 10 -i snapshot_%03d.png -vcodec mpeg4 -y wfirst128.mp4"):

<video src="{{site.baseurl}}/assets/videos/wfirst128_2.mp4" width="500" height="500" controls>
</video>


And then if I run AHF and plot the halo mass function at redshift zero:


<img src="{{ site.baseurl }}/assets/plots/HMF_wfirst128.png">

This looks decent, but I am wondering why (1) the simulation is slightly above the expected line and (2) why it doesn't look incomplete at low masses (see, e.g., <a href="https://ndrakos.github.io/blog/mocks/Halo_Mass_Function_Continued/">this post</a> for comparison)



## Conclusions

Overall this looks pretty good. I want to get this running on Pleiades, then do a $$1024^3$$ run. Once I'm happy, I'll submit the $$2048^3$$ job.
