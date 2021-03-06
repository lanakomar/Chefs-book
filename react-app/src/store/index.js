import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session';
import recipeBox from './recipeBox';
import recipes from './recipe';
import singleRecipe from './singleRecipe';
import groceryList from './groceryList';
import savedRecipes from './savedRecipes';


const rootReducer = combineReducers({
  session,
  recipeBox,
  recipes,
  singleRecipe,
  groceryList,
  savedRecipes
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
