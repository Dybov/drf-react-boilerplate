import { withFetching } from './fetch';

import {
  FetchOnComponentwWillMount,
  FetchOnComponentDidMount,
} from './components';


var willMountWithFetching = withFetching(FetchOnComponentwWillMount);
var didMountWithFetching = withFetching(FetchOnComponentDidMount);


export {
  willMountWithFetching as default,

  willMountWithFetching,
  didMountWithFetching,
}

export * from './cookie';
export * from './routes';
export * from './status';
