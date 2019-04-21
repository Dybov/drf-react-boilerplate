import { combineReducers } from 'redux';
import api from "./api";


const personalApp = combineReducers({
  api,
});


export default personalApp