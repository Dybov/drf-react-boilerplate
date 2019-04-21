import React, { Component } from 'react';


/* Main fetching component
 * handles fetching and provides api data inside child component
 */ 
class FetchComponent extends Component {
  constructor(props){
    super(props);
    this.getApi = this.getApi.bind(this);
    this.processData = this.processData.bind(this);
  }

  /* Provides api Redux state
   * or return empty object for compatibility
   * that allows to use this func as data
   * without checking that props.api exists
   */
  getApi(){
    if (!this.props.api){
      return {};
    }
    return this.props.api;
  }

  fetchData() {
    let {updated, updateInterval} = this.getApi();

    /* Prevent from fetching new data */
    if (
      updated
      && (Date.now()-updated) < updateInterval
    ){
      return;
    }

    this.props.setLoading();

    let {url, options} = this.props;

    fetch(url, options)
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Something went wrong ...');
        }
      })
      .then(this.processData)
      .catch(error => this.props.setError(error));
  }

  processData(data){
    const preprocess = this.props.preprocessData;
    if (typeof preprocess==='function'){
      data = preprocess(data);
    }
    this.props.setData(data);
  }

  render() {
    var props = Object.assign({getApi:this.getApi}, this.props);
    let {isLoading} = this.getApi()
    const ProvidedComponent = props.child;
    const LoadingComponent = props.loadingComponent;

    if (!ProvidedComponent){
      return null;
    }

    if (isLoading === true
        && LoadingComponent !== undefined){
      if (LoadingComponent instanceof Function) {
        return <LoadingComponent />;
      }
      return LoadingComponent;
    }

    delete props.child;
    delete props.url;
    delete props.options;
    delete props.parent;
    delete props.api;

    return <ProvidedComponent { ...props } />;
  }
}

export default FetchComponent
