import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';

import { setAllRecipes } from '../../store/recipe';
import './index.css';


const HomePage = () => {

    const history = useHistory();
    const recipes = useSelector((state) => state.recipes);
    const recipesArr = Object.values(recipes).sort(function (a, b) {
        return b.id - a.id;
    });
    const dispatch = useDispatch();

    useEffect(() => {
        (async () => {
            const res = await fetch(`/api/recipes`);
            if (res.ok) {
                const data = await res.json();
                dispatch(setAllRecipes(data));
            }
        })();
    }, [dispatch]);

    function getRandomIdx(min, max) {
        return Math.floor(Math.random() * (max - min) + min);
    }

    const dayRecipe = recipesArr[getRandomIdx(0, recipesArr.length)]

    const cardClick = (e) => {
        const recipeId = e.currentTarget.id;
        history.push(`/recipes/${recipeId}`)
    }

    return (
        <div className='home-page-container'>
            <div
                style={{ backgroundImage: `url(${dayRecipe?.img_url})` }}
                className='day-recipe'>
                <div className='day-recipe-card'>
                    <div className='badge'><p>RECIPE OF THE DAY</p></div>
                    <h3>{dayRecipe?.title}</h3>
                    <p>{dayRecipe?.description}</p>
                </div>
            </div>
            <div className='recipes-container'>
                {recipesArr?.map(recipe => (
                    <div key={recipe.id} id={recipe.id} className="card-container" onClick={cardClick}>
                        <div className='image-container' style={{ backgroundImage: `url(${recipe?.img_url})` }}></div>
                        <h4>{recipe.title}</h4>
                        <div className='time-serv-container'>
                            <p>Time: {recipe.time_to_cook}</p>
                            <p>Servings: {recipe.servings}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default HomePage;
