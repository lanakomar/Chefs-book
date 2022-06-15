import React, { useState, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { deleteItemsFromGL } from '../../store/groceryList';


const AccordionItem = ({ recipeId, recipes, groceryList}) => {

    const [clicked, setClicked] = useState(false);
    const contentEl = useRef();

    const handleToggle = () => {
        setClicked((prev) => !prev);
    };

    const dispatch = useDispatch();

    const user = useSelector((state => state.session.user))

    const measurements = {
        14: "",
        1: "cups",
        2: "fluid ounces",
        3: "gallons",
        4: "grams",
        5: "liters",
        6: "milliliters",
        7: "ounces",
        8: "pinch",
        9: "pints",
        10: "pounds",
        11: "quarts",
        12: "tablespoons",
        13: "teaspoons",
        15: "cans",
        16: "slices",
        17: "splash",
    };

    const handleRemoveRecipe = async (e) => {
        e.preventDefault();
        const recipeGL = groceryList[e.target.id]
        const ingrsIdToDelete = Object.keys(recipeGL);
        await dispatch(deleteItemsFromGL(ingrsIdToDelete, user.id, recipeId))
    }

    return (
        <>
            <div className='recipe-part'>
                <div className='title' onClick={handleToggle}>
                    <i className={clicked ? "fa-solid fa-chevron-right rotate": "fa-solid fa-chevron-right" } />
                    <div>{recipes[recipeId].title}</div>
                </div>
                <button
                    id={recipeId}
                    className="remove-all-ingr"
                    onClick={handleRemoveRecipe}
                >
                    Remove
                </button>
            </div>
            <ul ref={contentEl}
                style={
                    clicked
                        ? { height: contentEl.current.scrollHeight }
                        : { height: "0px" }
                }>
                {Object.values(groceryList[recipeId]).map(ingr => (
                    <li key={ingr.id} className='ingredient'>
                        <div>{ingr.amount} {measurements[ingr.measurement_unit_id]} {ingr.food_item}</div>
                        <div><i className="fa-solid fa-xmark"
                            id={ingr.id}
                        // onClick={handleItemDelete}
                        ></i></div>
                    </li>
                ))}
            </ul>
        </>
    )
}

export default AccordionItem;
