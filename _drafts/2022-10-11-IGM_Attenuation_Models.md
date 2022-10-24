---
layout: post
title:  "IGM Attenuation Models"
date:   2022-10-24
categories: cosmos_web
---

One thing I am interested in is how the environment effects luminosity of galaxies. As shown in <a href="https://ndrakos.github.io/blog/cosmos_web/LF_Environmental_Dependance/">this post</a>, there is significant different in the LF of galaxies in dense environments compared to galaxies in less dense environments. One thing I want to know is whether this will show a different signature depending on models during the EoR. Dense galaxies likely live in reionization bubbles at high redshifts, which will show signatures on their observed spectra. What does this look like? Is it obvious in certain JWST filters? Is this something that is measurable?

## Sample Spectra

Here is what an example DREaM spectra looks like, and the COSMOS-Web bands.

<img src="{{ site.baseurl }}/assets/plots/20220914_SEDs.png">


## IGM Absorption (FSPS)

FSPS includes a IGM absorption model from Madau (1995), and this is what I used in the DREaM galaxies (<a href="https://github.com/cconroy20/fsps/blob/master/src/igm_absorb.f90">source code</a>).

I generated a spectra with FSPS at redshifts 6,7,8,9 and 10 and looked to see how it changed with (solid lines) and without (dashed lines) the IGM absorption model.

<img src="{{ site.baseurl }}/assets/plots/20220914_AttenuationModel.png">


Here are the magnitudes with/without IGM Attenuation.

| Redshift   | F115W | F150W | F277W | F444W | F770W |
| ----------- | ----------- |
|6      |25.18/25.18     |25.10/25.10    |24.58/24.58     |24.08/24.08     |23.86/23.86     |
|7      |25.27/25.27     |25.19/25.19    |24.64/24.64     |24.12/24.12     |23.98/23.98     |
|8      |25.57/25.11     |25.26/25.26    |25.07/25.07     |24.36/24.36     |24.15/24.15     |
|9      |26.42/25.22     |25.31/25.31    |25.15/25.15     |24.34/24.34     |24.35/ 24.35    |
|10     |36.57/25.89     |25.24/25.14    |25.21/25.21     |24.80/24.80     |23.54 23.54     |

Here it looks like this signal will really only show up in F115W at redshifts ~9 and higher. Some of the bluer filters might be able to pick up differences in galaxies at lower redshifts.



## Where to Go Next

### Key questions
1. Bright End of the LF
- How well will COSMOS-Web measure the high-redshift bright-end of the LF?
- What are current predictions/measurements of what the bright end of the LF should look like?
2. Environmental Differences in LF
- How does the LF depend on environment?
- Will COSMOS-Web be able to measure this?
- What does this mean for our understanding of galaxy formation?
3. How does the EoR factor into this?
- Does the IGM model effect the measured LF (this post - maybe? shouldn't effect the UV LF, but perhaps it effects the LF in different filters? Or is this just a source of error in SED fitting?)
- How can I implement more complicated IGM models? How do I get these to depend on environment (e.g. whether they are in a reionized bubble).
- Can we use LF variation in different environments to constrain the EoR? With COSMOS-Web?

### To-Do
I think I need to write myself a little review on the UVLF, and get an idea of how this should vary/what people have done so far.

1. Question 1 should be straightforward to put together (and is probably already partially in the COSMOS-Web review paper).
2. I have already looked at environmental changes in the LF with the DREaM catalog. I need to think about this in the context of COSMOS-Web, and see if there is a straightforward way to change predictions here. Is this mainly related to my abundance matching algorithm?
3. This will be a more difficult thing to look into! I think I will assume that we can determine galaxy redshifts perfectly, and see if there is a signal depending on the EoR.
