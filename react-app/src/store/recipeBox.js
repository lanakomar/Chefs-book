const SET_RECIPE_BOX = 'recipeBox/SET_RECIPE_BOX'

export const setRecipeBox = (recipes) => ({
    type: SET_RECIPE_BOX,
    recipes
})

const initialState = {};

const recipeBoxReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_RECIPE_BOX:
            return {
                ...state,
                ...action.recipes
            }
        default:
            return state;
    }
}

export default recipeBoxReducer;
