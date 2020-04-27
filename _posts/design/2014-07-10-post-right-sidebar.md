---
layout: page
sidebar: right
subheadline: Templates
title:  "Page/Post Right Sidebar"
teaser: "This is an example of page/post with a sidebar on the right."
sidebar-text: "Don't forget to have look at the new features in [SILO](https://silo.llnl.gov)"
sidebar-image: "gallery_01.jpg"
breadcrumb: true
tags:
    - post format
categories:
    - design
image:
    thumb: gallery-example-2-thumb.jpg
    title: gallery-example-2.jpg
    caption: Unsplash.com
    caption_url: http://unsplash.com
audience: "developers"
---
*Feeling Responsive* shows metadata by default. The default behaviour can be changed via `config.yml`. To show metadata at the end of a page/post just add the following to front matter:
<!--more-->

~~~
show_meta: true
~~~

If you don't want to show metadata, it's simple again:

~~~
show_meta: false
~~~


## Other Post Formats
{: .t60 }
{% include list-posts tag='post format' %}
