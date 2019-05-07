import pathToRegexp from 'path-to-regexp';

export const buildPath = (path, params={version: "1"}) => {
  if (!path){
    return "";
  }
  return pathToRegexp.compile(path)(params);
}