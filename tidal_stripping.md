---
layout: page
permalink: /tidal_stripping/
title:  "Tidally Stripped Halos"
---


<p style="text-align:justify">
This project is related to modeling the evolution of tidally stripped subsystems. In minor mergers, dark matter halos fall into larger host halos and lose mass through tidal stripping, and the remaining bound material may exist as substructure within the host halo. Isolated simulations are often used to develop empirical models to describe the evolution of these systems, and these descriptions are used to develop galaxy formation models, dark matter annihilation constraints and lensing predictions. We have developed a physically-based model to describe the evolution of collisionless systems based on a truncation in energy space. Our model allows physical insight into the processes involved in tidal stripping. Also, since our model does not require tuning to simulations, it allows predictions for a wider range of halo models, including the earliest forming halos, which are known to have steeper density profiles.
</p>

<h2> Publications: </h2>
<ul>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2017MNRAS.468.2345D/abstract">Drakos, Taylor and Benson 2017</a> </li>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2020MNRAS.494..378D/abstract">Drakos, Taylor and Benson 2020</a> </li>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2022MNRAS.516..106D/abstract">Drakos, Taylor and Benson 2022</a> </li>
<li> Drakos, Taylor and Benson 2023 (in prep) </li>
</ul>


<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">
  {% for post in site.categories.tidal_stripping %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
