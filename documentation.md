---
layout: page-fullwidth
title: "Theme Documentation"
subheadline: "How to use Feeling Responsive"
description: "The documentation is a work in progress..."
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

### Post
The [post format]({{ site.url }}/design/post/) has no sidebar, its content is centered and beneath the content the visitor gets some metadata like categories, tags, date and author if provided via data in front matter of the post.

use in front matter via: `layout: post`


### Page
The [page template]({{ site.url }}/design/page/) shows the content in the same way as the *post* format without listing the metadata at the end of the page.

use in front matter via: `layout: page`


### Post with left sidebar
This template displays a [post left sidebar]({{ site.url }}/design/post-left-sidebar/) besides the content. To customize the content of the sidebar, open `_includes/sidebar.html`.

use in front matter via: `layout: post-left-sidebar`


### Post with right sidebar
This template displays a [post with right sidebar]({{ site.url }}/design/post-right-sidebar/) besides the content. To customize the content of the sidebar, open `_includes/sidebar.html`.

use in front matter via: `layout: post-right-sidebar`


### Page Full Width
If you want full control of styling a page, than use the [page full-width template]({{ site.url }}/design/page-full-width/). To set up a grid, just use the [foundation grid system](http://foundation.zurb.com/docs/components/grid.html).

use in front matter via: `layout: page-full-width`


### Video
If you're a video producer or cineast, you'll like the [video template]({{ site.url }}/design/video/). It darkens the layout to black and lets the video stand out full-width.

use in front matter via: `layout: video`

<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }




## Style your content with   {#styling}

Feeling Responsive offers lots of possibilities to style your articles. You can style your content in different ways. There are elements like subheadlines, feature images, header images, homepage images, meta data like categories and tags and many more.


### subheadlines

If you need a subheadline for an article, just define a subheadline in front matter like this:

`subheadline:  "Subheadline"`

### Quotes

Quotes mix it up a little bit, if you write long articles. So use quotes:

> Age is an issue of mind over matter. If you don't mind, it doesn't matter.
<cite>Mark Twain</cite>

<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }


## Responsive Videos

With foundation responsive videos are easy. [More ›](http://foundation.zurb.com/docs/components/flex_video.html)

<div class="flex-video">
        <iframe width="1280" height="720" src="//www.youtube.com/embed/WoHxoz_0ykI" frameborder="0" allowfullscreen></iframe>
</div>

### Code to use for flexible videos

{% highlight html %}
<div class="flex-video">
  <iframe with video />
</div>
{% endhighlight %}


<img class="t60" src="{{ site.url }}/assets/img/header_homepage_13.jpg">

## Images: Header, Title, Thumbnails, Homepage   {#images}

There are four types of images you can define via frontmatter: thumbnails, header images, title images and images in your article. 


### Header Images

Header images are displayed right under the top navigation. We use Backstretch to expand them from left to right. The width should be 1600 pixel or higher and in a ratio like 16:9 or 21:9 or 2:1.

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

Thumbnails are used on archive pages like the [blog index][2]. They have a size of 150x150 pixels. Define them in front matter like this:

~~~
image:
    thumb: thumbnail_image.jpg
~~~


### Homepage Image

If you want to feature an article on the homepage with a huge image, than use the homepage image with a width of 970 pixels. If no homepage image is defined *Feeling Responsive* writes over the blog entries *New Blog Articles*. Define the homepage image like this:

~~~
image:
    homepage: "header_homepage_13.jpg"
~~~



### Credits with URL

Sometimes you want to give credit to the creator of your images, maybe with a link. Especially when you use Creative Commons-images like I do for this website. Just add the following front matter and *Feeling Responsive* does the rest:

~~~
image:
    header: header_image.jpg
    credit: Image by Phlow
    url: "http://phlow.de/"
~~~

### Define all images for an article

~~~
image:
    header: header_image.jpg
    title: title_image.jpg
    thumb: thumbnail_image.jpg
    homepage: header_homepage_13.jpg
    credit: Image by Phlow
    url: "http://phlow.de/"
~~~


<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }


## Create a Table of Content
{: .t60}

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
**Table of Contents**
{: #toc }
*  TOC
{:toc}
</div>
{% endhighlight %}
<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }


## Includes

Includes can be very helpful to spice up your content. You can use includes in your Markdown-files with ease: Just call them with some Liquid code.

### list-posts.html

The `list-posts.html`-include is a loop to list posts. It's a helper to add some additional content fast and easy. You can use it in individual posts for example. Which parameters you use, depends on you.

Possible parameter for the loop:

- entries › define the number of entries to show
- offset › define the offset (number of entries to skip before displaying the first one)
- category › define **only one** category to display according entries

The loop looks when you use all parameters. Single parameters are possible of course.

~~~
{% raw %}
{% include list-posts.html entries='3' offset='1' category='design' %}
{% endraw %}
~~~


<small markdown="1">[Up to table of contents](#toc)</small>
{: .text-right }


## Javascript/Foundation modules

*Feeling Responsive* uses the foundation framework and some of its javascript components. I reduced the modules, to decrease page load and make the theme faster.

I only added one other javascript-module: [`backstretch`][3] by Scott Robbin. These modules are currently used by the theme and included in `javascript.min.js`. There is also a non-minified version, if you want to take a closer look: `javasript.js`.

~~~
/foundation/bower_components/foundation/js/vendor/jquery.js'
/foundation/bower_components/foundation/js/vendor/fastclick.js'
/foundation/bower_components/foundation/js/foundation.accordion.js'
/foundation/bower_components/foundation/js/foundation.clearing.js'
/foundation/bower_components/foundation/js/foundation.dropdown.js'
/foundation/bower_components/foundation/js/foundation.equalizer.js'
/foundation/bower_components/foundation/js/foundation.magellan.js'
/foundation/bower_components/foundation/js/foundation.topbar.js'
/foundation/js/jquery.backstretch.js'
~~~


</div><!-- /.medium-8.columns -->
</div><!-- /.row -->

 [1]: http://kramdown.gettalong.org/converter/html.html#toc
 [2]: {{ site.url }}/blog/
 [3]: http://srobbin.com/jquery-plugins/backstretch/
 [4]: #
 [5]: #
 [6]: #
 [7]: #
 [8]: #
 [9]: #
 [10]: #