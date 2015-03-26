---
title: Convert a .BIN file to .TRX for OpenWRT / DD-WRT
layout: page
redirect_from: /tutorial/how-to-convert-a-bin-file-to-trx-for-openwrt-dd-wrt/
permalink: /how-to/convert-a-bin-file-to-trx-for-openwrt-dd-wrt/
categories:
  - how-to
tags:
  - openwrt
---
I recently had reason to convert the latest DD-WRT firmware .bin file to .trx format, so that I could manually flash my WRT54GL. Not wanting to risk it, I first converted the .bin image with the following command:

    dd if=firmware.bin of=firmware.trx bs=32 skip=1

Which I found [here][1].

 [1]: http://www.openlinksys.info/forum/viewthread.php?forum_id=37&thread_id=919
