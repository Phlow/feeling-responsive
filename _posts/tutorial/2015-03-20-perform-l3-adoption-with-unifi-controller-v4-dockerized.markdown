---
layout: page
title: "Perform L3 adoption with UniFi Controller v4 (Dockerized)"
date: "2015-03-20"
category: how-to
---
Having recently deployed a "dockerized" [Ubiquity UniFi Controller][2], I was forced to reset my UniFi AP so that I could re-adopt it and bring it back under management.

This shouldn't have been a big deal, but a number of systems didn't work as the should have.

1. Using DHCP option 43 to point to the IP of the UniFi controller simply didn't work on the latest ScreenOS. Apparently the intended behaviour is that the AP [uses the result of DHCP option 43 to populate /etc/hosts with an entry for "unifi"][3]
2. Manually using set-inform from the CLI of the AP to my controller didn't work. I got errors about "Server Reject":
```Jan 1 00:33:22 UBNT user.err syslog: ace_reporter.reporter_fail(): Server Reject (http://192.168.1.78:8080/inform)```

Having discovered #1, I tried manually editing /etc/hosts on the AP, after which (surprisingly) my AP happily registered for adoption. I adopted it in the UniFi Controller, after which it promptly rebooted for a firmware update. After reboot, /etc/hosts was reset, and it was unable to complete changing to a "managed state":

```Mar 20 00:27:09 UBNT user.err syslog: ace_reporter.reporter_fail(): initial contact failed #14, url=http://unifi:8080/inform, rc=1
Mar 20 00:27:09 UBNT user.info syslog: ace_reporter.reporter_next_inform_url(): next inform url[0]=http://unifi:8080/inform
```

I re-ran the procedure to manually add my controller's AP to /etc/hosts, and the adoption completed successfully.

What I've learned:

1. DHCP Option 43 is unreliable. I'd be better off to create an A record in my domain for "unifi", pointing to the controller
2. Standardize on using an "admin" user for the controller. Don't get clever and change the username (to something like "davidy", for example). It'll only bite you in the end.

Another helpful tip I stumbled across on the way:

* Make sure you're logged into the controller as the user you setup when you installed the controller (The "[Super Admin][1]")




[1]: https://registry.hub.docker.com/u/pducharme/unifi/dockerfile/
[2]: http://community.ubnt.com/t5/UniFi-Wireless/AP-s-can-t-discover-controller/td-p/588425
[3]: https://community.ubnt.com/t5/UniFi-Wireless/Question-re-DHCP-Option-43/td-p/635501
