const SET_RECIPE_BOX = 'recipeBox/SET_RECIPE_BOX';
const ADD_RECIPE = 'recipeBox/ADD_RECIPE';
const UPDATE_RECIPE = 'recipeBox/UPDATE_RECIPE';

export const setRecipeBox = (recipes) => ({
    type: SET_RECIPE_BOX,
    recipes
});

const addRecipe = (recipe) => ({
    type: ADD_RECIPE,
    recipe
});

const updateRecipe = (recipe) => ({
    type: UPDATE_RECIPE,
    recipe
})

export const createRecipe = (payload, userId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/recipes`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if(res.ok) {
        const recipe = await res.json();
        dispatch(addRecipe(recipe));
        return recipe
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    };
};

export const editRecipe = (payload, recipeId) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if (res.ok) {
        const recipe = await res.json();
        console.log("response", recipe)
        dispatch(updateRecipe(recipe));
        return recipe
    } else if (res.status < 500) {
        const data = await res.json();
        console.log("errors", data)
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    };
}

const initialState = {};

const recipeBoxReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_RECIPE_BOX:
            return {
                ...state,
                ...action.recipes
            }
        case ADD_RECIPE:
            return {
                ...state,
                [action.recipe.id]: action.recipe
            }
        case UPDATE_RECIPE:
            return {
                ...state,
                [action.recipe.id]: action.recipe
            }
        default:
            return state;
    }
}

export default recipeBoxReducer;
