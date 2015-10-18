---
layout: page
#
# Content
#
subheadline: "Video & Music Player"
title: "Play Audio & Video with mediaelement.js"
teaser: "Do you like music? Or are you a podcaster? Do you want to stream your videos in a nice player? Than you likely will like the integration of <em>mediaelement.js</em>. It enables you to play music and stream video in a consistent player that looks in each browser delicious. It even works in IE6-8."
categories:
  - design
tags:
  - audio player
  - video player
  - streaming music
#
# Styling
#
header: no
image:
    title: mediaplayer_js-title.jpg
    thumb: mediaplayer_js-thumb.jpg
    homepage: mediaplayer_js-home.jpg
    caption: Photo by Corey Blaz
    caption_url: https://blaz.photography/
mediaplayer: true
---
[mediaelement.js][1] is like magic. It's browser and device support is perfect. To activate the video or audio player just set the following variable in front matter to `true`.

~~~
mediaplayer: true
~~~

To use the player just use some HTML5-magic like...

{% highlight html %}
<audio src="http://path-to-file.com/music.mp3" type="audio/mp3" controls="controls"></audio>
{% endhighlight %}

All possible functions and how to use *mediaelement.js* is well-documented on the [players website][1].



### B-Ju - »Philly Run«

<audio src="http://archive.org/download/music_from_all_around_the_world/13._music_from_all_around_the_world_-_b-ju_-_philly_run.mp3" type="audio/mp3" controls="controls"></audio>

### Comfort Fit - »Freeze The Cut« <span class="subhead">(Opolopo's Emotional Draft Remix)</span>

<audio src="http://archive.org/download/music_from_all_around_the_world/05._music_from_all_around_the_world_-_comfort_fit_-_freeze_the_cut_opolopos_emotional_draft_remix.mp3" type="audio/mp3" controls="controls"></audio>

### The Black Atlantic - »Dandelion«

<audio src="http://archive.org/download/music_from_all_around_the_world/02._music_from_all_around_the_world_-_the_black_atlantic_-_dandelion.mp3" type="audio/mp3" controls="controls"></audio>




 [1]: http://mediaelementjs.com/
 [2]: #
 [3]: #
 [4]: #
 [5]: #
 [6]: #
 [7]: #
 [8]: #
 [9]: #
 [10]: #