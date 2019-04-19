import { withFetching } from './fetch';
import { getCookie } from './cookie';

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
  getCookie,
}

export * from './routes';
export * from './status';
