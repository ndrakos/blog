---
layout: post
title:  "Limiting Magnitudes"
date:   2020-09-11
categories: mocks
---

Here I am calculating the limiting magnitude in each band in Roman Telescope for a potential Ultra Deep Field Survey.


## Limiting magnitude


I found <a href="https://faculty.virginia.edu/rwoclass/astr511/lec14-f03.pdf
">this link</a> useful in describing magnitude systems.


The AB magnitude limit of a potential UDF is $$m_{AB} \simto 30$$, which corresponds to $$f_{\nu} = 3.631 \times 10^{-9} \rm{Jy}$$. Therefore, the limiting magnitude of each

$$m_{i} = -2.5 \log_{10} \dfrac{3.631 \times 10^{-9} \rm{Jy}}{Q_i} $$,

where $$Q_i$$ is the zero point of each filter.


<a href="http://svo2.cab.inta-csic.es/svo/theory/fps3/index.php?mode=browse&gname=WFIRST&asttype=
">This site</a> has a summary of WFIRST filters and their zero points.


Therefore, here is the limiting magnitude in each of these bands, assuming the AB magnitude limit is $$m_{AB} \simto 30$$.


|Filter|ZP_{\nu} (Jy)|Limiting Magnitude|
|------|-------------|-------|
| R062 | 3022.34     | 29.80|
| Z087 | 2298.31     | 29.50|
| Y106 | 1962.64     | 29.33|
| J129 | 1479.84     | 29.03|
| Prism| 1388.79     | 28.96|
| Grism| 1207.17     | 28.80|
| W146 | 1174.09     | 28.77|
| H158 | 1090.69	   | 28.69|
| F184 | 863.33      | 28.44|




## As a function of redshift

Converting this to an absolute magnitude, as a function of distance, we can see the magnitude we will be able to detect in each filter.

$$M = m- 5 \log_{10}(D_L(z)/(\sqrt{1+z} 10 {\rm pc}))$$. Here I have an extra factor of (1+z) to account for the fact that the object has been redshifted, which I didn't include in <a href="https://ndrakos.github.io/blog/mocks/Mass_Resolution/">this post</a>.. **I'm really not sure this is correct... Does this assume the spectrum of the object is flat?**

Here is the plot I get for magnitude limits in each filter:


<img src="{{ site.baseurl }}/assets/plots/20200911_MagvsRedshift.png">
