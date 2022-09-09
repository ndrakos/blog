---
layout: post
title:  "Neutrino Velocities for MUSIC"
date:   2022-03-18
categories: neutrinos
---

As outlined in <a href="https://ndrakos.github.io/blog/iso_ics/Neutrino_IC_Method_Overview/">this post</a>, I am planning to modify MUSIC to contain neutrinos using the method from <a href="https://ui.adsabs.harvard.edu/abs/2018JCAP...09..028B/abstract">Banjeree et al. 2018</a>.

In the <a href="https://ndrakos.github.io/blog/neutrinos/MUSIC_code_breakdown/">previous post</a> I went through the main part of the MUSIC code, to understand the structure, and where the changes need to be implemented.

In this post, I am going to write the code to assign velocity to the particles. I did this in a <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_Velocity_Assignment_Test/">previous post</a> in python, but now I want to write it in a form that will be incorporated into MUSIC. This will be a bit slow going, because MUSIC is very object-oriented, which I haven't coded much in, and I am rusty in C++!


## In MUSIC


**Velocity calculations:** The velocity calculations are done in <code>main.cc</code>, but using functionality from other files (e.g. <code>poisson.cc</code>)

**Velocity data type:** Velocities are stored in a variable <code>data\_forIO</code>, which is type  <code>grid_hierarchy</code>; <code>grid_hierarchy</code> is the type of the <code>GridHierarchy</code> class, which is defined in <code>mesh.hh</code>.

**Writing out velocities:** The <code>write_dm_velocity</code> function takes in two arguments: <code>icoord</code> and  <code>data\_forIO</code>. The first,  <code>icoord</code>, is simply an integer (0,1,2) corresponding to the (x,y,z) coordinates.



## My Code Structure

What I want to do is create two files <code>neutrino.cc</code> and <code>neutrino.hh</code> that will contain all the functionality needed for neutrinos. I'll try and structure this similar to <code>poisson.cc</code>, but a bit simpler; e.g. the MUSIC headers define a bunch of different kinds of "plug-ins", that I don't really understand, and don't think its worth it to dive into. Remember, the end goal is to put this in the new Cholla ICs, so I just want to get this working to test if the methodology works!
