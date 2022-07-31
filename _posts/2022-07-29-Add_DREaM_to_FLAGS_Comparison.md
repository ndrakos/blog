---
layout: post
title:  "Add DREaM to FLAGS Comparison"
date:   2022-07-29
categories: cosmos_web
---


Stephen Wilkins has assembling a First Light and Assembly of Galaxies (FLAGS) comparison dataset in his
<a href="https://github.com/stephenmwilkins/flags_data">github</a> repo. I am going to upload my DREaM predictions as well.

It will be interesting to see how my model compares to the others, and whether JWST data will be able to distinguish between them! There are already some comparisons to DREaM in <a href="https://ui.adsabs.harvard.edu/abs/2022arXiv220710920W/abstract">Wilkins et al. 2022</a>.

## Adding to Github

Here is a quick review for myself on how to contribute to git projects:

1. Fork the GitHub repo, you get the fork in your GitHub account
2. Clone your fork
3. Commit into your local repo
4. Push to your fork
5. Create pull request from your fork


## Data Storage

The data is stored in an <a ref="https://docs.astropy.org/en/stable/api/astropy.io.ascii.Ecsv.html">astropy escv</a> format

For e.g. the LF, I can add a <code>dream.escv</code> file to flags_data/data/DistributionFunctions/LUV/models/binned



## Comparisons on Repo

The following are folders that are already on the repo, and which ones I can easily add to

### Distribution Functions

1. Intrinsic LUV

I do not have the intrinsic (unattenuated) M_UV values in the original DREaM paper (though I calculated these for the reionization project I am working on!).Therefore I'll just skip this for now.

2. LUV

The UV Luminosity functions are in my original DREaM paper, Fig 12.

I have them stored in redshift bins [1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8], [8,9], [9,10], in units N/mag/Mpc^3.

It looks like I can just calculate this the same way, but I'll use z~4, 5, 6, 7, 8, 9, 10.


3. MStar

This is again something I calculated (DREam paper, Fig 6.).

This is calculated almost exactly the same as the LUV. I'll rerun this code, using z~4, 5, 6, 7, 8, 9, 10.


4. SFR

I didn't calculate this before, but it would be easy to add. I'm going to skip it for now though.

### Scaling Relations

I am not going to add data to these for now, but here are my initial thoughts on whether it would be easy to add later.

1. LUV--beta

- I have calculated this for the DREaM catalog (Fig 11)
- Not anything else about this in the FLAG repo yet.

2. LUV--RUV

- I'm not sure what RUV is (maybe size?)
- Not anything else about this in the FLAG repo yet.

3. Mstar--age

- I have calculated an age for the DREaM catalogs, but not sure if it is defined the same

4. Mstar--Rstar

- I'm not sure what Rstar is
- Not anything else about this in the FLAG repo yet.

5. Mstar--SFR

- I have this (Fig 25 in DREaM). I would need to make sure it is defined the same

6. Mstar--sSFR

- I have this (Fig 25 in DREaM). I would need to make sure it is defined the same

7. Mstar--Zgas

- Fig 27 in DREaM. I have set the gas and stellar metallicity to be equal


8. Mstar--Zgas_young

- I'm not sure what this is

9. Mstar--Zstar

- Fig 27 in DREaM. I have set the gas and stellar metallicity to be equal
