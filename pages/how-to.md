---
layout: page
show_meta: false
subheadline: "How-To"
title: "How to..."
description: "As I figure out stuff, I like to post it here"
permalink: "/how-to/"
---
The links below explain how to..
<ul>
    {% for post in site.categories.how-to %}
    <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
