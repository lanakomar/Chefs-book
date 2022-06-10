import { useState } from 'react';

import CreateRecipeModal from "../CreateRecipeModal";
import EditRecipeModal from "../EditRecipeModal";
import './index.css'

const RecipeCard = ({ recipe }) => {
    return (
        <div className="card-container">
            <div className='img-container'>
                <img src={recipe.img_url} alt={recipe.title} />
                <div className='delete-recipe'>
                    <i className="fa-solid fa-square-xmark" />
                </div>
            </div>
            <h4>{recipe.title}</h4>
            <div className='edit-recipe'>
                <EditRecipeModal id={recipe.id} />

                {/* <i className="fa-solid fa-file-pen" /> */}
            </div>
            <div className='time-serv-container'>
                <p>Time to cook: {recipe.time_to_cook}</p>
                <p>Servings: {recipe.servings}</p>
            </div>
        </div>
    )
}

export default RecipeCard;
