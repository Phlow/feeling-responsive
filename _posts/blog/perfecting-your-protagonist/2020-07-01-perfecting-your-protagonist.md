---
layout: page
subheadline: "Blog"
title: "Perfecting Your Protagonist"
teaser: "A blog following Ousikai's journey in discovering the hero within."
header:
    image_fullwidth: "blog/perfecting-your-protagonist/intro-header.jpg"
    caption: In this world, a single blade can take you anywhere you want to go.
    caption_url: "https://en.wikipedia.org/wiki/Sword_Art_Online"
image:
    thumb:  blog/perfecting-your-protagonist/intro-thumb.jpg
    homepage: blog/perfecting-your-protagonist/intro.jpg
categories:
    - blog
tags:
    - self-improvement
author: Ousikai
show_meta: true
---
# The Story So Far
All my life, I have second guessed myself in every regard for every conceivably stupid reason. I always played the safe choices, which almost always guaranteed the safe outcomes. I followed the rails set upon by life, made it through school, university, and got a nice high-paying job, am living debt-free, and have a nice nest egg in case of emergencies. I get along with almost everyone, but I feel as though I can be honest with no one. Someone people would give everything and more to be in the position I'm currently in, and I'm *extremely* thankful that I grew up in a loving household that pushed me to at least get this far, but it seems as though... this isn't really what I need. When someone asks me given the chance to become anyone, who would I pick? Honestly, I wish I could be myself with more confidence.

With all these factors in mind, it took me a LONG time to pull the wool from over my eyes. To realize that everything is not okay, and I was falling. To only way to bolster my confidence, is by confronting by fears directly. And it's scary. The thought of going out of my comfort zone makes me tear up, throw up, sick to my stomach, and I want to quit before I even take the first step. But that's just it: *the first step is always the hardest*.

So this blog is my first step in recognizing what paralyzes me into inaction, drowning myself in my fears, and coming out the other side. This journey will not be easy, because the main theme of this adventure is *accepting failure*. My life up to this point has been uneventful because of my uncertainty and unwillingness to see how the greater world can challenge me. But now... instead of being afraid of what makes me sick to my stomach, I relish in the feeling. Because now I realize I'm above to cross a ravine, and find a new me on the other side.

The other main reason I'm making this blog is to find allies who are willing to walk this journey with me. As great as the sum of one person can be, real change can only occur when you find like-minded individuals who both challenge and support you. They keep you accountable, push you past the limits you didn't realize you had, and are generally some of the most inspirational and powerful people you can keep in your company.  

If you're willing to walk on this journey, let's take the first step. *Together*.


# Latest Blog Posts
<ul>
    {% for post in site.tags.perfecting-your-protagonist %}
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
