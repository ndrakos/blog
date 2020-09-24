---
layout: post
title:  "Galaxy Detection"
date:   2020-09-24
categories: mocks
---

Once I have SEDs for each galaxy, I want to determine whether they will be detected.

## Method from Williams et al. 2018

In W18, they say an object is "detected" if it is brighter than the 5$$\sigma$$ limits in two photometric bands corresponding to the rest frame UV.


To choose the photometric bands, they take (1) the band that is closest to 1500A, and then (2) the nearest band at a longer wavelength.

For the JADES survey, this corresponds to filters
- F115W, F150W for reshifts 6-7
- F150W, F200W for reshifts 7-9.6
- F200W, F277W for reshifts 9.6-13


## Roman Filters

There should be 5$$\sigma$$ detection around magnitude of $$m_{\rm AB} \approx 30$$, as shown in this table from Koekemoer et al:

<img src="{{ site.baseurl }}/assets/plots/20200924_filters.png">

Note the different exposure times; in <a href="https://ndrakos.github.io/blog/mocks/Limiting_Magnitudes/">this post</a> I calculated the relative filter depths at the same exposure time.


For each of these filters, we can determine the redshift at which the observed wavelength corresponds to 1500$$\AA$$ (using $$z=(\lambda_{obs}-\lambda_{rest})/\lambda_{rest}$$)


|Filter|Center|Redshift|
|------|------|------|
| R062 | 6200| 3.13|
| Z087 | 8690| 4.80|
| Y106 | 10600| 6.07|
| J129 | 12930| 7.62|
| H158 | 15770| 9.51|
| F184 | 18420 | 11.28|

Therefore, I will use the two filters that bracket each object; e.g. for an object at redshift 8, I will use filters J129 and H158.

If the apparent magnitude in **both** bands is above $$30$$, I will consider it detected.


## Calculating in FSPS

FSPS includes many filters, as listed <a href="http://dfm.io/python-fsps/current/filters/">here</a>. It does not currently include the RST filters. For now I will use [sdss_r, wfcam_z, wfcam_y, wfcam_k, wfcam_h, wfc3_ir_f160w, jwst_f200w], because they are roughly similar, but I will add in the proper filters soon.

In FSPS you can use <code>get_mags</code> to get magnitudes in different filters. Since the sps object has been normalized such that the total stellar mass created in the history of the star formation is $$1$$ solar mass, the flux has to be multiplied by the $$M/x$$, where $$x$$ is the stellar mass surviving at the current redshift (from <code>stellar_mass</code>);  i.e., you can calculate the magnitude as

<code> m = sps.get_mags(tage=mytage,bands=filter_list) - 2.5*log10(M/sps.stellar_mass) <code>
