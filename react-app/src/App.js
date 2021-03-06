import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import { authenticate } from './store/session';
import { setRecipeBox } from './store/recipeBox';
import { setGroceryList } from './store/groceryList';
import { setAllRecipes } from './store/recipe';
import { setSavedRecipes } from './store/savedRecipes';
import ProtectedRoute from './components/auth/ProtectedRoute';
import NavBar from './components/NavBar';
import HomePage from './components/HomePage';
import RecipeBox from './components/RecipeBox';
import NotFound from './components/NotFound'
import SingleRecipePage from './components/SingleRecipePage';
import SearchResult from './components/Search/SearchResult';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  const session = useSelector((state) => state.session.user)

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  useEffect(() => {
    (async () => {
      if (session) {
        const res = await fetch(`/api/users/${session.id}/recipes`);
        if (res.ok) {
          const data = await res.json();
          await dispatch(setRecipeBox(data));
        }
      }
    })();
  }, [dispatch, session]);

  useEffect(() => {
    (async () => {
      if (session) {
        const res = await fetch(`/api/recipes`);
        if (res.ok) {
          const data = await res.json();
          await dispatch(setAllRecipes(data));
        }
      }
    })();
  }, [dispatch, session]);

  useEffect(() => {
    (async () => {
      if (session) {
          const groceryList = session.grocery_list;
          const savedRecipes = session.recipes_saved;
          dispatch(setGroceryList(groceryList));
          dispatch(setSavedRecipes(savedRecipes));
      }
    })();
  }, [dispatch, session]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path='/' exact={true}>
          <HomePage />
        </Route>
        <ProtectedRoute path='/recipe-box' exact={true} loaded={loaded}>
          <RecipeBox />
        </ProtectedRoute>
        <ProtectedRoute path='/recipes/:recipeId' exact={true} loaded={loaded}>
          <SingleRecipePage />
        </ProtectedRoute>
        <Route path="/search/:searchQuery" exact={true}>
          <SearchResult />
        </Route>
        <Route path="/404" component={NotFound} />
        <Redirect to="/404" />
      </Switch>
    </BrowserRouter>
  );
}

export default App;
