exports.handler = async (event) => {
    console.log("## EVENT RECEIVED ##");
    console.log(event);
    console.log('## EVENT HEADERS ##');
    console.log(event.headers)
    var Auth = event.headers.Authorization
    console.log('## Authorization Header ##');
    console.log(event.headers.Authorization)
    const response = {
        statusCode: 302,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': true,
            'Location': 'REDIRECT-URL',
            'Set-Cookie': 'authorizationToken=' + Auth,
            'httpMethod': 'GET',
            
        },
    };
    return response;
};
