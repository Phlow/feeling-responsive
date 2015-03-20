---
title: 'Bandersnatch &#8211; The Jabber Logger'
author: David
excerpt: Bandersnatch is tool to log Jabber instant messaging traffic, and to generate meaningful usage statistics. Bandersnatch is designed for a corporate intranet environment. It is designed for administrators who wish to monitor the use / abuse of their Jabber servers.
layout: page
permalink: /project/bandersnatch/
btc_comment_counts:
  - 'a:0:{}'
btc_comment_summary:
  - 'a:0:{}'
bttc_cache:
  - 1301635694:0
aktt_notify_twitter:
  - no
categories:
  - Projects
tags:
  - bandersnatch
  - jabber
---
### What is Bandersnatch?

Bandersnatch is tool to log Jabber instant messaging traffic, and to generate meaningful usage statistics. Bandersnatch is designed for a corporate intranet environment. It is designed for administrators who wish to monitor the use / abuse of their Jabber servers.

### Peer-Policing

Bandersnatch is intended to be a deterrent to corporate users abusing a Jabber system for personal purposes. It is designed around the &#8220;peer-policing&#8221; theory, which hypothesizes that:

<p style="padding-left: 30px;">
  &#8221;If an individual is aware that their activities are publicly visible, they are likely to limit their activities to the public standard&#8221;.
</p>

In other words, if your users know that their Jabber activity is logged, and that their peers can see how many remote (personal?) messages they&#8217;ve sent, they&#8217;ll keep their behavior within reasonable boundaries.

### What information is publicly visible?

Statistics on total messages sent and received (both locally and remotely), and top user activity are publically visible. Individual  
message logs are not publicly visible.

### What information is visible to the administrator?

The administrator is able to view individual message logs. Administrators must &#8220;log in&#8221; in order to view logs.

### Privacy

Bandersnatch can be run with varying degrees of privacy:

  * Level 0 &#8211; Log everything
  * Level 1 &#8211; Mask out remote usernames
  * Level 2 &#8211; Mask out remote usernames and remote message bodies
  * Level 3 &#8211; Mask out remote usernames and all message bodies

For example, at Privacy Level 3, Bandersnatch will only record local usernames. It will be still report on local vs. remote usage, and message totals, but remote users will not be identifiable, and the actual text of the messages will not be logged.

### Download

Bandersnatch [source][1] is now hosted on <a title="GitHub" href="https://github.com/funkypenguin/bandersnatch" target="_blank">GitHub</a>

 [1]: https://github.com/funkypenguin/bandersnatch "source"
