---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  image_fullwidth: reactor1.png
widget1:
  title: "Download Now"
  url: 'https://github.com/visit-dav/visit'
  image: widget-github-303x182.jpg
  text: 'Get the <a href="https://github.com/visit-dav/visit/releases/latest">latest release</a> to start visualizing and analyzing your data today. Or, download the <a href="https://github.com/visit-dav/visit/releases/download/v3.1.1/build_visit3_1_1">build_visit</a> script to build a custom version. Please <a href="https://github.com/visit-dav/visit/issues/new">share a comment</a> with us about your experiences with VisIt.'
widget2:
  title: "Why use VisIt?"
  url: '/about/'
  text: '<em>VisIt</em> is extremely scalable.<br/>1. Runs on Unix, Windows & OSX<br/>2. Is Free, <a href="https://github.com/visit-dav/visit/blob/develop/LICENSE">BSD Open Source</a>.<br/>3. Reads 130+ <a href="https://www.visitusers.org/index.php?title=Detailed_list_of_file_formats_VisIt_supports">File Formats</a>.<br/>4. Installed on many <a href="https://science.osti.gov/User-Facilities/User-Facilities-at-a-Glance/ASCR">LCFs</a>'
  video: '<center><a href="#" data-reveal-id="videoModal"><img src="images/wing_tip_streamlines_thumb.png" width="303" align="middle"/></a></center>'
widget3:
  title: "Updates & Plans"
  url: 'https://github.com/visit-dav/visit/issues?q=is%3Aopen+is%3Aissue+milestone%3A3.2'
  image: gallery_00b.png
  text: 'Learn about recent releases, plans for upcomming releases, works in progress and other stuff about VisIt, its related technologies and visualization and data analysis in general.'

callforaction:
  url: https://elist.ornl.gov/mailman/listinfo/visit-announce
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
  <iframe width="1280" height="720" src="https://www.youtube.com/embed/aRV5etrNlAQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
  <a class="close-reveal-modal">&#215;</a>
</div>
