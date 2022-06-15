import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Select from "react-select";

import ErrorMessage from '../ErrorMessage';
import { createRecipe, editRecipe } from '../../store/recipeBox';


const CreateRecipeForm = ({ setShowModal, edit, id }) => {

    const [errorMessages, setErrorMessages] = useState({});
    const [title, setTitle] = useState("");
    const [amount, setAmount] = useState("");
    const [measure, setMeasure] = useState();
    const [foodItem, setFoodItem] = useState("");
    const [ingredients, setIngredients] = useState([]);
    const [instruction, setInstruction] = useState("");
    const [instructionsList, setInstructionsList] = useState([]);
    const [image, setImage] = useState(null);
    const [time, setTime] = useState("");
    const [servings, setServings] = useState("");
    const [description, setDescription] = useState("");
    const [isLoaded, setIsLoaded] = useState(false);
    const [deletedInstructions, setDeletedInstructions] = useState([]);
    const [deletedIngredients, setDeletedIngredients] = useState([]);
    const user = useSelector((state) => state.session.user);
    const recipes = useSelector((state) => state.recipeBox);
    const dispatch = useDispatch();

    let recipe;
    if (edit) {
        recipe = recipes[id];
    };

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

    const setValues = () => {
        const ingrArr = Object.values(recipe.ingredients);
        const instrArr = Object.values(recipe.instructions);

        setTitle(recipe.title);
        setTime(recipe.time_to_cook);
        setServings(recipe.servings);
        setDescription(recipe.description);
        setIsLoaded(true);
        setIngredients(ingrArr);
        setInstructionsList(instrArr);
    };

    if (edit && !isLoaded) {
        setValues()
    };

    const addIngredient = (e) => {
        e.preventDefault();
        e.stopPropagation();

        const newIngredient = {
            amount: amount,
            food_item: foodItem,
            measurement_unit_id: measure,
        };

        setIngredients([...ingredients, newIngredient]);
        setMeasure("");
        setFoodItem("");
        setAmount("");
    };


    const getMeasure = (idx) => {
        const measure = measurementOptions.filter(option => option.value === idx.toString());
        return measure[0].label;
    };

    const handleItemDelete = (e) => {
        const idx = e.target.id;
        const updatedIngredients = ingredients.slice();
        const deleted = updatedIngredients.splice(idx, 1);
        setIngredients(updatedIngredients);
        setDeletedIngredients([...deletedIngredients, ...deleted])
    };

    const ingredientsList = () => {
        return (
            <div>
                <ul>
                    {ingredients.map((item, idx) => (
                        <li key={idx} id={idx}>
                            <div>{item.amount}</div> <div>{getMeasure(item.measurement_unit_id)}</div> <div className='ingr-text'>{item.food_item}</div>
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
        const instructionToAdd = {
            specification: instruction,
            list_order: instructionsList.length
        };
        setInstructionsList([...instructionsList, instructionToAdd]);
        setInstruction("");
    };

    const handleInstrDelete = (e) => {
        const idx = e.target.id
        const updatedInstructionsList = instructionsList.slice();
        const deleted = updatedInstructionsList.splice(idx, 1)
        setInstructionsList(updatedInstructionsList);
        setDeletedInstructions([...deletedInstructions, ...deleted]);
    };

    const instructionList = () => (
        <div>
            <ol>
                {instructionsList.map((instruction, idx) => (
                    <li key={idx}>
                        <div className='instr-text'>
                            {instruction.list_order + 1}. {instruction.specification}
                        </div>
                        <i className="fa-solid fa-xmark"
                            id={idx}
                            onClick={handleInstrDelete}
                        ></i>
                    </li>
                ))}
            </ol>
        </div>
    );

    const ingrForPayload = (ingredients, ingredientsDeleted = []) => {
        const res = {};
        ingredients.forEach((item, idx) => {
            res[`ingredient-${idx}-amount`] = item.amount;
            res[`ingredient-${idx}-food_item`] = item.food_item;
            res[`ingredient-${idx}-measurement_unit_id`] = parseInt(item.measurement_unit_id)
            res[`ingredient-${idx}-identifier`] = item.id;
        });
        ingredientsDeleted.forEach((item, idx) => {
            res[`ingredient_deleted-${idx}-identifier`] = item.id;
        });

        return res;
    };

    const instrForPayload = (instructions, instructionDeleted = []) => {
        const obj = {};
        instructions.forEach((instr, idx) => {
            obj[`instructions-${idx}-specification`] = instr.specification;
            obj[`instructions-${idx}-list_order`] = idx + 1;
            obj[`instructions-${idx}-identifier`] = instr.id;
        });

        instructionDeleted.forEach((instr, idx) => {
            obj[`instructions_deleted-${idx}-identifier`] = instr.id;
        });

        return obj;
    };

    const toBase64 = file => new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });

    const handleAdd = async (e) => {
        e.preventDefault();

        const payload = {
            title,
            time_to_cook: time,
            description,
            servings,
            image: image ? await toBase64(image) : null,
            ...ingrForPayload(ingredients),
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
    };

    const handleEdit = async (e) => {
        e.preventDefault();

        const payload = {
            title,
            time_to_cook: time,
            description,
            servings,
            image: image ? await toBase64(image) : recipe.img_url,
            ...ingrForPayload(ingredients, deletedIngredients),
            ...instrForPayload(instructionsList, deletedInstructions)
        };

        const res = await dispatch(editRecipe(payload, id));

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
    }

    if (!recipes) {
        return null
    };

    return (
        <div className='new-recipe-form-container'>
            {edit ? <h1>Edit recipe</h1> :
                <h1>Add a recipe</h1>
            }
            <form onSubmit={edit ? handleEdit : handleAdd} className="new-recipe">
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
                                return setImage(e.target.files[0])
                            }}
                        />
                        <div className='preview-image-container'>
                            {image ?
                                <img id="uploadPreview" alt="upload-preview" />
                                : null
                            }
                            {edit ? <img id="preview" alt="preview" src={recipe.img_url} />
                                : null}
                        </div>
                    </div>
                    <ErrorMessage label={""} message={errorMessages.image} />
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
                    <div
                        style={{ overflowY: (ingredients.length > 3) ? "scroll" : "none" }}
                        className='addedIngredients'>
                        {ingredients.length ? ingredientsList() :
                            <div>No ingredients. Add some in the fields below</div>
                        }
                    </div>
                    <div className='ingredient-inputs'>
                        <div className='input-container amount'>
                            <input
                                id="amount"
                                type="number"
                                value={amount}
                                min="0.1"
                                step="0.1"
                                onChange={(e) => setAmount(e.target.value)}
                                placeholder="amount"
                            />
                        </div>
                        <ErrorMessage label={""} message={errorMessages.ingredient?.amount} />
                        <div className='select'>
                            <Select
                                options={measurementOptions}
                                value={measure ? measure.value : ""}
                                onChange={(option) => {
                                    return setMeasure(option.value)
                                }}
                                placeholder="Choose..."
                            />
                        </div>
                        <ErrorMessage label={""} message={errorMessages.ingredient?.measurement_unit_id} />
                        <div className='input-container food'>
                            <input
                                id="food-item"
                                type="text"
                                value={foodItem}
                                onChange={(e) => setFoodItem(e.target.value)}
                                placeholder="Food Item"
                            />
                        </div>
                        <ErrorMessage label={""} message={errorMessages.ingredient?.food_item} />
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
                    <div
                        className='added-instructions'>
                        {instructionsList.length ? instructionList() :
                            <div>Add your instructions below</div>
                        }
                    </div>
                    <div className='instr-inputs'>
                        <div className='instr'>
                            <textarea
                                id="instruction"
                                value={instruction}
                                placeholder="Instruction text"
                                onChange={(e) => setInstruction(e.target.value)}
                            />
                        </div>
                        <ErrorMessage label={""} message={errorMessages?.instructions?.specification} />
                        <div className='add-btn'><button
                            disabled={!instruction}
                            onClick={(e) => addIstruction(e)}
                            style={{ cursor: (!instruction) ? 'not-allowed' : "pointer" }}
                        >
                            Add
                        </button></div>
                    </div>

                </div>
                <div className='warning'>All fields required<sup>*</sup></div>
                <div className='buttons'>
                    <button
                        type="submit"
                    >{edit ? "Edit recipe" : "Add new recipe"}</button>
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
