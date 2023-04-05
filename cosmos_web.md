---
layout: page
permalink: /cosmos_web/
title:  "COSMOS Web"
---


<p style="text-align:justify">
This page contains the work I've done for COSMOS-Web
</p>



<h2> Related Publications: </h2>
<ul>
<li> <a href="https://ui.adsabs.harvard.edu/abs/2022arXiv221107865C/abstract">Casey, Kartaltepe, Drakos, et al. 2022</a> </li>
</ul>



<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">
  {% for post in site.categories.cosmos_web %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
