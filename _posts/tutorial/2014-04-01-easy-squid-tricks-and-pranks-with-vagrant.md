---
title: Easy squid tricks and pranks with Vagrant
author: David
layout: page
permalink: /project/easy-squid-tricks-and-pranks-with-vagrant/
categories:
  - Projects
---
For April Fools this year, I decided to update my [2011 squid prank][1], and gain some experience using [Vagrant][2] at the same time. I rebuilt the entire environment using a Vagrantfile, which permits anybody to check out a few files and reproduce it. See <https://github.com/funkypenguin/squidprank> for the code.

As before, I invert the occasional image and change Google&#8217;s language to Klingnon (less effective now that HTTPS is common). Edit prank.pl and let your imagination run wild <img src="https://www.funkypenguin.co.nz/wp-includes/images/smilies/icon_smile.gif" alt=":)" class="wp-smiley" />

Brief summary is provided you have virtualbox and vagrant, establishing the VM with squid, redirector, arpspoof etc is automatically done using &#8220;vagrant up&#8221;. The only prompt you&#8217;ll get on establishing the box is for an ethernet adapter to used in bridged mode (to do the traffic spoofing / interception).

Refer to the [README][3] for more details on getting started.

 [1]: https://www.funkypenguin.co.nz/tutorial/april-fools-pranks-with-a-squid-proxy-server/ "Squid Prank April Fools"
 [2]: http://www.vagrantup.com/ "Vagrant"
 [3]: https://github.com/funkypenguin/squidprank/blob/master/README.md
