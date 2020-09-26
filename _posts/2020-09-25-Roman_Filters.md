---
layout: post
title:  "Roman Filters"
date:   2020-09-25
categories: mocks
---

I outlined a method for calculating whether or not a galaxy was detected in <a href="https://ndrakos.github.io/blog/mocks/Galaxy_Detection/">this post</a>.

Here I am going to update this
(1) include the correct filters
(2) change the criteria for detection

## Adding Filters to FSPS

According to the FSPS documentation:

***There are three things the user must do: 1) modify the nbands parameter in the sps vars.f90 routine; 2) add the filter to the allfilters.dat file located in the data directory. Follow the format: there must be a line starting with a # sign, followed by two columns, the first being the wavelength in angstroms, the second being the total throughput. The filter can be of any resolution, and need not be properly normalized. 3) The user would be wise to add details of the filter to the FILTER LIST file located in the data directory, although this is not, strictly speaking, necessary for proper functioning of the code.***

Brant gave me filter information, from which I could calculate the transmission. I did this, and followed the instructions above.

I then reran "make" in the fsps src directory. Then need to reinstall python package.
(I also commented out the warning "redshift is different than 'zred'" in fsps.py because I want to specify z=0 to get magnitudes for the $$\beta$$ calculation)


## Detection Critera

To determine whether an object is detected, we should use the band that is one redder than the band the lyman alpha line is detected in.

For every filter, I assigned a non-overlapping wavelength range (the dividing point was taken to be halfway between the centers of two adjacent bands), and then found the corresponding redshift range in that band for the lyman alpha line (using $$\lambda =1216(1+z)$$). The redshift range for detection is then the redshift range of the band immediately bluer to that band.

Here is the redshift range for each band:

|Filter|$$\lambda$$ range| $$z$$ range detection|
|------|------           |------                |
| R062 | (600,7445)      | (0,3.9)|
| Z087 | (74445,9645)    |(3.9,5.1)|
| Y106 | (9645,11765)    | (5.1,6.9)|
| J129 | (11765,14350)   | (6.9,8.7)|
| H158 | (14350,17095)   | (8.7,10.8)|
| F184 | (17095,20000)   |  (10.8,13)|
