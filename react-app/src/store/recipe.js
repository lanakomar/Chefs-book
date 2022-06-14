const SET_ALL_RECIPES = 'recipe/SET_ALL_RECIPES';
const DELETE_SINGLE_RECIPE = 'recipe/DELETE_SINGLE_RECIPE';


export const setAllRecipes = (recipes) => ({
    type: SET_ALL_RECIPES,
    recipes
});

export const removeSingleRecipe = (recipeId) => ({
    type: DELETE_SINGLE_RECIPE,
    recipeId
});




const initialState = {};

const recipeReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_ALL_RECIPES:
            return {
                ...state,
                ...action.recipes
            }
        case DELETE_SINGLE_RECIPE:
            const newState = { ...state }
            delete newState[action.recipeId]
            return newState
        default:
            return state;
    }
}

export default recipeReducer;
