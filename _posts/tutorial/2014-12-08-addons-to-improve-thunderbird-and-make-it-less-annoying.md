---
title: Addons to improve Thunderbird (and make it less annoying)
author: David
layout: page
permalink: /tutorial/addons-to-improve-thunderbird-and-make-it-less-annoying/
categories:
  - Tutorial
tags:
  - featured
  - markdown
  - productivity
  - thunderbird
---
My organization standardizes on Mozilla Thunderbird as our mail client of choice (partly because Mail.app is so [deficient][1] on OSX). It&#8217;s a bit crusty since Mozilla [halted further development][2] in 2012, but better the devil you know, right&#8230;?

I recently had some downtime while waiting for gingerbread houses to be cooked (long story!), and spent some time identifying fixes for 2 of my everyday annoyances. I include them below, plus some neat improvements I&#8217;ve stumbled across over time.

## How do you annoy me? Let me count the ways&#8230; {#howdoyouannoymeletmecounttheways}

### Stop sending personal emails to my boss {#stopsendingpersonalemailstomyboss}

I have multiple email accounts on my laptop (Thunderbird) and my iPhone. I&#8217;ve always liked how the Mail.app on the iPhone auto-selects my sending address based on the recipient of a new message I create. I email my boss, it defaults to my work account. I email my wife, it defaults to my private account.

Having become accustomed to this behavior, I&#8217;ve accidentally sent email from the wrong account several times in Thunderbird, which has no such smarts. Outgoing emails are defaulted to the account associated with the folder I happen to be viewing at the time. So if I&#8217;ve been reading my personal email, and compose a new email to my boss, I have to remember to manually change the identity to my work account.

The [Correct Identity][3] add-on solves this. It lets you set text which is matched against recipient email addresses, allowing you to set your preferred sending account for your work domain, customers, etc. The plugin can also be configured to **warn** you when sending to that set of addresses from another account.

### Stop messing up my fonts {#stopmessingupmyfonts}

It&#8217;s bothered me for years that when I paste formatted content into a message in Thunderbird, the content is pasted with its font, which then becomes the default font for the rest of my message. To work around this, I used to have to type contents before and after the location I wanted to paste text, to avoid loosing my default formatting, or paste-and-copy via a plain-text editor first.

The solution is stupidly simple. **When pasting formatted content, use SHIFT-COMMAND-V to paste without formatting**. (Yes, this is also in the edit menu)

Secondly, Thunderbird behaves badly with font sizes. Fix it with the [Quote and Compose Manager][4]{.broken_link} add-on, which &#8220;stabilizes&#8221; your compose font, among other tweaks. I&#8217;ve set mine to Tahoma 16-point, after reading about how it&#8217;s the [most accessible size][5].

## What have you done for me lately? {#whathaveyoudoneformelately}

### Let me write in markdown {#letmewriteinmarkdown}

[I don&#8217;t always][6] send marked-up text, but when I do, I want to be able to apply formatting:

  * without moving my mouse 
  * with more precision than Thunderbird&#8217;s editor permits (i.e., explicitly setting heading levels) 
  * with more options than Thunderbird&#8217;s editor includes (horizontal lines, nested bullets, etc)

I.e., I want to mark up my emails in [Markdown][7] syntax.

There are a few bleeding-edge mail clients which natively support Markdown, but as far as I can tell, they all support it with a split-screen interface.The [Markdown Here][8] [add-on][9] lets you switch your message from native to markdown with a shortcut key, which I find preferable to the split-screen. I don&#8217;t have to do any clicking to write in markdown, but it stays out of my way when I don&#8217;t want it.

### Send emails to Evernote with one key {#sendemailstoevernotewithonekey}

The [EnForward][10] add-on can be configured with a shortcut key to send an email to your personal Evernote email address

### Why can&#8217;t you be more like Gmail? {#whycantyoubemorelikegmail}

The [Thunderbird Conversations][11] add-on makes Thunderbird format your messages and threads more like Gmail. It&#8217;s certainly a more attractive way of viewing messages. I&#8217;ve been using it for 1-2 years, and wouldn&#8217;t want to go without it.

 [1]: https://discussions.apple.com/thread/4742212
 [2]: http://www.zdnet.com/article/mozilla-scraps-thunderbird-development-email-client-not-a-priority-anymore/
 [3]: https://addons.mozilla.org/en-us/thunderbird/addon/correct-identity/
 [4]: https://freeshell.de/~kaosmos/quoteandcomposemanager-en.html
 [5]: http://www.smashingmagazine.com/2011/10/07/16-pixels-body-copy-anything-less-costly-mistake/
 [6]: http://knowyourmeme.com/memes/the-most-interesting-man-in-the-world
 [7]: https://guides.github.com/features/mastering-markdown/
 [8]: http://markdown-here.com/
 [9]: https://addons.mozilla.org/en-us/thunderbird/addon/markdown-here/
 [10]: https://addons.mozilla.org/en-US/thunderbird/addon/enforward/?src=cb-dl-mostpopular
 [11]: https://addons.mozilla.org/en-US/thunderbird/addon/gmail-conversation-view/
