import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import './index.css';


const GroceryList = ({ setShowModal }) => {
    const groceryList = useSelector(state => state.groceryList);
    const recipes = useSelector(state => state.recipes);
    const recipeIds = Object.keys(groceryList)
    const recipe = recipes[recipeIds[0]]
    console.log(groceryList[1]);

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

    return (
        <div className='list-container'>
            <p>Your Grocery List</p>
            <div className='gl-recipes-container'>
            <ol>
                {recipeIds.map(recipeId => (
                    <li key={recipeId}>
                        <div className='recipe-part'>
                            <div className='title'>
                                <i className="fa-solid fa-chevron-right"></i>
                                <div>{recipes[recipeId].title}</div>
                            </div>
                            <button className="remove-all-ingr">Remove</button>
                        </div>
                        <ul>
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
                    </li>
                ))}
            </ol>
            </div>
            <div className='gl-buttons'>
                <button className='done'>Done</button>
            </div>
        </div>
    )
};

export default GroceryList;
