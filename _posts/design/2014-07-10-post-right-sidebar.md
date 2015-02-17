---
layout: page
sidebar: right
subheadline: Templates
title:  "Page/Post Right Sidebar"
teaser: "This is a example of page/post with a sidebar on the right."
breadcrumb: true
tags:
    - post format
categories:
    - design
image:
    thumb: "unsplash_2_thumb.jpg"
    title: "unsplash_2.jpg"
    credit: Unsplash.com
    url: http://unsplash.com
---
*Feeling Responsive* shows metadata by default. The default behaviour can be changed via `config.yml`. To show metadata at the end of a page/post just add the following to front matter:

~~~
show_metadata: true
~~~

If you don't want to show metadata, it's simple again:

~~~
show_metadata: false
~~~


## Other Post Formats
{: .t60 }
{% include list-posts.html tag='post format' %}
