import EditRecipeModal from "../EditRecipeModal";
import DeleteRecipeModal from "../DeleteRecipeModal";
import './index.css'

const RecipeCard = ({ recipe }) => {
    return (
        <div className="card-container">
            <div className='img-container'>
                <img src={recipe.img_url} alt={recipe.title} />
                <DeleteRecipeModal id={recipe.id}/>
            </div>
            <h4>{recipe.title}</h4>
            <div className='edit-recipe'>
                <EditRecipeModal id={recipe.id} />
            </div>
            <div className='time-serv-container'>
                <p>Time to cook: {recipe.time_to_cook}</p>
                <p>Servings: {recipe.servings}</p>
            </div>
        </div>
    )
}

export default RecipeCard;
