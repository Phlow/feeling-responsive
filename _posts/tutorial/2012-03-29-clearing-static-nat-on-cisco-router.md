---
title: Clearing static nat on Cisco router
author: David
layout: page
permalink: /note/clearing-static-nat-on-cisco-router/
aktt_notify_twitter:
  - no
categories:
  - Note
tags:
  - cisco
---
I was asked to change a incoming NAT translation on a Cisco router for a customer today&#8230; however since this NAT was used to deliver all their internal email, it was never \_not\_ in use, and I got the standard message below when trying to clear it:

> %Static entry in use, cannot change

Thanks to [phirebird.net][1], I discovered that if (in conf mode) , I prefix my (pre-prepared and ready to paste) nat changes with &#8220;do clear ip nat translation *&#8221;, I can clear and change them fast enough to avoid the problem <img src="https://www.funkypenguin.co.nz/wp-includes/images/smilies/icon_smile.gif" alt=":)" class="wp-smiley" />

 [1]: http://www.phirebird.net/2009/07/cant-remove-ip-nat-entries-on-cisco-router-static-entry-in-use-cannot-remove/ "phirebird.net"
