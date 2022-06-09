import React, { useState } from 'react';

import CreateRecipeForm from "./CreateRecipeForm";
import { Modal } from '../../context/Modal';
import './index.css'


const CreateRecipeModal = () => {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <button className="btn-nav" onClick={() => setShowModal(true)}>
                <i className="fa-solid fa-plus"></i>
                Add a recipe
            </button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <CreateRecipeForm setShowModal={setShowModal} />
                </Modal>
            )}
        </>
    );
}

export default CreateRecipeModal;
