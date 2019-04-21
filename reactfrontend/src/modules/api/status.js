function beetween(value, min_, max_){
  return (
    (min_ <= value)
    && (value < max_)
  );
}

function isInformational(status){
  return beetween(status, 100, 200)
}

function isSuccess(status){
  return beetween(status, 200, 300)
}

function isRedirect(status){
  return beetween(status, 300, 400)
}

function isClientError(status){
  return beetween(status, 400, 500)
}

function isServerError(status){
  return beetween(status, 500, 600)
}

export {
  isInformational,
  isSuccess,
  isRedirect,
  isClientError,
  isServerError,
}