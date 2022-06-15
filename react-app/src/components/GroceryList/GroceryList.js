import React from 'react';
import { useSelector } from 'react-redux';

import AccordionItem from '../AccordionItem';
import './index.css';


const GroceryList = ({ setShowModal }) => {
    const groceryList = useSelector(state => state.groceryList);
    const recipes = useSelector(state => state.recipes);
    const recipeIds = Object.keys(groceryList)

    return (
        <div className='list-container'>
            <p>Your Grocery List</p>
            <div className='gl-recipes-container'>
                <ol>
                    {recipeIds.map(recipeId => (
                        <li key={recipeId}>
                            <AccordionItem
                                recipeId={recipeId}
                                recipes={recipes}
                                groceryList={groceryList} />
                        </li>
                    ))}
                </ol>
            </div>
            <div className='gl-buttons'>
                <button className='done'
                    onClick={(e) => { e.preventDefault(); setShowModal(false) }}
                >
                    Done
                </button>
            </div>
        </div>
    )
};

export default GroceryList;
