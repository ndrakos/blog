---
layout: page
permalink: /iso_sims/
title:  "Isolated Merger Simulations"
---


<p style="text-align:justify">
This project involves running simulations of controlled, isolated mergers between dark matter haloes.
</p>

<h2> Related Publications: </h2>
<ul>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2019MNRAS.487..993D/abstract">Drakos, Taylor, Berroueut, Robotham and Power 2019</a> </li>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2019MNRAS.487.1008D/abstract">Drakos, Taylor, Berroueut, Robotham and Power 2019</a> </li>
</ul>


<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">
  {% for post in site.categories.iso_sims %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
