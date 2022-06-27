const SET_SAVED_RECIPES = 'savedRecipes/SET_SAVED_RECIPES';
const ADD_SAVED_RECIPE = 'savedRecipes/ADD_SAVED_RECIPE';
const REMOVE_SAVED_RECIPE = 'savedRecipes/REMOVE_SAVED_RECIPE';

export const setSavedRecipes = (recipes) => ({
    type: SET_SAVED_RECIPES,
    recipes
});

const addSavedRecipe = (recipe) => ({
    type: ADD_SAVED_RECIPE,
    recipe
});

const removeFromSaved = (recipeId) => ({
    type: REMOVE_SAVED_RECIPE,
    recipeId
});

export const saveToRecipeBox = (recipeId, userId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/saved-recipes`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(recipeId),
    });
    if (res.ok) {
        const recipe = await res.json();
        dispatch(addSavedRecipe(recipe));
        return null
    } else if (res.status < 500) {
        const data = await res.json();
        console.log(data)
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    };
};

export const deleteFromSaved = (recipeId, userId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/saved-recipes`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(recipeId),
    });

    if (res.ok) {
        dispatch(removeFromSaved(recipeId));
        return null;
    } else if (res.status < 500) {
        const data = await res.json();
        console.log(data)
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    };
}

const initialState = {}

const savedRecipesReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_SAVED_RECIPES:
            return {
                ...state,
                ...action.recipes
            };
        case ADD_SAVED_RECIPE:
            return {
                ...state,
                [action.recipe.id]: action.recipe
            };

        case REMOVE_SAVED_RECIPE:
            const newState = { ...state };
            delete newState[action.recipeId];
            return newState;
        default:
            return state;
    }
};

export default savedRecipesReducer;
