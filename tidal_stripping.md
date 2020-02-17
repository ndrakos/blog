---
layout: page
permalink: /tidal_stripping/
title:  "Tidally-Stripped Halos"
---



<h2 class="page-heading">Related Posts</h2>

<ul class="post-list">
  {% for post in site.categories.tidal_stripping %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
