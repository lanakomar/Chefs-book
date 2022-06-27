import React, { useState } from 'react';

import CreateRecipeForm from '../CreateRecipeModal/CreateRecipeForm';
import { Modal } from '../../context/Modal';
import { useSelector } from 'react-redux';

const EditRecipeModal = ({ id, author }) => {
    const [showModal, setShowModal] = useState(false);
    const user = useSelector(state => state.session.user);

    return (
        <>
        {user.id === author ?
                <>
                    <i className="fa-solid fa-file-pen"
                        onClick={(e) => {
                            e.stopPropagation();
                            setShowModal(true)
                        }} />
                    {showModal && (
                        <Modal onClose={() => setShowModal(false)}>
                            <CreateRecipeForm setShowModal={setShowModal} edit={true} id={id} />
                        </Modal>
                    )}
                </>
                : null
        }
        </>
    );
}

export default EditRecipeModal;
