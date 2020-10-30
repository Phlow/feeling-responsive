---
layout: page
subheadline: "Blog"
title: "Teller of Worlds"
teaser: "A blog following Ousikai's daily musings and meanderings."
header:
    image_fullwidth: "blog/teller-of-worlds/floor-1-original.png"
    caption: In this world, a single blade can take you anywhere you want to go.
    caption_url: "https://en.wikipedia.org/wiki/Sword_Art_Online"
image:
    thumb:  blog/teller-of-worlds/floor-1-thumb.jpg
    homepage: blog/teller-of-worlds/floor-1-thumb.jpg
categories:
    - blog
tags:
    - reflection
    - story-telling
author: Ousikai
show_meta: true
comments: true
---
## Latest Blog Posts
<ul>
    {% for post in site.tags.teller-of-worlds %}
    <div class="row">
      <div class="small-12 columns b60">
        <h2><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
        <p>
          {% if post.image.thumb %}<a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" title="{{ post.title | escape_once }}"><img src="{{ site.urlimg }}{{ post.image.thumb }}" class="alignleft" width="150" height="150"></a>{% endif %}

          {% if post.meta_description %}{{ post.meta_description | strip_html | escape }}{% elsif post.teaser %}{{ post.teaser | strip_html | escape }}{% endif %}

          <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" title="{{ site.data.language.read }} {{ post.title | escape_once }}"><strong>{{ site.data.language.read_more }}</strong></a>
        </p>
      </div><!-- /.small-12.columns -->
    </div><!-- /.row -->
    {% endfor %}
</ul>


<!-- [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Q5Q81LOP9) -->
