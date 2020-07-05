---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: header_atos.jpg
widget1:
  title: "Virtual Reality"
  url: 'https://github.com/Phlow/feeling-responsive'
  image: widget-vr-302x182.jpg
  text: 'Discover the selves dwelling just beneath the surface.'
widget2:
  title: "Mobile Applications"
  url: 'https://github.com/Phlow/feeling-responsive'
  image: widget-apps-302x182.jpg
  text: 'Browse through what we have developed and get a sneak peek at what is in the works.'
widget3:
  title: "Blog"
  url: 'http://phlow.github.io/feeling-responsive/blog/'
  image: widget-tutorials-302x182.jpg
  text: 'Tutorials and musings through middle earth and the virtual unknown.'

#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: https://tinyletter.com/feeling-responsive
  text: Inform me about new updates and features ›
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

<div id="videoModal" class="reveal-modal large" data-reveal="">
  <div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/3b5zCFSmVvU" frameborder="0" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>
