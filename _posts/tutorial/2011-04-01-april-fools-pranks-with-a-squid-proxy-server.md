---
title: April Fools Pranks with a Squid Proxy Server
author: David
layout: page
permalink: /tutorial/april-fools-pranks-with-a-squid-proxy-server/
aktt_notify_twitter:
  - yes
aktt_tweeted:
  - 1
categories:
  - Tutorial
tags:
  - centos
  - imagemagick
  - perl
  - prank
  - squid
---
## Use Squid to turn the internet upside-down, change Google to Klingon

For this year&#8217;s April Fools Day, I went with the [classic][1] &#8220;turn the internet upside-down&#8221; squid trick, with a few tweaks. I didn&#8217;t want to be too obvious, so I avoided changing images on the majority of Google&#8217; pages, but instead changed the default language to Klingon. Here are the results:

<div id='gallery-1' class='gallery galleryid-1126 gallery-columns-2 gallery-size-thumbnail'>
  <figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://www.funkypenguin.co.nz/wp-content/uploads/2011/04/google_in_klingon.png'><img width="150" height="150" src="https://www.funkypenguin.co.nz/wp-content/uploads/2011/04/google_in_klingon-150x150.png" class="attachment-thumbnail" alt="Set Google&#039;s language to &quot;Klingon&quot;" aria-describedby="gallery-1-1127" /></a>
  </div><figcaption class='wp-caption-text gallery-caption' id='gallery-1-1127'> Set Google&#8217;s language to &#8220;Klingon&#8221; </figcaption></figure><figure class='gallery-item'> 
  
  <div class='gallery-icon landscape'>
    <a href='https://www.funkypenguin.co.nz/wp-content/uploads/2011/04/images_upside_down.png'><img width="150" height="150" src="https://www.funkypenguin.co.nz/wp-content/uploads/2011/04/images_upside_down-150x150.png" class="attachment-thumbnail" alt="Turn random (but not all) images upside-down" aria-describedby="gallery-1-1128" /></a>
  </div><figcaption class='wp-caption-text gallery-caption' id='gallery-1-1128'> Turn random (but not all) images upside-down </figcaption></figure>
</div>

It&#8217;s easy and fun to do, and you get to learn a bit about Squid, perl, and regular expressions. Here&#8217;s how it&#8217;s done:<!--more-->

## Squid, Apache, and ImageMagick

We use CentOS on our systems, so these examples assume default paths etc, but can easily be modified to your own environment.

  * Squid : &#8220;*yum install squid*&#8221; &#8211; I already had this in place, so I&#8217;m not going to cover setting up Squid Proxy. Obviously, this trick works best if you&#8217;re using it for transparent proxying
  * Apache : &#8220;*yum install apache*&#8221; &#8211; This is needed to serve the modified images back to the victim
  * ImageMagick : &#8220;*yum install ImageMagick*&#8221; &#8211; This is needed for the &#8220;mogrify&#8221; command, which turns the images upside-down

## Redirector configuration in squid.conf

I configured Squid to classify my &#8220;victim&#8221; as &#8220;browser\_firefox&#8221; or &#8220;browser\_ie&#8221;, based on their user-agent header. (I also turned on logging of user agent headers so I could tweak this). Then using the &#8220;url\_rewrite\_access&#8221; directive, I could selectively target my victims. Note that inverse matches (i.e., &#8220;!browser_firefox&#8221;) also work here.

<pre>acl browser_firefox browser Mozilla
acl browser_ie browser MSIE
url_rewrite_access allow LOADBALANCER
url_rewrite_program /etc/squid/aprilfoolsprank.pl
url_rewrite_bypass on
url_rewrite_children 1
useragent_log /var/log/squid/useragent.log</pre>

I configured Squid to classify my &#8220;victim&#8221; as &#8220;browser\_firefox&#8221; or &#8220;browser\_ie&#8221;, based on their user-agent header. (I also turned on logging of user agent headers so I could tweak this). Then using the **url\_rewrite\_access** directive, I could selectively target my victims. Note that inverse matches (i.e., &#8220;!browser_firefox&#8221;) also work here.

The **url\_rewrite\_bypass** directive tells squid not to wait for free redirector children, but to bypass the redirector rather than allowing it to become a bottleneck. I did this to (a) avoid tipping off the victims, and (b) I figured a random few upside images on a website, as opposed to every image, would be more subtle. As my victims started noticing the prank effects, I gradually increased the amount of **url\_rewrite\_children** from 1 to 3.

## Perl script to invert images and other mischief

I created /etc/squid/aprilfoolsprank.pl as follows:

<pre>#!/usr/bin/perl
$|=1;
$count = 0;
$pid = $$;
while (&lt;&gt;) {
 chomp $_;
 # Allow google static content, unmolested
 if ($_ =~ /(.*gstatic.*)/i) {
 $url = $1;
 print "$url\n";

 }
 # Change google language to Klingon
 elsif ($_ =~ /(.*google.*)/i) {
 $url = $1;
 $url =~ s/hl=en/hl=xx-klingon/;
 print "$url\n";

 }
 elsif ($_ =~ /(.*\.jpg)/i) {
 $url = $1;
 system("/usr/bin/wget", "-q", "-O","/var/www/html/images/$pid-$count.jpg", "$url");
 system("/usr/bin/mogrify", "-flip","/var/www/html/images/$pid-$count.jpg");
 print "http://127.0.0.1/images/$pid-$count.jpg\n";
 }
 elsif ($_ =~ /(.*\.gif)/i) {
 $url = $1;
 system("/usr/bin/wget", "-q", "-O","/var/www/html/images/$pid-$count.gif", "$url");
 system("/usr/bin/mogrify", "-flip","/var/www/html/images/$pid-$count.gif");
 print "http://127.0.0.1/images/$pid-$count.gif\n";

 }
 elsif ($_ =~ /(.*\.png)/i) {
 $url = $1;
 system("/usr/bin/wget", "-q", "-O","/var/www/html/images/$pid-$count.png", "$url");
 system("/usr/bin/mogrify", "-flip","/var/www/html/images/$pid-$count.png");
 print "http://127.0.0.1/images/$pid-$count.png\n";

 }
 else {
 print "$_\n";;
 }
 $count++;
}</pre>

Each successive &#8220;if&#8221; statement checks the requested URL against a regular expression, and if it matches, performs some tricky on it. Because we&#8217;re using &#8220;if&#8221; statements, the first match wins. The first stanza avoids upside-downing google&#8217;s static content (because we don&#8217;t want to tip anybody off by making search results look weird), and the following one changes the default language from english to Klingon. (You can substitue any value here, just search for &#8220;google whatever-country&#8221;, and identify the &#8220;hl=xx&#8221; string used).

The final 3 stanzas perform the classic &#8220;flip&#8221; action using ImageMagick&#8217;s mogrify.

&nbsp;

 [1]: http://www.ex-parrot.com/pete/upside-down-ternet.html
