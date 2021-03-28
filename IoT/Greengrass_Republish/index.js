const ggSdk = require('aws-greengrass-core-sdk');

const iotClient = new ggSdk.IotData();
const os = require('os');
const util = require('util');

function publishCallback(err, data) {
    console.log(err);
    console.log(data);
}

const myPlatform = util.format('%s-%s', os.platform(), os.release());
// Publishing options specifying topic and creating empty payload packet
const pubOpt = {
    topic: 'device/Test_device/messages/devicebound',
    payload: {},
    queueFullPolicy: 'AllOrError',
};

// Populate empty payload packet with event and then publish to previously specified topic
function greengrassHelloWorldRun(event) {
    console.log('Event Received;', event)
    pubOpt.payload = JSON.stringify(event)
    iotClient.publish(pubOpt, publishCallback);
}

// When incoming event received, republish event to specified topic
exports.handler = function handler(event, context) {
    greengrassHelloWorldRun(event);
    console.log(event);
    console.log(context);
};
