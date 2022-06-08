import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { setAllRecipes } from '../../store/recipe';


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
    }, [dispatch])

    return (
        <div>
            {recipesArr?.map(recipe => (
                <div key={recipe.id}>
                    <p>{recipe.title}</p>
                    <p>{recipe.time_to_cook}</p>
                    <div><img width="150px" src={recipe.img_url} alt={recipe.title} /></div>
                </div>
            ))}
        </div>
    )
}

export default HomePage;
