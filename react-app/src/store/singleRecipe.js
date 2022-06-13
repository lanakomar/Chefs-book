const SET_ONE_RECIPE = 'recipe/SET_ONE_RECIPE';
const ADD_NEW_NOTE = 'recipe/ADD_NEW_NOTE';
const DELETE_NOTE = 'recipe/DELETE_NOTE';

export const setOnerRecipe = (recipe) => ({
    type: SET_ONE_RECIPE,
    recipe
});

const addNewNote = (note) => ({
    type: ADD_NEW_NOTE,
    note
});

const removeNote = (noteId) => ({
    type: DELETE_NOTE,
    noteId
})

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
};

export const editNote = (payload, noteId) => async (dispatch) => {
    const res = await fetch(`/api/notes/${noteId}`, {
        method: "PUT",
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
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    }
}

export const deleteNote = (noteId) => async (dispatch) => {
    const res = await fetch(`/api/notes/${noteId}`, {
        method: "DELETE",
    });
    if (res.ok) {
        dispatch(removeNote(noteId));
        return null;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data;
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
        case DELETE_NOTE:
            const newState2 = {...state}
            newState2.ingredients = { ...state.ingredients }
            newState2.instructions = { ...state.instructions }
            newState2.notes = { ...state.notes}
            delete newState2.notes[action.noteId]
            return newState2
        default:
            return state;
    }
}

export default singleRecipeReducer;
