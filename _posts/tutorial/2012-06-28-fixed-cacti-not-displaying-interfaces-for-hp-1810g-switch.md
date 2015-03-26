---
title: Fixed Cacti not displaying interfaces for HP 1810G switch
author: David
layout: page
permalink: /note/fixed-cacti-not-displaying-interfaces-for-hp-1810g-switch/
aktt_notify_twitter:
  - no
categories:
  - Note
tags:
  - cacti
  - monitoring
  - snmp
---
While implementing a new network for a customer, we took an existing HP 1810G 48-port switch under management. As per normal, we setup monitoring (Icinga) and graphing (Cacti), but while the switch responded to Cacti sysname polls (leading us to believe it was happy), it didn&#8217;t return any interface details, so we weren&#8217;t able to graph anything.

After chasing a few red herrings, I tried changing the SNMP version from 2 to 1 in the Cacti device config, and after a refresh, I was able to graph all my interfaces again <img src="https://www.funkypenguin.co.nz/wp-includes/images/smilies/icon_smile.gif" alt=":)" class="wp-smiley" />

Strange thing was.. an SNMP walk on -v 2c would still give me the correct results, but seeing that the 1810G is a entry-level model (with a very basic web UI only), perhaps its SNMP implementation is a little flakey.
