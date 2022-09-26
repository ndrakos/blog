---
layout: post
title:  "Neutrino Summary"
date:   2022-09-23
categories: neutrinos
---

I fixed a couple of problems in my Neutrino code, so I am including the current code here.

Some things of note:
- Gadget does not use peculiar velocities, but uses $$v/\sqrt(a)$$.
- <code>camb.get_matter_power_interpolator</code> by default only goes to redshifts 10. You need to pass an extra argument to get the power spectra at higher redshifts.

<object width="500" height="200" type="text/plain" data="{{site.baseurl}}/assets/files/IC_Code_new.txt" border="0" >
</object>
