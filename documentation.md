---
layout: page-fullwidth
title: "Theme Documentation"
subtitle: "How to use Feeling Responsive"
description: "The documentation is a work in progress..."
image:
    header: "no"
permalink: "/documentation/"
---
<div class="row">
<div class="medium-4 medium-push-8 columns" markdown="1">
<div class="panel radius" markdown="1">
**Table of Contents**
{: #toc }
*  TOC
{:toc}
</div>
</div><!-- /.medium-4.columns -->



<div class="medium-8 medium-pull-4 columns" markdown="1">

## Different Page/Posts Formats   {#formats}

*Feeling Responsive* supports you with different templates for your content. These are the actual page/post formats:

[Post]({{ site.url }}/design/post/)
:   The *post* format has no sidebar, its content is centered and beneath the content the visitor gets some metadata like categories, tags, date and author if provided via data in front matter of the post.
:   use in front matter via: `layout: post`


[Page]({{ site.url }}/design/page/)
:   Shows the content in the same way as the *post* format without listing the metadata at the end of the page.
:   use in front matter via: `layout: page`


[Post with left sidebar]({{ site.url }}/design/post-left-sidebar/)
:   Displays a left sidebar besides the content. To customize the content of the sidebar, open `_includes/sidebar.html`.
:   use in front matter via: `layout: post-left-sidebar`


[Post with right sidebar]({{ site.url }}/design/post-right-sidebar/)
:   Displays a right sidebar besides the content. To customize the content of the sidebar, open `_includes/sidebar.html`.
:   use in front matter via: `layout: post-right-sidebar`


[Page Full Width]({{ site.url }}/design/page-full-width/)
:   If you want full control of styling a page, than use the full-width template. To set up a grid, just use the [foundation grid system](http://foundation.zurb.com/docs/components/grid.html).
:   use in front matter via: `layout: page-full-width`

<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }




## Style your content with   {#styling}

Feeling Responsive offers lots of possibilities to style your articles. You can style your content in different ways. There are elements like subtitles, feature images, header images, meta data like categories and tags and many more.


### Subtitles

If you need a subheadline for an article, just define a subheadline in front matter like this:

`subtitle:  "Subheadline"`

### Quotes

Quotes mix it up a little bit, if you write long articles. So use quotes:

> Age is an issue of mind over matter. If you don't mind, it doesn't matter.
<cite>Mark Twain</cite>





## Images: Header, Title, Thumbnails   {#images}

There are four types of images you can define via frontmatter: thumbnails, header images, title images and images in your article. 


### Header Images

Header images are displayed right under the top navigation. We use Backstretch to expand them from left to right. The width should be 1600 pixel or higher and in a ratio like 16:9 or 21:9 or 2:1. <mark>If you don't want any header image just write `image_header: "no"` into front matter.</mark>

~~~
image:
   header: thumbnail_image.jpg
~~~


### Title Images

~~~
image:
   title: thumbnail_image.jpg
~~~

You can choose to show a special full-width header image or not.


### Thumbnails

Thumbnails are used on archive pages like the [blog index][2]. Define them in front matter like this:

~~~
image:
   thumb: thumbnail_image.jpg
~~~


### Define all three images

~~~
image:
   header: header_image.jpg
   title: title_image.jpg
   thumb: thumbnail_image.jpg
~~~


<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }


## Create a Table of Content

With the Kramdown parser for Markdown you can render a table of contents for your documents. Just insert the following HTML in your post before the actual content. More information on [»Automatic ›Table of Contents‹ Generation«][1].

### Bare Bones Version
{% highlight html %}
### Table of Contents
*  Auto generated table of contents
{:toc}
{% endhighlight %}

### Foundation panel version

{% highlight html %}
<div class="panel radius" markdown="1">
### Table of Contents
*  Auto generated table of contents
{:toc}
</div>
{% endhighlight %}
<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }

</div><!-- /.medium-8.columns -->



</div><!-- /.row -->

 [1]: http://kramdown.gettalong.org/converter/html.html#toc
 [2]: {{ site.url }}/blog/
 [3]: #
 [4]: #
 [5]: #
 [6]: #
 [7]: #
 [8]: #
 [9]: #
 [10]: #