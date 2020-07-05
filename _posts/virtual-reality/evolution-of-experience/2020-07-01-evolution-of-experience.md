---
permalink: /virtual-reality/evolution-of-experience/
layout: page
subheadline: "Blog"
title: "Evolution of Experience"
teaser: "A blog following mtfallsVR's journey in experiencing what virtual reality has to offer and what new affordances succeed and fail in the infancy of this medium."
header:
    image_fullwidth: "blog/evolution-of-experience/header-intro.jpg"
    caption: Sword Art Online - Ordinal Scale
    caption_url: "https://en.wikipedia.org/wiki/Sword_Art_Online"
image:
    thumb:  blog/evolution-of-experience/thumb-intro.jpg
    homepage: blog/evolution-of-experience/header-intro.jpg
categories:
    - virtual-reality
tags:
    - Virtual Reality
    - Oculus Quest
author: mtfallsVR
show_meta: true
---
In an effort to convince me to be more diligent about my education and wanderlust of the virtual world while simulatenouesly improving my rapid writing skills, I am starting a blog to annote all my experiences in exploring the virtual world. As of July 3rd, 2020, virtual reality is still a gimmicky technology that has yet to find its niche and true value to the ever-evolving world. Through this blog, I will be testing both popular and indie experiences to see what each title has new to bring to the table, what lessons can be learned, and how I can implement all this knowledge into my own [virtual reality development diaries][1].

# Latest Blog Posts
<ul>
    {% for post in site.tags.evolution-of-experience %}
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


[1]: {{site.baseurl}}/virtual-reality/vr-developer-diaries


<!-- [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Q5Q81LOP9) -->
