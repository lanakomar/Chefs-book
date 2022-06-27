import { useSelector } from 'react-redux';

import CreateRecipeModal from "../CreateRecipeModal";
import RecipeCard from '../RecipeCard';
import './index.css'

const RecipeBox = () => {

    const usersRecipes = useSelector((state) => state.recipeBox);
    const recipes = Object.values(usersRecipes).sort(function (a, b) {
        return b.id - a.id;
    });

    const savedRecipes = useSelector((state) => state.savedRecipes);

    if (!usersRecipes) {
        return null
    };

    return (
        <div className='recipeBox-container'>
            <CreateRecipeModal />
            <div className="custom-recipes">
                <h3>Your Recipies</h3>
                <div className='custom-recipes-container'>
                    {recipes?.map(recipe => (
                        <RecipeCard recipe={recipe} saved={false} key={recipe.id} />
                    ))}
                </div>
            </div>
            <div className="saved-recipes">
                <h3>Saved Recipes</h3>
                <div className='saved-recipes-container'>
                    {Object.values(savedRecipes)?.map(recipe => (
                        <RecipeCard recipe={recipe} saved={true} key={recipe.id} />
                    ))}
                </div>
            </div>
        </div>
    )
}

export default RecipeBox;
