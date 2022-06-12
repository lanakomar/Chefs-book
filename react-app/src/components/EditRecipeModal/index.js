import React, { useState } from 'react';

import CreateRecipeForm from '../CreateRecipeModal/CreateRecipeForm';
import { Modal } from '../../context/Modal';

const EditRecipeModal = ({id}) => {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <i className="fa-solid fa-file-pen"
                onClick={(e) => {
                    e.stopPropagation();
                    setShowModal(true)
                }} />
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <CreateRecipeForm setShowModal={setShowModal} edit={true} id={id}  />
                </Modal>
            )}
        </>
    );
}

export default EditRecipeModal;
