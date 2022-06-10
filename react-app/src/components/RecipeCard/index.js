import './index.css'

const RecipeCard = ({ recipe }) => {
    return (
        <div className="card-container">
            <div className='img-container'>
                <img src={recipe.img_url} alt={recipe.title} />
            </div>
            <h4>{recipe.title}</h4>
            <div className='time-serv-container'>
                <p>Time to cook: {recipe.time_to_cook}</p>
                <p>Servings: {recipe.servings}</p>
            </div>
        </div>
    )
}

export default RecipeCard;
