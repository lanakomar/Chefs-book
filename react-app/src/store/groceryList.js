const SET_GROCERY_LIST = 'groceryList/SET_GROCERY_LIST';

export const setGroceryList = (listItems) => ({
    type: SET_GROCERY_LIST,
    listItems
});

const to_obj = (array) => {
    const newObj = {};
    array.forEach(item => {
        newObj[item.id] = item
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
