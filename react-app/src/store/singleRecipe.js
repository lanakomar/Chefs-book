const SET_ONE_RECIPE = 'recipe/SET_ONE_RECIPE';
const ADD_NEW_NOTE = 'recipe/ADD_NEW_NOTE';

export const setOnerRecipe = (recipe) => ({
    type: SET_ONE_RECIPE,
    recipe
});

const addNewNote = (note) => ({
    type: ADD_NEW_NOTE,
    note
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
};

export const addNote = (payload, recipeId) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}/notes`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload)
    });
    if (res.ok) {
        const note = await res.json()
        dispatch(addNewNote(note))
        return null;
    }
    else if (res.status < 500) {
        const data = await res.json();
        console.log(data)
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
        case ADD_NEW_NOTE:
            const newState = {...state}
                newState.ingredients = { ...state.ingredients }
                newState.instructions = { ...state.instructions }
                newState.notes = { ...state.notes, [action.note.id]: action.note }
            return newState;
        default:
            return state;
    }
}

export default singleRecipeReducer;
