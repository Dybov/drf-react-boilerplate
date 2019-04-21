const paths = require('./paths');


let entry_points = {
  main: [
    paths.appIndexJs,
  ],
  // another: [
  //   paths.resolveModuleInCurrentApp('src/another'),
  // ],
}

function build_paths(...conditions) {
  conditions.forEach((condition) => {
    if (condition) {
      for (entry in entry_points) {
        if (condition instanceof Array){
          entry_points[entry].unshift(...condition);
        } else {
          entry_points[entry].unshift(condition);
        }
      }
    }
  })
  return entry_points;
}

module.exports = {
  build_paths,
}