const os = require('os');

const port = 3000;
var ip;

try {
  // Get IP in local network to allow cross-network requests
  ip = os.networkInterfaces()['wlp3s0'][0]['address'];
} catch (e) {
  // Prevent errors with getting data from networkInterfaces 
  ip = 'localhost';
  console.log('Cannot get IP from os.networkInterfaces().wlp3s0, took "localhost" as IP');
}
const localhost = 'http://' + ip + ':' + port + '/';

module.exports = localhost;
