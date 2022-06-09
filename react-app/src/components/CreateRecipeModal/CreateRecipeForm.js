import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Select from "react-select";

import ErrorMessage from '../ErrorMessage';
import { createRecipe } from '../../store/recipeBox';


const CreateRecipeForm = ({ setShowModal }) => {
    const [errorMessages, setErrorMessages] = useState({});
    const [title, setTitle] = useState("");
    const [amount, setAmount] = useState("");
    const [measure, setMeasure] = useState();
    const [foodItem, setFoodItem] = useState("");
    const [foodItemList, setFoodItemList] = useState([]);
    const [amountList, setAmountList] = useState([]);
    const [measureList, setMeasureList] = useState([]);
    const [instruction, setInstruction] = useState("");
    const [instructionsList, setInstructionsList] = useState([]);
    const [image, setImage] = useState(null);
    const [time, setTime] = useState("");
    const [servings, setServings] = useState("");
    const [description, setDescription] = useState("");
    const user = useSelector((state) => state.session.user)
    const dispatch = useDispatch();

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
    };

    const getMeasure = (idx) => {
        const measure = measurementOptions.filter(option => option.value === idx);
        return measure[0].label;
    };

    const ingredientsList = () => {
        return (
            <div>
                <ul>
                    {foodItemList.map((item, idx) => (
                        <li key={idx}>
                            {amountList[idx]} {getMeasure(measureList[idx])} {item}
                        </li>
                    ))}
                </ul>
            </div>
        )
    };

    const addIstruction = (e) => {
        e.preventDefault();
        e.stopPropagation();
        const instructionToAdd = [...instructionsList, instruction];
        setInstructionsList(instructionToAdd);
        setInstruction("");
    }

    const instructionList = () => (
        <div>
            <ol>
                {instructionsList.map((instruction, idx) => (
                    <li key={idx}>
                        {instruction}
                    </li>
                ))}
            </ol>
        </div>
    );

    const ingrForPayload = (amountList, foodItemList, measureList) => {
        const res = {};

        foodItemList.forEach((item, idx) => {

                res[`ingredient-${idx}-amount`] = amountList[idx];
                res[`ingredient-${idx}-food_item`] = item;
                res[`ingredient-${idx}-measurement_unit_id`] = parseInt(measureList[idx])

        });

        return res;
    };

    const instrForPayload = (instructionsList) => {
        const obj = {};
        instructionsList.forEach((instr, idx) => {

                obj[`instructions-${idx}-specification`] = instr;
                obj[`instructions-${idx}-list_order`] = idx + 1;


        });

        return obj;
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const payload = {
            title,
            time_to_cook: time,
            description,
            servings,
            img_url: "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fpublic-assets.meredithcorp.io%2Fc69261efa4d825689cd3307f7082c1c0%2F164661054163DF72EA-F8B7-4158-AE95-655BA498DCB0.jpeg&w=595&h=791&c=sc&poi=face&q=60",
            ...ingrForPayload(amountList, foodItemList, measureList),
            ...instrForPayload(instructionsList)
        };

        const res = await dispatch(createRecipe(payload, user.id));
        if (!Array.isArray(res)) {
            setShowModal(false);
        } else {
            const errors = {};
            if (Array.isArray(res)) {
                res.forEach(error => {
                    const label = error.split(":")[0].slice(0, -1)
                    const message = error.split(":")[1].slice(1)
                    errors[label] = message;
                })
            } else {
                errors.overall = res;
            }
            setErrorMessages(errors);
        }
    }

    return (
        <div className='new-recipe-form-container'>
            <h1>Add a recipe</h1>
            <form onSubmit={handleSubmit}>
                <ErrorMessage label={""} message={errorMessages.overall} />
                <div className='input-container'>
                    <input
                        id="title"
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        required
                        placeholder="Recipe title"
                    />
                    <ErrorMessage label={""} message={errorMessages.title} />
                </div>
                <div>
                    <input
                        id="time_to_cook"
                        type="text"
                        value={time}
                        onChange={(e) => setTime(e.target.value)}
                        required
                        placeholder="Total time to cook"
                    />
                    <ErrorMessage label={""} message={errorMessages.time_to_cook} />
                </div>
                <div>
                    <input
                        id="servings"
                        type="number"
                        value={servings}
                        onChange={(e) => setServings(e.target.value)}
                        min="1"
                        step="1"
                        required
                        placeholder="Servings"
                    />
                    <ErrorMessage label={""} message={errorMessages.time_to_cook} />
                </div>
                <div>
                    <label htmlFor='image'>Add the photo of the dish</label>
                    <input
                        id="image"
                        type="file"
                        onChange={(e) => setImage(e.target.files[0])}
                    />
                </div>
                <div>
                    <textarea
                        id="description"
                        value={description}
                        placeholder="Description"
                        onChange={(e) => setDescription(e.target.value)}
                    />
                </div>
                <div className='ingredients-form'>
                    <div>
                        <h3>Ingredients</h3>
                    </div>
                    <div className='addedIngredients'>
                        {foodItemList.length ? ingredientsList() :
                            <div>No ingredients. Add some in the fields below</div>
                        }
                    </div>
                    <div className='input-container'>
                        <input
                            id="amount"
                            type="number"
                            value={amount}
                            min="0.1"
                            step="0.1"
                            onChange={(e) => setAmount(e.target.value)}
                            placeholder="amount"
                        />
                        <ErrorMessage label={""} message={errorMessages.amount} />
                    </div>
                    <div>
                        <Select
                            options={measurementOptions}
                            value={measure ? measure.value : ""}
                            onChange={(option) => {
                                return setMeasure(option.value)
                            }}
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
                <div className='instructions-form'>
                    <h3>Instructions</h3>
                    <div className='added-instructions'>
                        {instructionsList.length ? instructionList() :
                            <div>"Add your instructions below..."</div>
                        }
                    </div>
                    <div>
                        <textarea
                            id="instruction"
                            value={instruction}
                            placeholder="Instruction text"
                            onChange={(e) => setInstruction(e.target.value)}
                        />
                    </div>
                    <div><button
                        disabled={!instruction}
                        onClick={(e) => addIstruction(e)}
                    >
                        Add
                    </button></div>
                    <ErrorMessage label={""} message={errorMessages.instructions} />
                </div>
                <div className='buttons'>
                    <button type="submit">Add new recipe</button>
                    <button
                        onClick={(e) => {
                            e.preventDefault();
                            return setShowModal(false)
                        }}
                    >
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    )
}

export default CreateRecipeForm;
