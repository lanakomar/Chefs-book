import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';

import { setAllRecipes } from '../../store/recipe';
import './index.css';

import { Modal } from '../../context/Modal';
import LoginForm from "../LoginFormModal/LoginForm";


const HomePage = () => {
    const [showModal, setShowModal] = useState(false);
    const history = useHistory();
    const user = useSelector((state) => state.session.user)
    const recipes = useSelector((state) => state.recipes);
    const recipesArr = Object.values(recipes).sort(function (a, b) {
        return b.id - a.id;
    });
    const dispatch = useDispatch();

    useEffect(() => {
        (async () => {
            const res = await fetch(`/api/recipes`);
            if (res.ok) {
                const data = await res.json();
                dispatch(setAllRecipes(data));
            }
        })();
    }, [dispatch]);

    function getRandomIdx(min, max) {
        return Math.floor(Math.random() * (max - min) + min);
    }

    const dayRecipe = recipesArr[getRandomIdx(0, recipesArr.length)];

    const loginModal = (showModal && (
        <Modal onClose={() => setShowModal(false)}>
            <LoginForm setShowModal={setShowModal} />
        </Modal>));

    const cardClick = (e) => {
        if (user) {
            const recipeId = e.currentTarget.id;
            history.push(`/recipes/${recipeId}`)
        } else {
            setShowModal(true);
        }
    }

    if (!recipes || !recipesArr.length) {
        return null
    }

    return (
        <div className='home-page-container'>
            <div
                style={{ backgroundImage: `url(${dayRecipe?.img_url})` }}
                className='day-recipe'>
                <div className='day-recipe-card'>
                    <div className='badge'><p>RECIPE OF THE DAY</p></div>
                    <h3>{dayRecipe?.title}</h3>
                    <p className='reicpe-description'>{dayRecipe?.description}</p>
                </div>
            </div>
            {loginModal}
            <div className='recipes-container'>
                {recipesArr?.map(recipe => (
                    <div key={recipe.id} id={recipe.id} className="card-container" onClick={cardClick}>
                        <div className='image-container' style={{ backgroundImage: `url(${recipe?.img_url})` }}></div>
                        <h4>{recipe.title}</h4>
                        <div className='time-serv-container'>
                            <p>Time: {recipe.time_to_cook}</p>
                            <p>Servings: {recipe.servings}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default HomePage;
