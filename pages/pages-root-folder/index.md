---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: page
header:
    title: IoT Lab
    image_fullwidth: banner.jpg
   
title: "Overview"

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
  url: https://mlist.is.ed.ac.uk/lists/subscribe/iot
  text: Subscribe to the University of Edinburgh IoT Mailing List
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
---

The Internet of Things (IoT) is a cluster of technologies spanning hardware devices, networking, data collection and data applications. It allows any ‘thing’ to be connected to the internet. This means that we give things a name, a job to do, and a voice. A name is some kind of unique identifier; a job will typically involve some kind of sensing of &mdash; or acting upon &mdash; the environment; a voice is a means of communicating. As an example, we might add sensors to a chair so that it can tell whether someone is sitting on it. If all chairs in a given room were able to communicate this information, we could get a real-time picture of how full it was.

As an initiative spearheaded by Information Services, the University is setting up a pilot IoT network using LoRaWAN technology. The network will be made available as a shared infrastructure for R&amp;D by a wide range of partners, as well as supporting teaching and learning opportunities within the University.
