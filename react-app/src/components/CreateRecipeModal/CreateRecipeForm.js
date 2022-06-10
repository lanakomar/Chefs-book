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

    const handleItemDelete = (e) => {
        const idx = e.target.id;
        const updatedMeasureList = measureList.slice();
        const updatedAmountList = amountList.slice();
        const updatedfoodItemList = foodItemList.slice();
        updatedAmountList.splice(idx, 1);
        updatedMeasureList.splice(idx, 1);
        updatedfoodItemList.splice(idx, 1);
        setAmountList(updatedAmountList);
        setMeasureList(updatedMeasureList);
        setFoodItemList(updatedfoodItemList);
    };

    const ingredientsList = () => {
        return (
            <div>
                <ul>
                    {foodItemList.map((item, idx) => (
                        <li key={idx} id={idx}>
                            {amountList[idx]} {getMeasure(measureList[idx])} {item}
                            <i className="fa-solid fa-xmark"
                                id={idx}
                                onClick={handleItemDelete}
                            ></i>
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
    };

    const handleInstrDelete = (e) => {
        console.log(e.target.id)
        const idx = e.target.id
        const updatedInstructionsList = instructionsList.slice();
        updatedInstructionsList.splice(idx, 1)
        setInstructionsList(updatedInstructionsList)
    };

    const instructionList = () => (
        <div>
            <ol>
                {instructionsList.map((instruction, idx) => (
                    <li key={idx}>
                        {instruction}
                        <i className="fa-solid fa-xmark"
                            id={idx}
                            onClick={handleInstrDelete}
                        ></i>
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
    };

    const toBase64 = file => new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });

    const handleSubmit = async (e) => {
        e.preventDefault();

        const payload = {
            title,
            time_to_cook: time,
            description,
            servings,
            image: image ? await toBase64(image) : null,
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
                    const label = error.split(":")[0].slice(0, -1);
                    let message;
                    if (label === "instructions") {

                    }
                    message = error.split(":")[1].slice(1)
                    // let [first, ...rest] = error.split(':');
                    let rest = [...error.split(':').slice(1)];
                    let tmp2 = rest.join(':').replaceAll("'", '"');
                    if (tmp2.indexOf(":") > 0) {
                        let remainder = rest.join(':').replaceAll("'", '"');
                        let tmp = JSON.parse(remainder)
                        errors[label] = tmp;
                    } else {
                        errors[label] = message;
                    }
                })
            } else {
                errors.overall = res;
            }
            setErrorMessages(errors);
        }
    };

    const PreviewImage = () => {
        var oFReader = new FileReader();
        oFReader.readAsDataURL(document.getElementById("image").files[0]);

        oFReader.onload = function (oFREvent) {
            document.getElementById("uploadPreview").src = oFREvent.target.result;
        };
    }

    return (
        <div className='new-recipe-form-container'>
            <h1>Add a recipe</h1>
            <form onSubmit={handleSubmit} className="new-recipe">
                <ErrorMessage label={""} message={errorMessages.overall} />
                <div className='input-container'>
                    <input
                        id="title"
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder="Recipe title"
                    />
                    <ErrorMessage label={""} message={errorMessages.title} />
                </div>
                <div className='time-serv-container'>
                    <div>
                        <input
                            id="time_to_cook"
                            type="text"
                            value={time}
                            onChange={(e) => setTime(e.target.value)}
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
                            placeholder="Servings"
                        />
                        <ErrorMessage label={""} message={errorMessages.servings} />
                    </div>
                </div>
                <div className="image-container">
                    <label htmlFor='image'>Add the photo of the dish</label>
                    <div>
                        <input
                            id="image"
                            type="file"
                            accept="image/jpg, image/png, image/jpeg, image/gif"
                            onChange={(e) => {
                                PreviewImage();
                                return setImage(e.target.files[0])}}
                        />
                        {image ?
                        <img id="uploadPreview" alt="upload-preview"/>
                        : null
                        }
                    </div>
                    <ErrorMessage label={""} message={errorMessages.img_url} />
                </div>
                <div>
                    <textarea
                        id="description"
                        value={description}
                        placeholder="Description"
                        onChange={(e) => setDescription(e.target.value)}
                    />
                    <ErrorMessage label={""} message={errorMessages.description} />
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
                    <div className='ingredient-inputs'>
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
                            <ErrorMessage label={""} message={errorMessages.ingredient?.amount} />
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
                            <ErrorMessage label={""} message={errorMessages.ingredient?.measurement_unit_id} />
                        </div>
                        <div className='input-container'>
                            <input
                                id="food-item"
                                type="text"
                                value={foodItem}
                                onChange={(e) => setFoodItem(e.target.value)}
                                placeholder="Food Item"
                            />
                            <ErrorMessage label={""} message={errorMessages.ingredient?.food_item} />
                        </div>
                        <div className='add-btn'><button
                            disabled={!foodItem || !amount || !measure}
                            onClick={(e) => addIngredient(e)}
                            style={{ cursor: (!foodItem || !amount || !measure) ? 'not-allowed' : "pointer" }}
                        >
                            Add
                        </button></div>
                    </div>
                </div>
                <div className='instructions-form'>
                    <div><h3>Instructions</h3></div>
                    <div className='added-instructions'>
                        {instructionsList.length ? instructionList() :
                            <div>Add your instructions below...</div>
                        }
                    </div>
                    <div className='instr-inputs'>
                        <div>
                            <textarea
                                id="instruction"
                                value={instruction}
                                placeholder="Instruction text"
                                onChange={(e) => setInstruction(e.target.value)}
                            />
                        </div>
                        <div className='add-btn'><button
                            disabled={!instruction}
                            onClick={(e) => addIstruction(e)}
                            style={{ cursor: (!foodItem || !amount || !measure) ? 'not-allowed' : "pointer" }}
                        >
                            Add
                        </button></div>
                    </div>
                    <ErrorMessage label={""} message={errorMessages?.instructions?.specification} />
                </div>
                <div className='buttons'>
                    <button
                        type="submit"
                    >Add new recipe</button>
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
