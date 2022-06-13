const SET_ALL_RECIPES = 'recipe/SET_ALL_RECIPES';

export const setAllRecipes = (recipes) => ({
    type: SET_ALL_RECIPES,
    recipes
});



const initialState = {};

const recipeReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_ALL_RECIPES:
            return {
                ...state,
                ...action.recipes
            }
        default:
            return state;
    }
}

export default recipeReducer;
