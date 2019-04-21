import { createStore, compose } from "redux";

import personalApp from "./reducers";


export default (preloadedState=undefined) => {
  var enhancers;

  const constantEnhancers = [];

  const onlyProdEnhancers = [];

  const onlyDevEnhancers = [
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
  ];
  
  if (process.env.NODE_ENV === 'development') {
    enhancers = constantEnhancers.concat(onlyDevEnhancers);
  } else if (process.env.NODE_ENV === 'production') {
    enhancers = constantEnhancers.concat(onlyProdEnhancers);
  }

  const composedEnhancers = compose(...enhancers);

  const store = createStore(personalApp, preloadedState, composedEnhancers);

  return store;
}