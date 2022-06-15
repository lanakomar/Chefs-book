import React from 'react';
import { useSelector } from 'react-redux';

import AccordionItem from '../AccordionItem';
import EmptyGroceryList from '../EmptyGroceryList';
// import blank from '../../images/blank-state-image.png';
import './index.css';


const GroceryList = ({ setShowModal }) => {
    const groceryList = useSelector(state => state.groceryList);
    const recipes = useSelector(state => state.recipes);
    const recipeIds = Object.keys(groceryList);

    // const emptyGL = (
    //     <div className='emptyGL'>
    //         <div className='empty-list'>
    //             <img src={blank} alt="empty-grocery-list" />
    //         </div>
    //         <h3>Build Your Grocery List</h3>
    //         <p>Add recipes you plan to cook.</p>
    //         <p> Adjust what you need to buy.</p>
    //     </div>
    // )

    return (
        <div className='list-container'>
            <p>Your Grocery List</p>
            <div className='gl-recipes-container'>
                {!recipeIds.length ? <EmptyGroceryList /> :
                    <ol>
                        {recipeIds.map(recipeId => (
                            // <li key={recipeId}>
                                <AccordionItem
                                    recipeId={recipeId}
                                    recipes={recipes}
                                    groceryList={groceryList}
                                    key={recipeId} />
                            // </li>
                        ))}
                    </ol>
                }
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
