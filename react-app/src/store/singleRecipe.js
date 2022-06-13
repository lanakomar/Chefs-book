const SET_ONE_RECIPE = 'recipe/SET_ONE_RECIPE';

export const setOnerRecipe = (recipe) => ({
    type: SET_ONE_RECIPE,
    recipe
});

export const viewRecipe = (recipeId) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}`);
    if (res.ok) {
        const data = await res.json();
        dispatch(setOnerRecipe(data));
        return null;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    }
}

const initialState = {};

const singleRecipeReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_ONE_RECIPE:
            return {
                ...state,
                ...action.recipe
            }
        default:
            return state;
    }
}

export default singleRecipeReducer;
