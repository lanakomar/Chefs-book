import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, Link } from 'react-router-dom';

import { setAllRecipes } from '../../store/recipe';
import { Modal } from '../../context/Modal';
import LoginForm from "../LoginFormModal/LoginForm";
import './index.css';
import docker from '../../images/technologies/docker.svg';
import flask from '../../images/technologies/flask.svg';
import github from '../../images/technologies/github.svg';
import javascript from '../../images/technologies/javascript.svg';
import nodejs from '../../images/technologies/nodejs.svg';
import python from '../../images/technologies/python.svg';
import react from '../../images/technologies/react.svg';
import redux from '../../images/technologies/redux.svg';
import sqlalchemy from '../../images/technologies/sqlalchemy.svg';
import css from '../../images/technologies/css.svg';
import postgresql from '../../images/technologies/postgresql.svg';


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
            {loginModal}
            <div
                style={{ backgroundImage: `url(${dayRecipe?.img_url})` }}
                className='day-recipe'>
                <div className='day-recipe-card'>
                    <div className='badge'><p>RECIPE OF THE DAY</p></div>
                    <Link to={`/recipes/${dayRecipe.id}`}><h3>{dayRecipe?.title}</h3></Link>
                    <p className='reicpe-description'>{dayRecipe?.description}</p>
                </div>
            </div>
            <div className='main-container'>
                <div className='about-app'>
                    <div className='about-title'><h2>The only cookbook Real Chef needs</h2></div>
                    <div className='about-content'><p>Chef's book helps home cooks of every level discover, save and organize the world’s best recipes</p>
                        <p>You could easily add your favourite recipe to the recipe box,
                            edit them (if needed) and delete them.
                            Add necessary ingredients to the shopping list for your next
                            culinary adventure.</p>
                        <div><span>Inspired by NYTCooking</span></div>
                    </div>
                </div>
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
            <div className='footer-wrapper'>
                <div className='footer'>
                    <div className='about-developer'>
                        <h4>About Developer:</h4>
                        <p className='name'>Lana Komar</p>
                        <p>Love to create beautiul things from scratch.</p>
                    </div>
                    <div className='personal-links'>
                        <h4>Personal Links:</h4>
                        <ul>
                            <li>
                                <a href="https://github.com/lanakomar">
                                    <i className="fa-brands fa-github-square fa-xl" />
                                    GitHub
                                </a>
                            </li>
                            <li>
                                <a href="https://www.linkedin.com/in/lana-komar">
                                    <i className="fa-brands fa-linkedin fa-xl" />
                                    LinkedIn
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div className='technologies'>
                        <h4>Technologies: </h4>
                        <ul>
                            <li><div><img src={postgresql} alt="postgresql" /></div>
                                <span>postgresql</span>
                            </li>
                            <li><div><img src={python} alt="python" /></div>
                                <span>python</span>
                            </li>
                            <li><div><img src={sqlalchemy} alt="sqlalchemy" /></div>
                                <span>sqlalchemy</span>
                            </li>
                            <li><div><img src={flask} alt="flask" /></div>
                                <span>flask</span>
                            </li>
                            <li><div><img src={redux} alt="redux" /></div>
                                <span>redux</span>
                            </li>
                            <li><div><img src={react} alt="react" /></div>
                                <span>react</span>
                            </li>
                            <li><div><img src={nodejs} alt="nodejs" /></div>
                                <span>nodejs</span>
                            </li>
                            <li><div><img src={javascript} alt="javascript" /></div>
                                <span>javascript</span>
                            </li>
                            <li><div><img src={css} alt="css3" /></div>
                                <span>css3</span>
                            </li>
                            <li><div><img src={github} alt="github" /></div>
                                <span>github</span>
                            </li>
                            <li><div><img src={docker} alt="docker" /></div>
                                <span>docker</span>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HomePage;
