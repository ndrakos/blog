---
layout: post
title:  "SED Pipeline Quiescent Galaxies"
date:   2021-05-10
categories: mocks
---


As described previously, I now have a working method to assign SEDs to the galaxies in the mock catalog that reproduces the $$\beta$--$M_{\rm UV}$$ relation, the $$M_{\rm UV}$$--mass relation, the $$SFR$$--mass relation, the fundamental metallicity relation and the metallicity--$$\log U_S$$ relation.

However, it is not working well for the quiescent galaxy assignment. Here is a summary of the current status.

## Current Method

Here is the SED assignment pipeline:

<img src="{{ site.baseurl }}/assets/plots/20210510_SED_Pipeline.png">

The assigned SEDs are sensitive to the parent catalogs as well as the distance metrics. These tables summarize how the different parameters are selected:

<img src="{{ site.baseurl }}/assets/plots/20210510_TableSFGs.png">

<img src="{{ site.baseurl }}/assets/plots/20210510_TableQGs.png">


## Results

As shown previously, this does a very good job at reproducing the MUV and beta trends in the SFGs

<img src="{{ site.baseurl }}/assets/plots/20210510_MUV.png">

However, there are some issues with the QGs. First, the SFR--mass relation does not match for QGs, except at low redshifts:

<img src="{{ site.baseurl }}/assets/plots/20210510_SFR_vs_M.png">

and the UVJ diagram doesn't look right either:

<img src="{{ site.baseurl }}/assets/plots/20210510_UVJ.png">


The SFRs should be correct by construction, so this should be fixable. Hopefully fixing the SFRs will also help with the UVJ diagram. If not, I could potentially try and constrain the U-V colors as well (right now I have 2 free parameters (age and tau), and am only trying to constrain the SFR).

There are two possible things that could improve this (1) sample the parent catalog better or (2) make sure that my metric for assigning nearest neighbours is right. I am going to look into these both in a bit more detail.

## Parent Catalogs

First, here is a comparison of the parameter space spanned by the SFGs and the QGs in the assigned SEDs compared to the parent catalog. These both look pretty good.


<img src="{{ site.baseurl }}/assets/plots/20210510_triangle_plot_SF.png">

<img src="{{ site.baseurl }}/assets/plots/20210510_triangle_plot_Q.png">



## Distance Metrics

I also looked a bit closer into how well the assigned parameters are matching the proposed parameters:

<img src="{{ site.baseurl }}/assets/plots/20210510_test_tree_SFGs.png">

<img src="{{ site.baseurl }}/assets/plots/20210510_test_tree_QGs.png">

The biggest problem seems to be that the nearest neighbours are favouring lower redshift galaxies for the QGs. Therefore, I should change the distance metric I am using for the redshifts to ensure that I am considering galaxies near in redshift.
