import {api as api_actions} from '../../actions/';


export function getMapStateToProps(app){
  return  state => {
    return {
      api: state.api[app],
    }
  }
}


export function getMapDispatchToProps(app){
  return dispatch => {
    return {
      setLoading: () => {dispatch(api_actions.setLoading(app))},
      setData: (data) => {dispatch(api_actions.setData(app, data))},
      setError: (error) => {dispatch(api_actions.setError(app, error))},
      resetReduxState: () => {dispatch(api_actions.resetReduxState(app))}
    }
  }
}