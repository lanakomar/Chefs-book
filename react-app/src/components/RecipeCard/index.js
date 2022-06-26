import { Link } from 'react-router-dom';

import EditRecipeModal from "../EditRecipeModal";
import DeleteRecipeModal from "../DeleteRecipeModal";
import './index.css'

const RecipeCard = ({ recipe, saved }) => {
    return (
        <div className="card-container">
            <div className='img-container'>
                <Link to={`/recipes/${recipe.id}`}>
                    <img src={recipe.img_url} alt={recipe.title} />
                </Link>
                <DeleteRecipeModal id={recipe.id} saved={saved} />
            </div>
            <h4>{recipe.title}</h4>
            <div className='edit-recipe'>
                <EditRecipeModal id={recipe.id} author={recipe.user_id} />
            </div>
            <div className='time-serv-container'>
                <p>Time: {recipe.time_to_cook}</p>
                <p>Servings: {recipe.servings}</p>
            </div>
        </div>
    )
}

export default RecipeCard;
