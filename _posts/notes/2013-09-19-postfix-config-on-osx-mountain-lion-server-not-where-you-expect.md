---
title: Postfix config on OSX Mountain Lion (Server) not where you expect
author: David
layout: page
permalink: /note/postfix-config-on-osx-mountain-lion-server-not-where-you-expect/
wp-to-buffer-log:
  - 'O:8:"WP_Error":2:{s:6:"errors";a:1:{s:19:"http_request_failed";a:1:{i:0;s:65:"Operation timed out after 5000 milliseconds with 0 bytes received";}}s:10:"error_data";a:0:{}}'
wp-to-buffer:
  - 'a:1:{s:7:"publish";s:1:"1";}'
categories:
  - Note
---
I spent the better part of an hour wondering why my postfix main.cf config changes didn&#8217;t apply on a OSX Mountain Lion server. Turns out that because &#8220;OSX Server&#8221; no longer exists (it&#8217;s just Server.app now), the postfix files specific to the Mail component of the server now live at:

/Library/Server/Mail/Config/postfix/

Which is confusing, since the originals still exist at /etc/postfix

Anyway, files edited, service restarted, config applied!
