import { useState } from 'react';
import { useParams, useHistory } from "react-router-dom";
import { useSelector } from "react-redux";
import { useStateIfMounted } from "use-state-if-mounted";


import { Modal } from '../../context/Modal';
import LoginForm from "../LoginFormModal/LoginForm";


const SearchResult = () => {
    const { searchQuery } = useParams();
    const [showModal, setShowModal] = useStateIfMounted(false);
    const [redirectId, setRedirectId] = useState();


    let recipes = useSelector((state) => state.recipes);
    recipes = Object.values(recipes);
    const user = useSelector((state) => state.session.user);
    const history = useHistory();


    const results = recipes.filter(
        (recipe) =>
            recipe?.title?.toLowerCase().indexOf(searchQuery.toLowerCase()) >= 0
    );

    const loginModal = (showModal && (
        <Modal onClose={() => setShowModal(false)}>
            <LoginForm setShowModal={setShowModal} recipeId={redirectId} />
        </Modal>));

    const cardClick = (e) => {
        const recipeId = e.currentTarget.id;
        if (user) {
            history.push(`/recipes/${recipeId}`)
        } else {
            setRedirectId(recipeId);
            setShowModal(true);
        }
    };

    return (
        <div className="result-container">
            {loginModal}
            <div className="main-container">
                <div className="search-result-header">
                    Showing Results for
                    <span> "{searchQuery}" </span>
                </div>
                {!results.length ? (
                    <div className="no-results">
                        <div id="no-result-msg">NO RECIPES FOUND</div>
                    </div>
                ) : (
                    <div className="recipes-container">
                        {results.map((recipe) => (
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
                )}
            </div>
        </div>
    );

};

export default SearchResult;
