---
permalink: /virtual-reality/vr-developer-diaries/
layout: page
subheadline: "Blog"
title: "VR Developer Diaries"
teaser: "A blog following mtfallsVR's journey in creating virtual worlds and experiences."
header:
    image_fullwidth: "blog/vr-developer-diaries/header-intro.jpg"
    caption:  Akihiko Kayaba, the famed created of Sword Art Online
    caption_url: "https://en.wikipedia.org/wiki/Sword_Art_Online"
image:
    thumb:  blog/vr-developer-diaries/thumb-intro.jpg
    homepage: blog/vr-developer-diaries/kayaba-akihiko-BIG.jpg
categories:
    - virtual-reality
tags:
    - Virtual Reality
    - Oculus Quest
author: mtfallsVR
show_meta: true
---
The most important value in gaining knowledge, is the application of it. The most important value in applying things, is finding out what your limits are, so you can exceed them on your next attempt. In this blog, I will be putting my [knowledge][1] to the test to see if I can get even just an inch closer to creating the worlds I've dreamed of for so long.  

![Aincrad](/images/blog/vr-developer-diaries/aincrad-full.jpg)

# Latest Blog Posts
<ul>
    {% for post in site.tags.vr-developer-diaries %}
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


[1]: {{site.baseurl}}/virtual-reality/evolution-of-experience


<!-- [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Q5Q81LOP9) -->
