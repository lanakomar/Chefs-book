import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Select from "react-select";

import ErrorMessage from "../ErrorMessage";


const CreateRecipeForm = ({ setShowModal }) => {
    const [errorMessages, setErrorMessages] = useState({});
    const [title, setTitle] = useState("");
    const [amount, setAmount] = useState("");
    const [measure, setMeasure] = useState();
    const [foodItem, setFoodItem] = useState("");
    const [foodItemList, setFoodItemList] = useState([]);
    const [amountList, setAmountList] = useState([]);
    const [measureList, setMeasureList] = useState([]);

    const measurementOptions = [
        { label: "", value: "14" },
        { label: "cups", value: "1" },
        { label: "fluid ounces", value: "2" },
        { label: "gallons", value: "3" },
        { label: "grams", value: "4" },
        { label: "liters", value: "5" },
        { label: "milliliters", value: "6" },
        { label: "ounces", value: "7" },
        { label: "pinch", value: "8" },
        { label: "pints", value: "9" },
        { label: "pounds", value: "10" },
        { label: "quarts", value: "11" },
        { label: "tablespoons", value: "12" },
        { label: "teaspoons", value: "13" },
        { label: "cans", value: "15" },
        { label: "slices", value: "16" },
        { label: "splash", value: "17" },
    ];

    const addIngredient = (e) => {
        e.preventDefault();
        e.stopPropagation();

        const itemsToAdd = [...foodItemList, foodItem];
        const amountsToAdd = [...amountList, amount];
        const measuresToAdd = [...measureList, measure];

        setFoodItemList(itemsToAdd);
        setAmountList(amountsToAdd);
        setMeasureList(measuresToAdd);
        setMeasure("");
        setFoodItem("");
        setAmount("");
    }

    console.log(foodItemList);
    console.log(amountList);
    console.log(measureList);
    console.log("measure", measure?.value)

    const ingredientsList = () => {
        return (
            <div>
                <ul>
                    {foodItemList.map((item, idx) => (
                        <li key={idx}>
                            {amountList[idx]} {measureList[idx]} {item}
                        </li>
                    ))}
                </ul>
            </div>
        )
    }

    return (
        <div className='new-recipe-form-container'>
            <h1>Add a recipe</h1>
            <form>
                <ErrorMessage label={""} message={errorMessages.overall} />
                <div className='input-container'>
                    <label htmlFor="title">Title</label>
                    <input
                        id="title"
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        required
                    />
                    <ErrorMessage label={""} message={errorMessages.title} />
                </div>
                <div>
                    <h3>Ingredients</h3>
                    {foodItemList ? ingredientsList() :
                        <div>No ingredients. Add some in the fields below</div>
                    }
                </div>
                <ErrorMessage label={""} message={errorMessages.overall} />
                <div className='ingredients-form'>
                    <div className='addedIngredients'></div>
                    <div className='input-container'>
                        <input
                            id="amount"
                            type="number"
                            value={amount}
                            min="0.1"
                            step="0.1"
                            onChange={(e) => setAmount(e.target.value)}
                            placeholder="amount"
                            required
                        />
                        <ErrorMessage label={""} message={errorMessages.amount} />
                    </div>
                    <div>
                        <Select
                            options={measurementOptions}
                            value={measure ? measure.value : ""}
                            required
                            onChange={(option) => {
                              return  setMeasure(option.value)}}
                            placeholder="Choose..."
                        />
                        <ErrorMessage label={""} message={errorMessages.measurement_unit_id} />
                    </div>
                    <div className='input-container'>
                        <input
                            id="food-item"
                            type="text"
                            value={foodItem}
                            onChange={(e) => setFoodItem(e.target.value)}
                            placeholder="Food Item"
                            required
                        />
                        <ErrorMessage label={""} message={errorMessages.food_item} />
                    </div>
                    <div><button
                        disabled={!foodItem || !amount || !measure}
                        onClick={(e) => addIngredient(e)}
                    >
                        Add
                    </button></div>
                </div>
            </form>
        </div>
    )
}

export default CreateRecipeForm;
