---
layout: post
title:  "Vpeak Function"
date:   2020-02-25

categories: mocks
---

This is a summary for where we are in the abundance matching procedure:

(1) Halo mass proxy: $$v_{\rm peak}$$

(2) Stellar mass function: I have a parameterized form from <a href="https://ui.adsabs.harvard.edu/abs/2009MNRAS.398.2177L">Li & White 2009</a>, but we will need to update this to a more recent model that extends to higher redshifts, as in <a href="https://ui.adsabs.harvard.edu/abs/2018ApJS..236...33W/abstract"> Williams et al. 2018</a>

(3) Halo $$v_{\rm peak}$$ function: before I had been measuring this from the simulation, but once adding scatter this becomes problematic outside of the range of the data. Also it becomes a problem below the resolution limit of the simulation. In this document I will check a parameterized form.

(4) Scatter model: I am using the method from  <a href="https://ui.adsabs.harvard.edu/abs/2019arXiv191003605C/abstract">Cao et al. 2019</a></li>; I had run into problems before because I couldn't reproduce their $$M_*$$ versus $$v_{\rm peak}$$ plot. In this post I will try this again with the parameterized $$v_{\rm peak}$$ function.



## Halo $$v_{\rm peak}$$ Function

I am using the fit for $$dn/d\ln v_{\rm peak}$$ from  Appendix A of <a href="https://ui.adsabs.harvard.edu/abs/2017MNRAS.469.4157C/abstract">Comparat et al 2017</a>. This function gives fits for both distinct and satellite haloes, for redshifts $$0<z<2.3$$ (note we will need to extend this parameterization to higher redshifts if we want to use it in the abundance matching procedure for the mock catalogues).

The parameterization is (I fixed some typos in their equation):

$$\dfrac{dn}{d \ln v_{\rm peak}} = \dfrac{H(z)}{v_{\rm peak}^3} 10^A \left(1 + \dfrac{v_{\rm peak}}{10^{V_{\rm cut}}} \right)^{-\beta} \exp\left[ \left(\dfrac{v_{\rm peak}}{10^{V_{\rm cut}}} \right)^{-\alpha}\right]$$

where $$A,\beta,\alpha$$ and $$V_{\rm cut}$$ are the fitted parameters. I used $$H(0)=70 km /s/Mpc$$.

Comparing this to the output from the simulation, I get:

<img src="{{ site.baseurl }}/assets/plots/HaloVelocityFunction.png">

as expected, there are resolution problems below $$v_{\rm peak} \approx 2.6$$.



## Halo Mass - Stellar Mass Relation

I can now recover the expected relation between $$M_*$$ and $$V_{\rm peak}$$.

From <a href="https://ui.adsabs.harvard.edu/abs/2019arXiv191003605C/abstract">Cao et al. 2019</a></li>:

<img src="{{ site.baseurl }}/assets/plots/Cao2019_MvsV.png">

Mine:

<img src="{{ site.baseurl }}/assets/plots/Mstar_vs_vpeak_updated.png">

It looks much better! (I also realized I had been missing a factor of $$h^3$$ in the stellar mass function...)




## Scatter Model

And the scatter mapping:

From <a href="https://ui.adsabs.harvard.edu/abs/2019arXiv191003605C/abstract">Cao et al. 2019</a></li>:

<img src="{{ site.baseurl }}/assets/plots/HaloVelocityFunction.png">

For mine I calculated this by doing the abundance matching for 1000 $$v_{\rm peak}$$ values, binning it into 100 bins, and calculating the standard deviation in each. Then I repeated this 1000 times and averaged it to get a smoother relation.

<img src="{{ site.baseurl }}/assets/plots/scatter_mapping_updated.png">

This is a lot better, but still doesn't match. I will look into this more another day, but for now it seems to be roughly working.





## Next In This Project
Now the abundance matching procedure is pretty much ironed out (with the exception of the scatter mapping), at least at $$z=0$$. I will finish fixing this, and check that the abundance matching results in the proper stellar mass function with the appropriate scatter.

Then, the next thing I am going to focus on is making a light cone. This will also help us determine what we need for the dark matter only simulation.
