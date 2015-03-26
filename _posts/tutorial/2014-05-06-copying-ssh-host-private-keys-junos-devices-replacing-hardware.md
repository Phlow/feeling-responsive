---
title: Copying SSH host private keys between JUNOS devices to when replacing hardware
author: David
layout: page
permalink: /note/copying-ssh-host-private-keys-junos-devices-replacing-hardware/
wp-to-buffer-success:
  - 1
categories:
  - Note
tags:
  - junos
  - ssh
---
A certain customer of mine is (rightly or wrongly) pedantic about security warnings. Recently, we did a hardware replacement of a JUNOS device (an SRX240 firewall). While the config was a drop-in replacement, users who tried to SSH to the host post-migration would normally see an SSH &#8220;host key has changed&#8221; warning. In this environment, we wanted to eliminate this friction (and stop training our users to ignore security warnings), so we copied the following from the old device:

  * /etc/ssh/ssh\_host\_dsa_key
  * /etc/ssh/ssh\_host\_dsa_key.pub
  * /etc/ssh/ssh\_host\_rsa_key
  * /etc/ssh/ssh\_host\_rsa_key.pub

And overwrote the corresponding files in /etc/ssh/ on the new device. Surprisingly, no restart of the SSH service was required to effect this. But, of course, it had to be done as root.

&nbsp;
