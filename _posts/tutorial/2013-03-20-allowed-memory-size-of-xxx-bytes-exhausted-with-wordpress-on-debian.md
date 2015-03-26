---
title: Allowed memory size of xxx bytes exhausted with WordPress on Debian
author: David
layout: page
permalink: /note/allowed-memory-size-of-xxx-bytes-exhausted-with-wordpress-on-debian/
categories:
  - Note
tags:
  - debian
  - wordpress
---
My Debian Squeeze host started having trouble performing WordPress 3.5 core or plugin updates &#8211; in the error logs, I&#8217;d see messages like:

> Allowed memory size of xxx bytes exhausted

After scouring the internet, attempting to adjust memory limits on php.ini, apache, etc, I eventually discovered the solution was to add:

> *USE\_ZEND\_ALLOC*=0

to /etc/apache2/envvars. Problem solved.
