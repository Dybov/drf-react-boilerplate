// Initial state for api reducers
var initialState = {
  updated: null,
  updateInterval: 60*60*60,
  data: null,
  isLoading: false,
  error: null,
};

const apiReducer = (state=initialState, action) => {
  let updated = Date.now();
  let isLoading = false;

  switch (action.type) {
    case "SET_LOADING":
      return {
        ...state,
        updated,
        isLoading: true,
      };

    case "SET_DATA":
      return {
        ...state,
        error: null,
        data: action.data,
        updated,
        isLoading,
      };

    case "SET_ERROR":
      return {
        ...state,
        error: action.error,
        data: null,
        updated,
        isLoading,
      };

    case "RESET":
      return initialState;

    case "SET_UPDATE_INTERVAL":
      return {
        ...state,
        updateInterval: action.updateInterval,
      }

    default:
      return state;
  }
};

/* Complicated reducer which allows to combine the same
 * reducers and store their states inside this one
 */
const appsReducer = (state={}, action) => {
  const { app, ...rest } = action;
  if (app) {
    return {
      ...state,
      [app]: apiReducer(state[app], rest)
    };
  }

  return state;
};


export default appsReducer
