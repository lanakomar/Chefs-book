import { useSelector } from 'react-redux';

import CreateRecipeModal from "../CreateRecipeModal";
import RecipeCard from '../RecipeCard';
import './index.css'

const RecipeBox = () => {

    const usersRecipes = useSelector((state) => state.recipeBox);
    const recipes = Object.values(usersRecipes);

    if (!usersRecipes) {
        return null
    };

    return (
        <div className='recipeBox-container'>
            <CreateRecipeModal />
            <div className="custom-recipes">
                    {recipes?.map(recipe => (
                        <RecipeCard recipe={recipe} key={recipe.id} />
                    ))}
            </div>
            <div className="saved-recipes"></div>
        </div>
    )
}

export default RecipeBox;
