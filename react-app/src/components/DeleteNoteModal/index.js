import { useState } from "react";

import DeleteNoteConfirmation from "./DeleteNoteConfirmation";
import { Modal } from "../../context/Modal";
import './index.css'

const DeleteNoteModal = ({ noteId }) => {
    const [showModal, setShowModal] = useState(false);
    return (
        <>
            <div className='delete'>
                <i
                    className="fa-solid fa-trash"
                    onClick={() => setShowModal(true)}
                ></i>
            </div>
            {showModal && (
                <Modal
                    onClose={() => {
                        setShowModal(false);
                    }}
                >
                    <DeleteNoteConfirmation
                        setShowModal={setShowModal}
                        id={noteId}
                    />
                </Modal>
            )}
        </>
    );
};

export default DeleteNoteModal;
