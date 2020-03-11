---
layout: page
permalink: /cosmo_sims/
title:  "High Time Resolution Simulations"
---


<p style="text-align:justify">
In this project, I will run dark matter cosmological simulations with many time outputs. This will enable us to study mass accretion histories of halos in more detail. Additionally, we will look at how the time resolution effects different parts of the procedure to produce mock catalogues (e.g. abundance matching and light cone generation).
</p>



<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">
  {% for post in site.categories.cosmo_sims %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
