import React, { useState, useRef } from 'react';
// import { useDispatch, useSelector } from 'react-redux';


const AccordionItem = ({ recipeId, recipes, groceryList}) => {

    const [clicked, setClicked] = useState(false);
    const contentEl = useRef();

    const handleToggle = () => {
        setClicked((prev) => !prev);
    };

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
        <>
            <div className='recipe-part'>
                <div className='title' onClick={handleToggle}>
                    <i className={clicked ? "fa-solid fa-chevron-right rotate": "fa-solid fa-chevron-right" } />
                    <div>{recipes[recipeId].title}</div>
                </div>
                <button className="remove-all-ingr">Remove</button>
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
