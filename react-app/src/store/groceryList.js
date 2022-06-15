const SET_GROCERY_LIST = 'groceryList/SET_GROCERY_LIST';
const ADD_GROCERY_LIST = 'groceryList/ADD_GROCERY_LIST';
const DELETE_ITEMS_FROM_GL = 'groceryList/DELETE_ITEMS_FROM_GL';
const DELETE_ITEM_FROM_GL = 'groceryList/DELETE_ITEM_FROM_GL';

export const setGroceryList = (listItems) => ({
    type: SET_GROCERY_LIST,
    listItems
});

const addThingsToBuy = (listItems) => ({
    type: ADD_GROCERY_LIST,
    listItems
});

const deleteRecipeIngr = (recipeId) => ({
    type: DELETE_ITEMS_FROM_GL,
    recipeId
});

const deleteItem = (recipeId, ingrId) => ({
    type: DELETE_ITEM_FROM_GL,
    recipeId,
    ingrId
})

export const addToGroceryList = (payload, userId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/groceries`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if (res.ok) {
        const data = await res.json();
        dispatch(addThingsToBuy(data));
        return null;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    };
};

export const deleteItemsFromGL = (payload, userId, recipeId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/groceries`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if (res.ok) {
        const data = await res.json();
        dispatch(deleteRecipeIngr(recipeId));
        return data;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    };
};

export const deleteItemFromGL = (payload, userId, recipeId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/groceries`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if (res.ok) {
        await res.json();
        dispatch(deleteItem(recipeId, payload[0]));
        return null;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return "An error occurred. Please try again.";
    };
}

const to_obj = (array) => {
    const newObj = {};

    array.forEach(item => {
        newObj[item.recipe_id] = { ...newObj[item.recipe_id], [item.id]: item }
    });

    return newObj;
};


const initialState = {};

const groceryListReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_GROCERY_LIST:
            const groceryList = to_obj(action.listItems)
            return {
                ...state,
                ...groceryList
            };
        case ADD_GROCERY_LIST:
            const added = to_obj(action.listItems)
            return {
                ...state,
                ...added
            }
        case DELETE_ITEMS_FROM_GL:
            const newState = { ...state };
            delete newState[action.recipeId]
            return newState;
        case DELETE_ITEM_FROM_GL:
            if (Object.keys(state[action.recipeId]).length > 1) {
                const newState2 = { ...state, [action.recipeId] : {...state[[action.recipeId]]} }
                delete newState2[action.recipeId][action.ingrId];
                return newState2;
            } else {
                const newState = { ...state };
                delete newState[action.recipeId]
                return newState;
            }
        default:
            return state;
    }
}

export default groceryListReducer;
