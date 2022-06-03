---
layout: post
title:  "A Closer Look at the Double Hernquist Model"
date:   2022-06-02
categories: tidal_stripping
---

Bradley's project involves analyzing tidal stripping in two-component systems.

I had run a test simulation for him with double Hernquist profile, (<a href="https://ndrakos.github.io/blog/tidal_stripping/Two_Component_System/">see this post</a>).

When analyzing it, he was finding that there was very little bound mass---larger than appeared reasonable given the way the simulation looked. In this post I'm going to figure out what's going on, and make sure there is nothing funky with the test simulation I gave him.

## Double checking the IC calculation

I had checked the IC stability <a href="https://ndrakos.github.io/blog/tidal_stripping/Two_Component_System/">previously</a>, and the IC's looked good to me. However, it is worth looking into a little closer, especially because this is the method I plan on using to generate the ICs we will actually use.


Brant pointed out the paper by Ciotti (<a href="">Ciotti 1996</a>) that derives the distribution function for a double Hernquist profile.

Their equation for the DF of a i-th component system (their Eq. 2) agrees with mine:

$$f_i(\mathcal{E})=\dfrac{1}{\sqrt{8}\pi^2}\left[ \int_{r_{\mathcal{E}}}^\infty \dfrac{1}{\sqrt{\mathcal{E}- \Psi}}\dfrac{d^2 \rho_i}{d \Psi^2} \dfrac{GM}{r^2} dr \right]$$

so this is a good sanity check that my methods make sense!


## Sim 1

Here I am going to analyze the test simulation I had given Bradley (<a href="https://ndrakos.github.io/blog/tidal_stripping/Two_Component_System/">here</a>), and see if I can sort out what is happening.

At first the code I have wasn't working to find the bound remnant. After a couple checks, I realized the velocity frame was constant (which it shouldn't be).

To get the analysis to work, I had to slightly change my algorithm for finding the frame of the satellite. Here is the current algorithm (where I have added step 3)
1. take all particles bound in the previous snapshot
2. find the frame in x,y,z space (by finding highest density point)
3. only consider particles within r<10 of this frame (algorithm seems to be insensitive to what I choose for r)
4. find the velocity frame, (vx,vy,vz), using the same algorithm as Step 2
5. subtract off the frame off all particles in the snapshot
6. find the bound particles (considering all particles in the snapshot) by iterative method

Here are the results:

<video src="{{site.baseurl}}/assets/videos/Sim1.mp4" width="500" height="500" controls>
</video>

This is the same result that Bradley got.

Comparing the density profile in the frame of the satellite with all particles and with just the bound particles, it looks like the frame is correct, but a lot of the mass is not actually "bound". I played around with the algorithm, and it doesn't make any difference, so I think that this is not numerical in origin.

Maybe my way of defining a self-bound remnant doesn't work very well in this extreme case, where the profile is very extended; note that more than 90 per cent of the mass is in the extended orange system! Potentially, there is a correction that could be made  by including a background potential when calculating each particles energies. Also note I am assuming the satellite potential is roughly spherical, which I have found works very well in the past; but maybe it fails here. This idea of deciding which particles are bound is an interesting one, and one I might look into in the future, but for now it doesn't seem worth our time, since these aren't the final simulations we will use.


## Sim 2

I ran this simulation, but put the ICs at an initial distance of r=1000 instead of r=100. I also decreased this initial velocity by a factor of $$\sqrt{3}$$. This should give it a much smaller tidal field. I will also give it slightly more initial velocity ($$v_0=5$$)

<video src="{{site.baseurl}}/assets/videos/Sim2.mp4" width="500" height="500" controls>
</video>

Since the orbital time is much longer than Sim 1, this will take a longer time to pass through an orbit. Its probably not worth testing further.


# Sim 3

I ran a third simulation, with the same initial position/velocity as Sim 1, where the two components are more similar in mass/size (the second component has 2 times the mass, and is 10 times as extended as the first).


<video src="{{site.baseurl}}/assets/videos/Sim3.mp4" width="500" height="500" controls>
</video>

This looks a lot easier to work with. One thing that is a little strange is that it seems to calculate the bound mass in some snapshots better than others. I did not pre-calculate the orbital time when setting the snapshot output times, so we will need to figure out what snapshots are approximately at apocenter to run the analysis. But these are probably easier to work with than Sim 1!


## Conclusions

The bound mass was easier to track in S3, but I am still interested in why the density profile with all particles looks like there should be more mass. I think this probably has something to do with the profiles, which makes my current algorithms not robust. I don't want to waste a lot of time looking into the problem, if it will go away with the new profile.

1. Bradley can take a look at Sim 3, and see if it is easier to see what is happening in energy space.

2. I need to write the IC code for the more complicated profiles (see <a href="https://ndrakos.github.io/blog/tidal_stripping/General_model_for_two-component_satellite/">this post</a> for my plan for these). I am pretty convinced my method for creating ICs is working alright, so I just need to do so for the more complicated distribution functions. Once I have a fiducial case working for this, we can check to see if we run into the same problem. If we do, we will need to dig into it more to figure out what is happening.
