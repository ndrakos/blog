---
layout: post
title:  "Galaxy Sizes Part III"
date:   2021-03-02
categories: mocks
---

The method I am using to assign galaxy sizes is outlined <a href="https://ndrakos.github.io/blog/mocks/Galaxy_Sizes_Part_II/">here</a>.

I am using the relation:

$$R_{\rm eff} = A R_{\rm vir}$$

with the coefficients from <a href="https://ui.adsabs.harvard.edu/abs/2020MNRAS.492.1671Z/abstract">Zanisi et al 2020</a>, calibrated at redshift zero.

The coefficient may very well have a $$z$$ dependance. In particular, the evolution of $$R_{\rm eff}$$ with fixed stellar mass depends on whether a galaxy is star-forming or quiescent (e.g. <a href="https://ui.adsabs.harvard.edu/abs/2014ApJ...788...28V/abstract">van der Wel et al. 2014</a>, <a href="https://ui.adsabs.harvard.edu/abs/2018MNRAS.477..219M/abstract">Ma et al. 2018</a>), but for now I am assuming that there is no dependance. In this post I will compare the results from my catalog to data and decide whether it needs to be updated.




## Size Definitions

One thing to be careful about is the radius definitions

### Projected vs 3D

In all the measurements, assuming projected shapes. There is some discussion of this in Z20.


### Major axis vs circular axis

There are two common radius definitions (1) $$R_{\rm eff, maj}$$ which is the half-light radius in the semi-major axis and (2) $$R_{\rm eff, circ}$$  which is the circularized half-light radius.

You can convert between the two using:
$$R_{\rm eff, circ} = \sqrt{b/a} R_{\rm eff, maj}$$
where $$b/a$$ is the projected shape ratio.

The  $$R_{\rm eff, maj}$$ definition is what is used in Z20 and W18, so it is what I will generally to use; however, I will try and be explicit.




### Physical vs Co-moving

Finally, just a note that the halo catalogs return $$R_{\rm vir}$$ in co-moving co-ordinates, in units of kpc/h. This needs to be changed to physical units.



## Data Set

For comparison, I am using the data from <a href="https://ui.adsabs.harvard.edu/abs/2015ApJS..219...15S/abstract">Shibuya et al. 2015</a>

<!---
https://ui.adsabs.harvard.edu/abs/2019ApJ...872L..13M/abstract
https://ui.adsabs.harvard.edu/abs/2019ApJ...880...57M/abstract
https://ui.adsabs.harvard.edu/abs/2021MNRAS.501.1028Y/abstract
-->

### Low Redshift Sample


176,152 photo-z galaxies from redshfits $$z = 0–6$$ from the 3D-HST+CANDELS catalog.

The sizes $$R_{\rm eff}$$ are in Table 4 of Shibuya et al. These are either UV or Opt, but I am going to combine these (by taking the mean when both are available). The sizes are in arcsec so have to be converted to kpc by dividing by the angular diameter distance.

Redshifts and masses are from Skelton et al. 2014; data can be downloaded <a href="https://archive.stsci.edu/prepds/3d-hst/">here</a>.

The galaxies are classify as star-forming or quiescent using UVJ criteria for galaxies with redshifts $$z<4$$. Presumably I could do this with the information from Skelton et al. I will add this on later; for now I am considering everything star-forming.



### High Redshift Sample

10,454 Lyman break galaxies (LBGs) at $$z = 4–10$$ identified in the Cosmic Assembly Near-infrared Deep Extragalactic Legacy Survey (CANDELS), HUDF 09/12, and HFF parallel field.

The sizes are listed in Table 5 of Shibuya et. al. The rough redshifts are in the ID, and depend on colour criteria. The IDs correspond to <a href="https://ui.adsabs.harvard.edu/abs/2016ApJ...821..123H/abstract"> Harikane et al. 2016</a>.

Masses from mass---$$M_{\rm UV}$$ relation in Equations 58-60 in Harikane et al. The $$M_{\rm UV}$$ values are also in Table 5 of Shibuya et al.

In Shibuya, they argue that you can assume these are all star-forming since the quiescent fraction should be low, so I will do the same.



## Results

<img src="{{ site.baseurl }}/assets/plots/20210302_Reff.png">


<!---
Re versus M relation (shen2003, bernardi2014,lange2015)???
-->
