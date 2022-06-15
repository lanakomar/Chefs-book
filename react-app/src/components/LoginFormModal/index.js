import React from 'react';
import { useStateIfMounted } from "use-state-if-mounted";

import LoginForm from "./LoginForm";
import { Modal } from '../../context/Modal';
import './LoginForm.css';


const LoginFormModal = () => {
    const [showModal, setShowModal] = useStateIfMounted(false);

    return (
        <>
            <button className="btn-nav" onClick={() => setShowModal(true)}>Log In</button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <LoginForm setShowModal={setShowModal}/>
                </Modal>
            )}
        </>
    );
}

export default LoginFormModal;
