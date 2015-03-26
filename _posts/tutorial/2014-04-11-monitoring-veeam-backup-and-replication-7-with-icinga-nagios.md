---
title: Monitoring Veeam Backup and Replication 7 with Icinga / Nagios
author: David
layout: page
permalink: /tutorial/monitoring-veeam-backup-and-replication-7-with-icinga-nagios/
categories:
  - Tutorial
tags:
  - icinga
  - nagios
  - veeam
---
We&#8217;ve recently deployed a Veeam Backup and Replication 7 platform, and needed to monitor the ongoing success of the backup / replication jobs. I identified a <a title="check_veeam_backups" href="http://exchange.nagios.org/directory/Plugins/Backup-and-Recovery/Others/check_veeam_backups/details" target="_blank">plugin</a> which does **most** of what&#8217;s required, but seems to have 2 current shortcomings: 1. In-progress jobs trigger false warnings 2. Date calculation doesn&#8217;t always work, and produces false warnings

I made the following modifications to check\_veeam\_backups.ps1 to address these: Under

`$status = $job.GetLastResult()`

Add:

`if($($job.findlastsession()).State -eq "Working")<br />
{ Write-Host "OK - Job: $name is currently in progress." exit 0<br />
}`

And then change line #59 from:

`if ($now -gt $last)`

To:

`if(Get-Date $now) -gt (Get-Date $last))`
