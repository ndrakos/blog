---
layout: post
title:  "FSPS Parameters"
date:   2020-09-09
categories: mocks
---

This post is on choosing the parameters in FSPS.


## Parameters

There are a large number of possible parameters that can be changed. Most will be left to their default values:

<object width="500" height="1000" type="text/plain" data="{{site.baseurl}}/assets/files/FSPS_params.txt" border="0" >
</object>



## My Choice of Models/Parameters

The redshift of each galaxy, <code>zred</code> is known.

The age of the galaxy (in Gyr), <code>tage</code> can be varied. I think this is the age since the start of star formation. This is something I will treat as a free parameter.

add_stellar_remnants?
igm_factor? (igm_absorption)



### Initial Mass Function

The options for the initial mass functions (IMFs) are Salpeter, Chabrier, Kroupa, van Dokkum, Dave or your own tabulated IMF. For now I will use a Chabrier 2003 IMF (<code>imf_type=1</code>), because that was what was used in Williams et al.



### Metallicity

<code>zcontinuous</code> specifies how the interpolation in metallicity is done. I will use the option $$1$$, in which the SSPs are interpolated to the value of <code>logzsol</code> before the spectra and magnitudes are computed.

The metallicity of each galaxy is then controlled by the parameter <code>logzsol</code>, which gives the metallicity in units of $$\log(Z/Z_\odot)$$

### Star Formation History

I'm going to use a delayed tau model.

The code has a delayed six parameter tau model (<code>sfh=4</code>), that has a tau model plus a constant component and a burst; I will leave the parameters that control the constant and burst components off.

The parameters are:

<code>tau</code>: e-folding time in Gyr. Range is $$0.1 <\tau <10^2$$.

<code>sf_start</code>: start time of SFH, in Gyr. (is this the age of the universe? maybe I should just leave this to zero?)

<code>sf_trunc</code>: truncation time of SFH, in Gyr. Can I use this to control whether a galaxy is quiescent?



### Dust Model


The dust absorption follows Charlot & Fall (2000). Dust emission follows Draine & Li (2007). I included the circumstellar dust models calibrated from DUSTY, but not the dust emission associated with an AGN torus.

I will use <code>dust_type=2</code> for the extinction curve for now, as it seems to be the simplest. This uses the Calzetti et al. (2000) attenuation curve, where dust attenuation is applied to all starlight equally (not split by age), and therefore the only relevant parameter is <code>dust2</code>, which sets the overall normalization (but you must also set  <code>dust1=0.0</code> for this to work correctly).


## Nebular Emission

I will turn on the nebular emission model (<code>add_neb_emission=True</code>)
(also include the nebular continuum, which it will do by default).

The nebular emission is controleld by the gas ionization parameter <code>gas_logu</code>, and the gas metallicity, <code>gas_logz</code>. As in Williams et al., I will approxiate the stellar and ISM metallicities as a single metallicity value ($$Z_{ISM} = Z$$)

## Free Parameters

From this post, the parameters that will vary between each galaxy are...

<code>zred</code>

<code>tage</code>

<code>logzsol</code>

<code>tau</code>

<code>sf_start</code>

<code>sf_trunc</code>

<code>dust2</code>

<code>gas_logu</code>

<code>gas_logz</code>

Next, I will look into how these effect the properties I want to match (e.g. mass, UV magnitude, UV continuum slope)
