---
layout: post
title:  "Add Filters to DREaM"
date:   2022-07-28
categories: cosmos_web
---

I want to add more photometry to the DREaM mock catalogs. Currently, DREaM has the NIRCAM wide filters included already. This includes the four COSMOS-Web NIRCAM filters (F115W, F150W, F277W, F444W), but not the MIRI imaging (F770W). Additionally, I have specifically been asked about NIRCAM-F410M, NIRCAM-F430M, and ACS-F814W. However, there are many other filters I could add. <a href="https://cosmos.astro.caltech.edu/page/filterset">This page</a> has a list of all the filters that currently cover the COSMOS field.

My workflow is to add these filters to FSPS (if they don't already exist), regenerate spectra for every galaxy in the catalog, calculate the photometry in the filter, and then save the final catalog.

## NIRCAM Filters

NIRCAM has a total of 29 bandpass filters, as summarized <a href="https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-instrumentation/nircam-filters">here</a>.

Here is a summary of the NIRCAM filters:

<img src="{{ site.baseurl }}/assets/plots/20220728_NIRCAM_filter_table.png">

and a plot of their throughput:

<img src="{{ site.baseurl }}/assets/plots/20220728_nircam_filters.png">


I currently have the wide filters (F070W, F090W, F115W, F150W, F200W, F277W, F356W, F444W), and Steve Wilkins requested the medium filters F410M and F430M for his FLAGS comparison.

The current version of FSPS has the JWST wide filters, but no others. Therefore, I will manually add the 12 medium filters, and ignore the others for now.

## MIRI Filters

MIRI has <a href="https://jwst-docs.stsci.edu/jwst-mid-infrared-instrument/miri-instrumentation/miri-filters-and-dispersers">9 imaging filters</a> (actually 10, but one is redundant):

<img src="{{ site.baseurl }}/assets/plots/20220728_MIRI_filters.png">

I will add all 9 MIRI filters. These are not currently in FSPS, so I will add them manually.



## HST Filters

Here are the HST filters available in the COSMOS field (I pulled this from the COSMOS site):

<img src="{{ site.baseurl }}/assets/plots/20220728_HST_filter_table.png">

One of the most relevant filters for COSMOS-Web will be ACS F814W, as it will help detect galaxies in the EoR. However, I will just add all the filters in the table. These are all currently in FSPS, so it doesn't require much extra work.


## Add Filters to FSPS

I had detailed the instructions for adding FSPS filters in an <a href="https://ndrakos.github.io/blog/mocks/Roman_Filters/">earlier post</a>.

The NIRCAM throughputs were all available on the <a href="https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-instrumentation/nircam-filters">summary site</a>.

The MIRI throughputs were not available on the MIRI page, but I found them with the <a href="https://outerspace.stsci.edu/display/PEN/Pandeia+Engine+Installation">Pandeia Engine "required data"</a>.

This went mostly smoothly. For some reason, the python fsps code does not read in the nbands from the Fortran properly, so I used the manual install of the python code (i.e. not the pip version), and changed the number of bands manually in <code>src/fsps/libfsps/src/sps_vars.f90</code>. Note that you can double check where your python-fsps is installed using "<code>import fsps; fsps.__file__</code>". I got this working on both my computer and lux.

Here is an example spectra, to check the photometry makes sense:

<img src="{{ site.baseurl }}/assets/plots/20220728_SEDs.png">


## New Catalog

Once I added the filter information, I can generate more photometry for the DREaM catalog.

This is done by looping through the galaxies (parallelized in lux), generating spectra using FSPS and the stored spectra parameters, and then calculating the photometry in the new filters using FSPS. With this, I am creating a new catalog called <code>DREaM_photometry</code>. This catalog contains ID, RA, Dec, redshift, M_halo, M_gal, logpsi, the 8 NIRCAM wide filters, the 12 NIRCAM medium filters, the 9 MIRI filters and the 10 HST filters I listed above.

Right now I'm just waiting for this to finish running!
