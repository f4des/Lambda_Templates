exports.lambdaHandler =  async (event, context, callback) => {
    console.log(`event: ${JSON.stringify(event)}\n`)
    var sleep = require('sleep');
    console.log(' Grabbing Username');
    var uname = event.protocolData.mqtt.username;
    console.log(uname);
    console.log('Grabbing Password');
    var pwd = event.protocolData.mqtt.password;
    console.log(pwd);
    var buff = new Buffer(pwd, 'base64');
    var passwd = buff.toString('ascii');
    sleep.sleep(5)
    switch (passwd) { 
        case 'test': 
            callback(null, generateAuthResponse(passwd, 'Allow')); 
        default: 
            callback(null, generateAuthResponse(passwd, 'Deny'));  
    }
};

// Helper function to generate authorization response
var generateAuthResponse = function(token, effect) {


    var authResponse = {};
    authResponse.isAuthenticated = true;
    authResponse.principalId = 'principalId';

    var policyDocument = {};
    policyDocument.Version = '2012-10-17';
    policyDocument.Statement = [];
    var statement = {};
    statement.Action = 'iot:*';
    statement.Effect = effect;
    statement.Resource = "*";
    policyDocument.Statement[0] = statement;
    authResponse.policyDocuments = [policyDocument];
    authResponse.disconnectAfterInSeconds = 3600;
    authResponse.refreshAfterInSeconds = 600;

    return authResponse;
}
