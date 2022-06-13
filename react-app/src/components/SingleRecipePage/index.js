import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';

import { viewRecipe } from '../../store/singleRecipe';
import './index.css'

const SingleRecipePage = () => {
    const { recipeId } = useParams();
    const dispatch = useDispatch();
    const recipe = useSelector(state => state.singleRecipe);

    useEffect(() => {
        async function fetchData() {
            await dispatch(viewRecipe(recipeId))
        };
        fetchData()
    }, [dispatch, recipeId])

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
        const noteDate = new Date(date);

        const day = noteDate.getDay();
        const month = noteDate.getMonth();
        const year = noteDate.getFullYear();

        return `${month}/${day}/${year}`
    }

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
                            className='note-text'
                            placeholder="Add your note here"
                        ></textarea>
                        <button>Add Note</button>
                    </form>
                </div>
                <div className="notes-container">
                    {notes.map(note => (
                        <div key={note.id}>
                            <div className='note-text'>
                                <div className='about-note'>
                                    <p className='author'>{note.author}</p>
                                    <p className='date'>{getNoteDate(note.date_created)}</p>
                                </div>
                                {note.content}
                            </div>
                            <div className='note-edit-delete'>
                                <div className='edit'></div>
                                <div className='delete'></div>
                            </div>
                        </div>
                    ))}
                </div>
                </div>
            </div>
        </div>
    )
};

export default SingleRecipePage;
