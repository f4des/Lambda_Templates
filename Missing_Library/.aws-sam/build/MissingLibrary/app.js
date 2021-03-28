const fs = require('fs');
var ogr2ogr = require('ogr2ogr');
const testFolder = '/opt/';

exports.handler = async (event) => {
    console.log('## Logging Local Files ##');
    fs.readdirSync(testFolder).forEach(file => {
        console.log(file);
      });

    console.log('## Logging Imported Libraries ##');
    console.log(fs.readdirSync("/opt/lib").filter(p => p.match(/\.so/)).sort().join("\n"));


    var database='missing-db.cpkvauuf3xbl.us-east-1.rds.amazonaws.com'
    var tableName='DEPARTMENT'
    let data = ogr2ogr('/var/task').destination(database)
    .options(['-f "PostgreSQL"', '-nlt PROMOTE_TO_MULTI', 'nln useradministration."' + tableName + '"', '-overwrite']);
    console.log(data);

    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};
