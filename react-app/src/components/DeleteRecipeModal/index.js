import { useState } from "react";
import DeleteRecipeForm from "./DeleteRecipeForm";
import { Modal } from "../../context/Modal";

const DeleteRecipeModal = ({ id, saved }) => {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <div className='delete-recipe' onClick={() => setShowModal(true)}>
                <i className="fa-solid fa-xmark"
                   onClick = {() => setShowModal(true)}
                />
            </div>
            {showModal && (
                <Modal
                    onClose={() => {
                        setShowModal(false);
                    }}
                >
                    <DeleteRecipeForm
                        setShowModal={setShowModal}
                        id={id}
                        saved={saved}
                    />
                </Modal>
            )}
        </>
    );
};

export default DeleteRecipeModal;
