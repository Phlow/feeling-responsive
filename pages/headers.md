---
layout: page
subheadline: "Header"
title: "Style your Header!"
description: "These are your options to style the header of each webpage individually."
image:
   header: "header_unsplash_5.jpg"
permalink: "/headers/"
---
<ul>
    {% for post in site.tags.header %}
    <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>