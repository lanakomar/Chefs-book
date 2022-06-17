import { useEffect, useState, useRef } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';

import ErrorMessage from '../ErrorMessage';
import DeleteNoteModal from '../DeleteNoteModal';
import { viewRecipe } from '../../store/singleRecipe';
import { addNote, editNote } from '../../store/singleRecipe';
import { addToGroceryList } from '../../store/groceryList';
import './index.css'

const SingleRecipePage = () => {
    const { recipeId } = useParams();
    const [content, setContent] = useState("");
    const [errorMessages, setErrorMessages] = useState({});
    const [isEdit, setIsEdit] = useState(false);
    const [editId, setEditId] = useState();
    const [added, setAdded] = useState(false);

    const inputRef = useRef();

    const dispatch = useDispatch();
    const recipe = useSelector(state => state.singleRecipe);
    const cur_user = useSelector(state => state.session.user);
    const groceries = useSelector(state => state.groceryList);

    useEffect(() => {
        async function fetchData() {
            await dispatch(viewRecipe(recipeId))
        };

        fetchData();
    }, [dispatch, recipeId])

    useEffect(() => {
        if (Object.keys(groceries).includes(recipeId)) {
            setAdded(true);
        } else {
            setAdded(false);
        }
    }, [groceries, recipeId])

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

    if (!Object.values(recipe).length) {
        return null
    };

    const ingredients = Object.values(recipe.ingredients);
    const instructions = Object.values(recipe.instructions);
    const notes = Object.values(recipe.notes).sort(function (a, b) {
        return b.id - a.id;
    });

    const getNoteDate = (date) => {

        const noteDate = date.split(":")[0].split(",")[1].slice(0, -3);

        return noteDate;
    };

    const addCommentClick = async (e) => {
        e.preventDefault();

        if (content.trim().length) {
            const payload = {
                content,
            };

            const res = await dispatch(addNote(payload, recipeId));

            if (!res) {
                setContent("");
                setErrorMessages({});
            } else {

                const errors = {};
                if (Array.isArray(res.errors)) {
                    res.errors.forEach((error) => {
                        const label = error.split(":")[0].slice(0, -1);
                        const message = error.split(":")[1].slice(1);
                        errors[label] = message;
                    });
                } else {
                    errors.overall = res;
                }
                setErrorMessages(errors);
            };
        } else {
            const errors = {};
            errors.content = "Note cannot be empty"
            setErrorMessages(errors)
        }
    }


    const handleEditPencilClick = (e, note) => {
        setContent(note);
        setIsEdit(true);
        setEditId(e.target.id);
        inputRef.current.scrollIntoView({ behavior: 'smooth', block: "center" })
    };

    const cancelEditClick = (e) => {
        e.preventDefault();
        setContent("");
        setIsEdit(false);
        setEditId();
    }

    const editNoteClick = async (e) => {
        e.preventDefault();

        const payload = {
            content: content
        };

        const data = await dispatch(editNote(payload, editId));
        if (data) {
            const errors = {};
            if (Array.isArray(data)) {
                data.forEach((error) => {
                    const label = error.split(":")[0].slice(0, -1);
                    const message = error.split(":")[1].slice(1);
                    errors[label] = message;
                });
            } else {
                errors.overall = data;
            }
            setErrorMessages(errors);
        } else {
            setContent("");
            setIsEdit(false);
            setEditId();
        }

    };

    const addToGL = async (e) => {
        e.preventDefault();
        const ingrIds = ingredients.map(ingr => ingr.id)
        await dispatch(addToGroceryList(ingrIds, cur_user.id));
        setAdded(true);
    };

    const addedToGL = (
        <div className='added-to-list'>
            <i className="fa-solid fa-check" />
            In the Grocery List
        </div>
    );

    const addButton = (
        <button
            onClick={addToGL}
            className='add-to-grocery-list'
        >
            Add to Your Grocery List
        </button>
    );


    return (
        <div className='single-recipe-container'>
            <div className='title-container'>
                <h3>{recipe?.title}</h3>
            </div>
            <div className='recipe-overview-container'>
                <div className='time-and-serving'>
                    <p>Servings: {recipe?.servings}</p>
                    <p>Total time to cook: {recipe?.time_to_cook}</p>
                </div>
                <div className='overview'>
                    <p>{recipe?.description}</p>
                    <div className='image-container' style={{ backgroundImage: `url(${recipe?.img_url})` }}></div>
                </div>
                <div className='cooking-instructions'>
                    <div className='ingredients-container'>
                        <h4>Ingredients</h4>
                        {ingredients.map(ingredient => (
                            <div key={ingredient.id} id={ingredient.id}>
                                {ingredient.amount} {measurements[ingredient.measurement_unit_id]} {ingredient.food_item}
                            </div>
                        ))}
                        {added ? addedToGL : addButton}
                    </div>
                    <div className='instructions-container'>
                        <h4>Preparation</h4>
                        {instructions.map(instruction => (
                            <div key={instruction.id}>
                                <h5>Step {instruction.list_order}</h5>
                                {instruction.specification}
                            </div>
                        ))}
                    </div>
                </div>
            </div>
            <div className='notes'>
                <div className='all-notes-container'>
                    <h4>Cooking Notes</h4>
                    <div className='input-note'>
                        <form className='note'>
                            <textarea
                                ref={inputRef}
                                value={content}
                                onChange={(e) => setContent(e.target.value)}
                                className='note-text'
                                placeholder="Add your note here"
                            ></textarea>
                            <ErrorMessage label={""} message={errorMessages.content} />
                            <div className='form-buttons'>
                                <button
                                    className='cancel-edit'
                                    hidden={!isEdit}
                                    onClick={cancelEditClick}
                                >
                                    Cancel
                                </button>
                                <button
                                    onClick={isEdit ? editNoteClick : addCommentClick}
                                    disabled={content.length ? false : true}
                                >
                                    {isEdit ? "Edit Note" : "Add Note"}
                                </button>
                            </div>
                        </form>
                    </div>
                    <div className="notes-container">
                        {notes.map(note => (
                            <div className='note-text' key={note.id}>
                                <div className='note-header'>
                                    <div className='about-note'>
                                        <p className='author'>{note.author}</p>
                                        <p className='date'>{getNoteDate(note.date_created)}</p>
                                    </div>
                                    <div
                                        className='note-edit-delete'
                                        style={{ display: (cur_user.id !== note.author_id) ? "none" : "flex" }}
                                    >
                                        <div className='edit'>
                                            <i id={note.id}
                                                className="fa-solid fa-pencil"
                                                onClick={(e) => handleEditPencilClick(e, note.content)}
                                            ></i></div>
                                        <DeleteNoteModal noteId={note.id} />
                                    </div>
                                </div>
                                {note.content}
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
};

export default SingleRecipePage;
