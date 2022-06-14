import React, { useState } from 'react';

import GroceryList from "./GroceryList";
import { Modal } from '../../context/Modal';
// import './index.css'


const GroceryListModal = () => {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <button onClick={() => setShowModal(true)}>Your Grocery List</button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <GroceryList setShowModal={setShowModal} />
                </Modal>
            )}
        </>
    );
}

export default GroceryListModal;
