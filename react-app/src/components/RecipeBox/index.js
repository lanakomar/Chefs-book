import CreateRecipeModal from "../CreateRecipeModal";

const RecipeBox = () => {
    return (
        <div>
            <CreateRecipeModal />
            <div className="custom-recipes">
                <p>here is my own recipes</p>
            </div>
            <div className="saved-recipes"></div>
        </div>
    )
}

export default RecipeBox;
