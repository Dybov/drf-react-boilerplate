export const setLoading = (app) => {
  return {
    type: 'SET_LOADING',
    app,
  }
}

export const setData = (app, data) => {
  return {
    type: 'SET_DATA',
    data,
    app,
  }
}

export const setError = (app, error) => {
  return {
    type: 'SET_ERROR',
    error,
    app,
  }
}

export const resetReduxState = (app) => {
  return {
    type: 'RESET',
    app,
  }
}

export const setUpdateInterval = (app, updateInterval) => {
  return {
    type: 'SET_UPDATE_INTERVAL',
    updateInterval,
  }
}