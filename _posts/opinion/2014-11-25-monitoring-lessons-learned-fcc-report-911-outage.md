---
title: IT Monitoring lessons learned from FCC report into 911 outage
author: David
layout: page
permalink: /opinion/monitoring-lessons-learned-fcc-report-911-outage/
categories:
  - Opinion
tags:
  - featured
  - monitoring
---
[IEEE Spectrum][1] highlighted an [FCC report][2] into a 911 outage in April 2014, which resulted in over 11 million Americans.. or about three and half percent of the population of the United States, being at risk of not being able to reach emergency help through 911.

I found the report interesting in the parallels to the (less life-threatening) issues we routinely deal with at [Prophecy Networks][3]. I&#8217;ve detailed some recommendations to mitigate some of these issues below, and then have commented on the pertinent sections in the report

Within [Prophecy][3], we:

  * Implement [automated monitoring][4], including severity and escalation levels, so that unhandled alerts are escalated to backup engineers and management based on severity and SLA response time 
  * Send escalation alerts at different levels via independent messaging platforms (e.g. [SMS][4] and [Pushover][5]), to guard against a single &#8220;silent&#8221; failure
  * Run multiple monitoring platforms, each monitoring the other, so that a failure of the monitoring platform itself creates alerts
  * Where possible, monitor intended behaviour (&#8220;[are emails delivered?][6]&#8220;) rather than specific processes (&#8220;is sendmail running?&#8221;) to avoid the trap of only monitoring predicted failures.
  * Use a simple set of [mailing lists][7] to quickly delivery status updates via email and txt to staff, customers and partners during an outage

On to my interpretation of the FCC investigative report&#8230;

The root-cause of the 911 outage was a preventable software error:

> In this case, the trunk assignment counter reached a pre-set capacity limit to assign trunks, which meant that no additional database entries to reserve a PSAP CAMA trunk could be created, no trunk assignments for call delivery could be made for PSAPs with CAMA trunks22 and, therefore, no 911 calls could be completed to these PSAPs or any backup PSAP through the Englewood ECM

The fault was mis-classified from a monitoring perspective:

> &#8230;a full hour after the counter had reached its threshold, low-level alarms began to go off at the Englewood, Colorado ECMC. The alarms were automatically categorized by the server monitoring logs as “low level,” and personnel at the ECMC appear to have realized neither what had failed nor the severity of the problem.

This mis-classification was a default setting:

> The low-level designation was a default setting accepted by Intrado’s System Administrator that, in hindsight, did not reflect the potential severity of the fault.

Unrelated issues obscured the source of the fault, and produced a mis-diagnosis:

> In the first few hours, Intrado was responding to a series of individual PSAP incidents and an area network outage in Oregon that was later determined unrelated&#8230;. Moreover, for several hours Intrado was unable to identify the root cause of the failure to deliver 911 calls to the appropriate PSAP. For at least a portion of that time, Intrado and CenturyLink were also dealing with a separate and simultaneous 911 outage on CenturyLink’s network in northern Oregon, leading to a misdiagnosis of the actual problem for a period of that time. The Oregon outage ultimately proved unrelated to the Washington outage, but for several hours early on April 10, Intrado and CenturyLink worked under the mistaken impression that the Washington and Oregon outages were related. As Intrado noted in its publicly-filed reply comments, this diverted its attention from the true cause of the multi-state outage.

It ultimately took manual (human) communications to finally alert staff to the severity of the issue, after failure of the automated systems:

> It appears that Intrado was not able to fully understand the significance and breadth of the problem until around 2:00 a.m. PDT, when CenturyLin informed it that CenturyLink’s PSAP customers in the State of Washington were suffering an outage.

The fault was a &#8220;silent failure&#8221;:

> NORS reports showed that Intrado had redundant capability to reroute 911 traffic through its Miami ECMC, but the Englewood outage was a “silent failure” that, due to a “low-level fault” designation, did not trigger automatic rerouting.

The architecture of the system was partly to blame for the massive breath of impact:

> Finally, the enormous breadth of the outage was in part attributable to an architecture that consolidated critical 911 functions in two locations serving multiple states, without adequate safeguards in place.

Consolidating 911 routing operations, while producing a cost-saving in terms of operational overhead, introduced an undesirable amount of fragility into the system:

> While this consolidation lowered the cost of 911 operations for the LEC, the outage clearly showed that consolidation can result in too much dependence on a few critical elements if providers do not ensure the effective operation of adequate diversity and redundancy in the design and execution of the network.

Communication to customers and partners during the outage was inadequate:

> Notably, the IPSR did not issue any major or critical alarm for this outage. Instead, it issued several thousand minor alarms for calls not completing, but these did not attract the attention of Intrado staff.

Minor secondary alarms created additional noise, which decreased the effect of the (already misclassified) alarms. Additionally, consolidation of alarm data resulted in further misclassification of the severity of the issue.

> The failure did generate an alarm, but the alarm was not distinguishable as a failure to process calls. Because of this, [Intrado] did not recognize the significance of the problem. In addition, even though the device that failed sent 4,500 alarms to [Intrado’s Englewood office], they were grouped together in a summary, so again, the significance of the problem was not recognized by [Intrado].

Involving multiple parties in the operation of a platform complicates the process of detection and resolution of faults:

> While the technical cause of this multistate outage rested in Intrado’s network, operations and maintenance for 911 communications generally was distributed among multiple communications providers. This complicated the process of detecting and repairing problems.

We increase the robustness of a system by establishing monitoring based on past failures:

> Intrado implemented a number of new features to fix the original problem with the PTM and to prevent recurrence of the same or similar problems. The most important changes include significantly increasing the PTM counter limit for both ECMCs (i.e., in Englewood and in Miami) to reduce the possibility of reaching the maximum threshold, and checking the PTM counter value weekly to ensure the value is not nearing the higher, maximum threshold;

Monitoring for anomolies in the intended behavior of a system as a whole, rather than just the individual components:

> &#8230;Creating an alarm “based on percentage of successful calls processed on a given ECMC compared to total calls for that ECMC over a 15-minute sample period.” Thus, in the future, whenever the ECMC stops processing calls, regardless of the reason, the failure should generate an immediate alarm; and

Automating redundancy and graceful failover where this does not further increase the complexity and fragility of the system:

> Implementing a change to automatically reroute an individual call to another ECMC if for some reason that call cannot be processed at its primary ECMC. This change permits 911 calls in the NG911 transition architecture to route to an available server as is commonly found in a distributed Internet service.

Sometimes the efforts taken to reduce costs (in this case, consolidation, but there&#8217;s an obvious parallel to virtualization of server and network infrastructure) can result in unexpected fragility of the system

> With the transition to NG911 system implementation, new entrants have already begun to enter the market for the provision of key functional services, and the entry of specialized providers has the potential to promote innovation. Sometimes “innovation” leads to lower operating costs through efficiencies made possible by consolidating operations into fewer facilities. However, such consolidation can greatly multiply the impact from a single or dual point of failure.

In summary, building too fast or or too &#8220;clever&#8221; can result in catastrophic failure of complex systems:

> The April 2014 multistate outage was far more than a simple software error on an otherwise uneventful spring evening in Englewood, Colorado. It was a vivid example of the vulnerabilities that IP-supported architectures may present, without sufficient network safeguards and clear lines of accountability. The issues raised in the outage go to the heart of providing reliable 911 service.

 [1]: http://spectrum.ieee.org/riskfactor/computing/it/-fcc-chairman-calls-aprils-seven-state-sunny-day-911-outage-terrifying-
 [2]: http://www.fcc.gov/document/april-2014-multistate-911-outage-report
 [3]: http://www.prophecy.net.nz
 [4]: http://www.clickatell.com
 [5]: http://www.pushover.net
 [6]: http://exchange.nagios.org/directory/Plugins/Email-and-Groupware/check_email_delivery/details
 [7]: http://www.gnu.org/software/mailman/
