import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { deleteRecipe } from "../../store/recipeBox";
import ErrorMessage from '../ErrorMessage';
import "./DeleteRecipeForm.css";


const DeleteRecipeForm = ({ setShowModal, id }) => {

    const [errorMessages, setErrorMessages] = useState({});
    const recipes = useSelector(state => state.recipeBox);
    const recipe = recipes[id];
    const dispatch = useDispatch();

    const handleDelete = async (e) => {
        e.preventDefault();
        e.stopPropagation();

        const data = await dispatch(deleteRecipe(id));
        if (data) {
            const errors = {};
            if (Array.isArray(data.errors)) {
                data.errors.forEach((error) => {
                    const label = error.split(":")[0].slice(0, -1);
                    const message = error.split(":")[1].slice(1);
                    errors[label] = message;
                });
            } else {
                errors.overall = data;
            }
            setErrorMessages(errors);
        }
    }

    return (
        <div className="delete-form-container">
            <h3> {recipe?.title} </h3>
            <ErrorMessage label={""} message={errorMessages.overall} />
            <p>Are you sure you want to delete this recipe?</p>
            <div className="message-btns">
                <button
                    className="delete-recipe-cancel"
                    onClick={(e) => {
                        e.preventDefault();
                        setShowModal(false);
                    }}
                >
                    Cancel
                </button>
                <button
                    className="delete-recipe-confirm"
                    onClick={(e) => handleDelete(e)}
                >
                    Delete
                </button>
            </div>
        </div>
    );
}

export default DeleteRecipeForm;
