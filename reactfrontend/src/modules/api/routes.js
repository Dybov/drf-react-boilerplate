const GET_PATH_URL = '/api/v1/react-paths/';

var routes = {};

var request = new XMLHttpRequest();
request.open('GET', GET_PATH_URL, false);  // `false` makes the request synchronous
request.setRequestHeader('Accept', 'application/json');  // `false` makes the request synchronous
request.send(null);

if (request.status === 200) {
  routes = JSON.parse(request.responseText);
} else {
  // throw Error('Bad request while getting routes')
}

export default routes
