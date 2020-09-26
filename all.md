---
layout: page
permalink: /all/
title:  "All Posts"
---


<ul class="post-list">
  {% for post in site.posts %}

  <li>
    <span>{{ post.date | date: "%b %-d, %Y" }}</span> &nbsp; <a href="{{ post.url | prepend: site.baseurl }}">{{post.title }}</a>
  </li>

  {% endfor %}
</ul>
