---
title: Monitoring OSX with Icinga / Nagios using NRPE
author: David
layout: page
permalink: /tutorial/monitoring-osx-with-icinga-nagios-nrpe/
categories:
  - Tutorial
tags:
  - icinga
  - nagios
  - osx
---
I have a fairly comprehensive [Icinga][1] monitoring platform monitoring my various linux hosts, but one area which has been lacking until now is the monitoring of the OSX Mavericks Mac Mini that I use for a home media center. Considering this is used by my family to watch <a title="Plex" href="http://plex.tv" target="_blank">TV/Movies</a>, play music, and manage iPhoto, it&#8217;s arguably one of the most important hosts to monitor carefully. Of course, I could monitor its state (up or down) by pinging it from Icinga, but I wanted to know more than that. I&#8217;ve had issues in the past with running out of disk space on the host, and I&#8217;m all to familiar with the risks of 4-year-old hardware using spindled disks. This solution enables me to monitor the following on OSX with Icinga:

  * Load/Memory
  * Disk Usage
  * Time Machine Status
  * Disk Health

<!--more-->

# Prerequisites

## Homebrew Install

<a title="Homebrew" href="http://brew.sh/" target="_blank">Homebrew</a> as per the docs on the website (or just paste in the line below):

`ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`

# Installation

## NRPE and nagios-plugins To install NRPE along with the standard nagios-plugins, install NRPE using brew: [bash]brew install nrpe[/bash] To have launchd start nrpe at login: [bash]ln -sfv /usr/local/opt/nrpe/*.plist ~/Library/LaunchAgents[/bash]

# Configuration Edit /usr/local/etc/nrpe.cfg, and set at least the

**allowed_hosts** directive to the IP of your Icinga host It may also be necessary (because of the location the plugins are installed to) to change occurances of  
`/usr/local/Cellar/nrpe/2.15/` To `/usr/local/Cellar/nagios-plugins/1.5/` Further, customize disk usage plugin as follows, by removing reference to the specific device (/ instead of /dev/<whatever>) `# Disk usage (use plugin supplied by nagios-plugins from brew) command[check_disk]=/usr/local/Cellar/nrpe/2.15/sbin/check_disk -w 20% -c 10% -p /` To start NRPE immediately, run: `launchctl load ~/Library/LaunchAgents/homebrew.mxcl.nrpe.plist`

## Install smartmontools Use Brew again to install smartmontools, necessary for the disk health check: `brew install nrpe smartmontools`

## Add custom plugins Download additional nagios plugins from

<a href="https://github.com/jedda/OSX-Monitoring-Tools" target="_blank">https://github.com/jedda/OSX-Monitoring-Tools</a> (I used <span class="css-truncate css-truncate-target"><a id="18a14441501fb6d3b2b859ec4fecb5fd-6da31795108d8cd5ee7326d82d9d4b0eb3edfa0f" class="js-directory-link" title="check_smart.sh" href="https://github.com/jedda/OSX-Monitoring-Tools/blob/master/check_smart.sh" target="_blank">check_smart.sh</a></span> and <span class="css-truncate css-truncate-target"><a id="e9adde12d25015ad2c8cfd0971bfe6c0-8123de00944c2d6f3d20bd103682602acd4ca1dd" class="js-directory-link" title="check_time_machine_currency.sh" href="https://github.com/jedda/OSX-Monitoring-Tools/blob/master/check_time_machine_currency.sh" target="_blank">check_time_machine_currency.sh</a></span>) To avoid future updates breaking non-brew-managed plugins, put them in ~/bin/. Symlink smartctl into ~/bin to avoid future conflicts: `ln -s /usr/local/Cellar/smartmontools/6.2/sbin/smartctl ~/bin/` Edit check_smart.sh, and replace every occurance of `/opt/local/libexec/nagios/smartctl` with `/Users/<youruser>/bin/smartctl` Add the following to /usr/local/etc/nrpe.cfg: `# Disk Health (use custom plugin) command[check_disk_health]=/Users/<youruser>/bin/check_smart.sh -d disk0 -g "badSectors,reallocSectors,powerOnHours,tempCelcius,retiredBlockCount,lifetimeWrites,lifetimeReads" # Time Machine (use custom plugin) command[check_timemachine]=/Users/<youruser>/bin/check_time_machine_currency.sh -w 360 -c 720` And restarted NRPE

# Exclusions

I haven&#8217;t covered adding the services to Icinga &#8211; if you&#8217;re comfortable with Icinga and NRPE already, it&#8217;ll be obvious from the command definitions above.

 [1]: http://www.icinga.org "Icinga"
