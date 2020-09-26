---
layout: page
permalink: /other/
title:  "Other"
---


<h2 class="page-heading">Posts</h2>

<ul class="post-list">
  {% for post in site.categoriesother %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
