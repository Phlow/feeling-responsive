---
title: Restart VRRP on JUNOS to fix master/master issues
author: David
layout: page
permalink: /note/trouble-vrrp-mastership-2-junos-devices-restarting-vrrp-can-fix/
categories:
  - Note
tags:
  - junos
  - vrrp
---
I spent about 30 min this evening chasing a non-existing VRRP issue between 2 JUNOS SRX devices after a hardware drop-in replacement. One was configured as master, one as backup. Both were in the &#8220;master&#8221; status (normally indicating a lack of L2 connectivity), but each could ping the other on their interface address. The solution, ultimately, was to run &#8220;restart vrrp gracefully&#8221; on each router, which restored the expected master / backup behaviour.
