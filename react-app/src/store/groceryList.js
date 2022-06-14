const SET_GROCERY_LIST = 'groceryList/SET_GROCERY_LIST';
const ADD_GROCERY_LIST = 'groceryList/ADD_GROCERY_LIST';

export const setGroceryList = (listItems) => ({
    type: SET_GROCERY_LIST,
    listItems
});

const addThingsToBuy = (listItems) => ({
    type: ADD_GROCERY_LIST,
    listItems
});

export const addToGroceryList = (payload, userId) => async (dispatch) => {
    console.log(payload);
    const res = await fetch(`/api/users/${userId}/groceries`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if (res.ok) {
        const newGL = await res.json();
        console.log("####", newGL);
    } else if (res.status < 500) {
        const data = await res.json();
        console.log("******", data)
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
}


const initialState = {};

const groceryListReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_GROCERY_LIST:
            const groceryList = to_obj(action.listItems)
            return {
                ...state,
                ...groceryList
            };
        default:
            return state;
    }
}

export default groceryListReducer;
