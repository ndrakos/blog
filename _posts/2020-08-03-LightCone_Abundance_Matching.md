---
layout: post
title:  "Light Cone Abundance Matching"
date:   2020-08-03
categories: mocks
---

I have done abundance matching on the $$512^3$$ simulation light cone to assign galaxy masses to each halo. There are still some things to sort out, but these are my preliminary results.

## Results

The theoretical curves are given with dashed lines (when known) and the data with solid lines; the shaded area gives the  $$1\, \sigma$$ error bars:


<img src="{{ site.baseurl }}/assets/plots/20200803_AbundanceMatching.png">


### Stellar Mass Function

The scatter method I am using should preserve the SMF exactly, which is why there is excellent agreement between the theoretical SMF and the light cone SMF. The SMF seems to be a little high for low redshifts; this may be because of the low volume in this redshift range, but the error bars don't seem to agree with this... I need to double check that things make sense for this range.

Another thing to think about is whether the shape of these SMFs is reasonable, particularly for high redshifts. The form is from <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>. Here is their plot with data:

<img src="{{ site.baseurl }}/assets/plots/20200803_WilliamsSMF.png">

There doesn't seem to be good evidence for the high redshift SMFs, so maybe I should alter this.

### Halo Vpeak Function

The second panel shows the HVFs measured from the simulations compared to the fit I have for the HVFs. Right now the high redshifts don't agree in the abundance matching procedure, but that's because I only fit the parameterization out to redshift $$7.4$$: see below:

<img src="{{ site.baseurl }}/assets/plots/20200803_HVF.png">

I need to update these fits, and extend them to higher redshifts.


### Stellar Mass--Vpeak Relation

The third panel shows the relation between the galaxy masses and the halo $$v_{\rm peak}$$ values.

Galaxy masses are a little higher than expected at low vpeaks... see for example this plot from <a href="https://ui.adsabs.harvard.edu/abs/2019arXiv191003605C/abstract">Cao et al. 2019</a>:

<img src="{{ site.baseurl }}/assets/plots/20200511_Cao2019.png">

This could be partially because we are using a different SMF, but it is probably mostly because we aren't resolving enough lower mass haloes; really shouldn't trust the shape below $$\log_{10}(V_{\rm peak}) = 2.2\,{\rm dex}$$. This will improve with the higher resolution simulations.



### Stellar Mass--Halo Mass Function

Finally, the last panel shows the stellar mass--halo mass relation.I want to check if these relations look reasonable. To do this, I'm going to compare to this paper: <a href="https://ui.adsabs.harvard.edu/abs/2020A%26A...634A.135G/abstract">Girelli et al. 2020</a>.



## Scatter

To get the scatter in this relation, I roughly used the scatter mapping for redshift 0 (since I am having issues getting it to work for higher redshifts). I set it up so that it should give a scatter $$\sigma [M_{\rm gal}\rvert V_{\rm peak}]=0.2\, \rm{dex}$$.

With the current plots, I have the following scatter:

<img src="{{ site.baseurl }}/assets/plots/20200803_SMHM_Scatter.png">

Clearly, this isn't constant at 0.2 as I tried to implement. However, I really only roughly estimated the mapping between $$V_{\rm peak} = 2.1$$ and $$2.8$$ for redshift zero.

If we compare to current constaints on

<img src="{{ site.baseurl }}/assets/plots/20200213_Cao2019.png">

Not only is my method for putting scatter on $$V_{\rm peak}$$ not completely working, it also isn't clear (1) how this will relate to scatter in the SMHM relation and (2) what scatter we want. I really want to sort out this step to get this section of the methods done. After assigning galaxy masses, the next step will be to assign galaxy properties.



## To-Do

**SMF**

(1) Do we want to update/change the Williams SMF parameterizations?

(2) Is there somthing off with the recovered SMFs at low redshifts?

**HVF**

(3) Update the HVF to agree for higher redshifts.

**Scatter Mapping**

(4) Decide what scatter I want... right now I am setting it to $$\sigma [M_{\rm gal}\rvert V_{\rm peak}]=0.2\, \rm{dex}$$.

(5) Get my procedure for scatter working for all redshifts.

**SMHM Relation**

(6) Compare these results to the literature, to check that this looks reasonable.

**Other**

(7) Check that the clustering and/or bias look right.
