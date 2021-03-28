var mysql = require('mysql');
var config = require('./config.json');
var connection = mysql.createConnection({
    host: process.env.RDS_HOST,
    user: process.env.RDS_USER,
    password: process.env.RDS_PASSWORD,
    database: process.env.RDS_NAME
});
exports.handler =  (event, context, callback) => {
  //prevent timeout from waiting event loop
  context.callbackWaitsForEmptyEventLoop = false;
  connection.connect(err => {
    if (err) {
        console.error('error connecting: ' + err.stack)
        callback(null)
    }
    console.log('connected as id: ' + connection.threadId)
    });
    connection.end(err => {
        if (err) console.error('error closing connection: ' + err.stack)
        console.log('connection closed')
        callback('done')
    }); 
};