import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { setAllRecipes } from '../../store/recipe';
import './index.css';


const HomePage = () => {

    const recipes = useSelector((state) => state.recipes);
    const recipesArr = Object.values(recipes);
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
    console.log(recipesArr.length);
    console.log(getRandomIdx(0, recipesArr.length));
    const dayRecipe = recipesArr[getRandomIdx(0, recipesArr.length)]
    console.log(dayRecipe);

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
                    <div key={recipe.id} className="card-container">
                        <div><img src={recipe.img_url} alt={recipe.title} /></div>
                        <h4>{recipe.title}</h4>
                        <div className='time-serv-container'>
                            <p>Time to cook: {recipe.time_to_cook}</p>
                            <p>Servings: {recipe.servings}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default HomePage;
