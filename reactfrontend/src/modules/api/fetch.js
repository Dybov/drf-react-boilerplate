import pathToRegexp from 'path-to-regexp';
import {connect} from 'react-redux';

import routes from './routes';
import {getMapStateToProps, getMapDispatchToProps} from './mapToProps';


import {DefaultLoading} from './components';


const defaultFetchOptions = {
  headers: {'Accept': 'application/json'}
}


export function withFetching(FetchingComponent){
  return (api_route_name, options=defaultFetchOptions, api_version='v1', params={}) => {
    var raw_api_url = routes[api_route_name]
    var url = pathToRegexp.compile(raw_api_url)(
      {
        ...params,
        version: api_version,
      }
    )

    let stateToProps = getMapStateToProps(api_route_name);
    let dispatchToProps = getMapDispatchToProps(api_route_name);

    return (
      ProvidedComponent,
      LoadingComponent=DefaultLoading,
      mapStateToProps=stateToProps,
      mapDispatchToProps=dispatchToProps,
      preprocessData=undefined,
    ) => {
      return connect(
        mapStateToProps,
        mapDispatchToProps
      )(class APIFetching extends FetchingComponent {
        static defaultProps = {
          url,
          options,
          child: ProvidedComponent,
          parent: FetchingComponent,
          loadingComponent: LoadingComponent,
          preprocessData: preprocessData,
        } 
      });
    }
  }
}
