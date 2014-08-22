---
layout: page-fullwidth
title: "Theme Documentation"
subtitle: "How to use Feeling Responsive"
description: "The documentation is a work in progress..."
image_header: "no"
permalink: "/documentation/"
---
<div class="row">
<div class="medium-8 columns" markdown="1">

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



## How to use images   {#images}

There are three types of images you can define via frontmatter:

 - thumbnails
 - header images
 - title images

<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }



## Possibilites to style your Post   {#styling}

You can style your content in different ways. There are elements like subtitles, feature images, header images, meta data like categories and tags and many more. This article shows the different possibilites.

## Subtitles

## Feature Images

## Header Images

You can choose to show a special full-width header image or not.

## Meta-Data



## Create a Table of Contents via Kramdown

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



</div><!-- /.medium-8.columns -->

<div class="medium-4 columns" markdown="1">
<div class="panel radius" markdown="1">
**Table of Contents**

*  TOC
{:toc}
</div>
</div><!-- /.medium-4.columns -->
</div><!-- /.row -->



 [1]: http://kramdown.gettalong.org/converter/html.html#toc
 [2]: #
 [3]: #
 [4]: #
 [5]: #
 [6]: #
 [7]: #
 [8]: #
 [9]: #
 [10]: #