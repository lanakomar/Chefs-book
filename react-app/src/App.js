import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import { authenticate } from './store/session';
import { setRecipeBox } from './store/recipeBox';
import ProtectedRoute from './components/auth/ProtectedRoute';
import User from './components/User';
import NavBar from './components/NavBar';
import HomePage from './components/HomePage';
import RecipeBox from './components/RecipeBox';
import NotFound from './components/NotFound'
import SingleRecipePage from './components/SingleRecipePage';

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
          dispatch(setRecipeBox(data));
        }
      }
    })();
  }, [dispatch, session])

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
        <ProtectedRoute path='/recipe-box' exact={true} >
          <RecipeBox />
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <ProtectedRoute path='/recipes/:recipeId' exact={true}>
          <SingleRecipePage />
        </ProtectedRoute>
        {/* <ProtectedRoute path='/' exact={true} >
          <h1>My Home Page</h1>
        </ProtectedRoute> */}
        <ProtectedRoute loaded={loaded}>
          <NotFound />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
