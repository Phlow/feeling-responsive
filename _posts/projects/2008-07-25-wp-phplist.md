---
title: WP-PHPList
author: David
excerpt: The WP-PHPlist plugin integrates PHPList into your Wordpress blog, giving you all the mailing list power of PHPList, within the beautiful styling, theme, and widgets of your Wordpress theme.
layout: page
permalink: /project/wp-phplist/
btc_comment_counts:
  - 'a:0:{}'
aktt_notify_twitter:
  - no
btc_comment_summary:
  - 'a:0:{}'
bttc_cache:
  - 1291018455:3
wp-to-buffer-error:
  - 1
categories:
  - Projects
tags:
  - phplist
  - wordpress
---
The [WP-PHPlist plugin][1] integrates PHPList into your WordPress blog, giving you all the mailing list power of PHPList, within the beautiful styling, theme, and widgets of your WordPress theme. This tutorial will take you through the installation of the plugin, assuming that you&#8217;re starting with a vanilla install of PHPList. <!--more-->

## Getting Started

What you&#8217;ll need to start:

  * A working, un-modified <a title="PHPlist" href="http://www.phplist.com/" target="_blank">PHPList</a> installation (2.10.10 is the latest)
  * A working <a title="Wordpress" href="http://www.wordpress.org/" target="_blank">WordPress</a> installation with pretty permalinks enabled (any version)
  * The corresponding <a title="WP-PHPList plugin" href="https://github.com/funkypenguin/wp-phplist" target="_blank">WP-PHPList plugin</a> (2.10.10 is the latest)
  * Best results with PHPList and WordPress sharing one database (using their default wp_ and phplist_ prefixes)

Unpack the wp-phplist plugin zipfile. You should see the following files and folders:

  * lists
  * wp-phplist
  * README.TXT
  * phplist-2.10.10.patch

## PHPList modifications for WP-PHPList

Copy the contents of the &#8220;lists&#8221; folder into your PHPList &#8220;lists&#8221; folder. The objective is to overwrite the following files:

  * lists/index.php
  * lists/admin/commonlib/lib/userlib.php
  * lists/admin/processqueue.php
  * lists/admin/subscribelib2.php

WARNING &#8211; If you&#8217;ve made modifications to your PHPList installation, this may overwrite those modifications, and BREAK IT. I&#8217;ve provided a diff (phplist-2.10.8.patch) in case you want to manually update PHPList.

Make sure your PHPList installation is setup correctly, required path and URL configuration settings are correct, etc. Also, make sure that you have at least one active list, else the plugin won&#8217;t display anything.

## WordPress installation for WP-PHPList

Make sure you have &#8220;Pretty Permalinks&#8221; enabled in WordPress. WP-PHPList uses this to cretae the &#8220;slug&#8221; below.

Copy the &#8220;wp-phplist&#8221; folder into your WordPress wp-content/plugins folder. You must end up with the folder structure wp-content/plugins/wp-phplist/.

Activate the plugin in WordPress, and double-check the options under Admin -> Options -> PHPList.

  * **PHPList public pages slug** : The WordPress &#8220;slug&#8221; you want PHPList to be accessible as, for example: http://your.blog.com/newsletter.
  * **PHPList default subscribe page** : PHPList lets you define multiple subscribe pages, each requesting different information from users, and making different lists available. Enter the number of the subscribe page you want to use (default is 1), or leave it blank to let PHPList prompt you.
  * **PHPList embedded page title** : The title WordPress will display on PHPList&#8217;s page. (Formatted the same as a default blog post title)
  * **PHPList relative path** : The path to your PHPList &#8220;lists&#8221; directory, relative to your WordPress root. By default the plugin assumes that the &#8220;lists&#8221; directory is a subdirectory of your WordPress install. If PHPList is installed in the same directory as WordPress, this will be &#8220;../phplist&#8221;.

## Test PHPList in WordPress

That&#8217;s it. Go to http://yourblog/slug (*you chose the slug above*) and check that it works.

Remember to change your subscribe / unsubscribe / confirmation URLs in PHPList to reflect the new path that your users will use (*http://yourblog/slug/?p=confirm, for example*).

## Caveats

### Theme Integration

The &#8220;wp-phplist/wp-phplist-page.php&#8221; is based on the default template&#8217;s &#8220;single.php&#8221; file. Your template may use other CSS class values, and you&#8217;ll need to adjust &#8220;wp-phplist-page.php&#8221; accordingly.

### Shared Databases

You&#8217;ll get best results if your WordPress and PHPList installations share a single database. It may be easy to avoid, but it seems like if you start pulling values from PHPList&#8217;s independent database, a bunch of the queries that WordPress uses for its template will fail. You&#8217;ll see messages like this:

WordPress database error Table &#8216;newsletter\_phplist.wp\_terms&#8217; doesn&#8217;t exist for query SELECT t.\*, tt.\* FROM wp_terms..

Combining your databases shouldn&#8217;t be a problem, since PHPList defaults to a table prefix of &#8220;phplist\_&#8221;, and WordPress to &#8220;wp\_&#8221;.

### PHPList standalone

We&#8217;ve &#8220;broken&#8221; the PHPList index file, which displays your subscribe pages, to make it fit into your blog. If you still want to use PHPList&#8217;s interface **as well as** the interface within WordPress, you&#8217;ll probably want another (unaltered) copy of lists/index.php.

Let&#8217;s assume you call it &#8220;index\_for\_wordpress.php&#8221;. Edit wp-content/plugins/wp-phplist/wp-phplist-page.php, look for &#8220;index.php&#8221;, and change it to &#8220;index\_for\_wordpress.php&#8221;.

## Optional extra

Using <a title="Urban Giraffe" href="http://urbangiraffe.com/" target="_blank">Urban Giraffe</a>&#8216;s **awesome** <a title="Urban Giraffe's Redirection Plugin" href="http://urbangiraffe.com/plugins/redirection/" target="_blank">Redirection</a> plugin, you can add the following redirection rules for some cosmetic improvements on your unsubscribe / preferences links:

  * /member/preferences\?(.*)$ &#8211;> /member/?p=preferences&$1 (301 redirect, with regex enabled)
  * /member/unsubscribe\?(.*)$ &#8211;> /member/?p=unsubscribe&$1 (301 redirect, with regex enabled)

This means that I can now modify my unsubscribe / preferences links in PHPList to [http://example.com/member/unsubscribe/?id=whatever][2] &#8211; not a big deal maybe, but in my case, I had a few years of historical links pointing to these sorts of URLs, and the redirection plugin was ideal. (And a good idea for anyone interested in SEO on WordPress)

**Download**

WP-PHPList is hosted at <a title="GitHub" href="https://github.com/funkypenguin/wp-phplist" target="_blank">GitHub</a> now.

 [1]: https://github.com/funkypenguin/wp-phplist
 [2]: http://example.com/member/unsubscribe/?id=whatever "http://example.com/member/unsubscribe/?id=whatever"
