'use strict';

var ttn = require('ttn');

var appEUI = '';
var accessKey = '';

//var client = new ttn.Client('staging.thethingsnetwork.org', appEUI, accessKey);
var client = new ttn.Client('toast.is.ed.ac.uk', appEUI, accessKey);

client.on('connect', function () {
	console.log('[DEBUG]', 'Connected');
});

client.on('error', function (err) {
	console.error('[ERROR]', err.message);
});

client.on('activation', function (e) {
	console.log('[INFO] ', 'Activated: ', e.devEUI);
});

client.on('uplink', function (msg) {
	var pload = msg["fields"]["raw"];
        if (msg.counter % 10 === 0) {
		console.info('[INFO] ', 'Uplink: ' + JSON.stringify(msg, null, 2));
	}
//	console.log('  Payload: ' + pload);
	console.log('Payload: ' + new Buffer(pload, 'base64').toString('ascii'));
});

client.on('message', function(deviceId, data) {
    console.info('[INFO] ', 'Message:', deviceId, JSON.stringify(data, null, 2));
});

client.on('uplink', function (msg) {

	// respond to every third message
	if (msg.counter % 10 === 0) {
		console.log('[DEBUG]', 'Downlink');

		//var payload = new Buffer('4869', 'hex');
		//client.downlink(msg.devEUI, payload);
	}
});
