---
layout: post
title:  "Testing ICs in Gadget"
date:   2022-09-02
categories: neutrinos
---

My overall goal for this project is to write ICs that have <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_ICs_Background/">stable massive neutrinos</a>, using the method outlined <a href="https://ndrakos.github.io/blog/neutrinos/Neutrino_IC_Method_Overview/">here</a>. In a <a href="https://ndrakos.github.io/blog/neutrinos/Writing_my_own_IC_Code/"> previous post</a>, I went through how to make my own initial conditions, rather than altering existing code. I wrote code to do this for DM particles, and with the previous work I've done sorting out how to treat neutrinos, it should be trivial to add them after.

The goal of this post is to write the dark matter particles in the current code to Gadget files, and test that the initial conditions are set up correctly (i.e. the power spectrum evolves as expected). Once this is verified, I will add in my code for neutrino particles.

## Current Code

I went through how to write this code in <a href="https://ndrakos.github.io/blog/neutrinos/Writing_my_own_IC_Code/">this post</a>. Here is the current code, with some minor updates/corrections:

<object width="500" height="200" type="text/plain" data="{{site.baseurl}}/assets/files/IC_Code.txt" border="0" >
</object>


## Writing Gadget Output Files

I'm going to run this through Gadget to test my ICs. First, I need to write an output file. 


## Running in Gadget

## Testing the Output
