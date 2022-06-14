import { useState } from "react";
import { useDispatch } from "react-redux";

import ErrorMessage from '../ErrorMessage';
import { deleteNote } from '../../store/singleRecipe';

const DeleteNoteConfirmation = ({ setShowModal, id }) => {

    const [errorMessages, setErrorMessages] = useState({});
    const dispatch = useDispatch();

    const handleDelete = async (e) => {
        e.preventDefault();

        const data = await dispatch(deleteNote(id));

        if (data) {
            const errors = {};
            if (Array.isArray(data)) {
                data.forEach((error) => {
                    const label = error.split(":")[0].slice(0, -1);
                    const message = error.split(":")[1].slice(1);
                    errors[label] = message;
                });
            } else {
                errors.overall = data;
            }
            setErrorMessages(errors);
        }
    }

    const handleCancel = async (e) => {
        e.preventDefault();
        setShowModal(false);
    }

    return (
        <div className="confirmation-continer">
            <ErrorMessage label={""} message={errorMessages.overall} />
            <p>Are you sure you want to delete this note?</p>
            <ErrorMessage label={""} message={errorMessages.content} />
            <div className="confirm-buttons">
                <button onClick={handleCancel}>
                    Cancel
                </button>
                <button
                    className="delete-note-confirm"
                    onClick={handleDelete}
                >
                    Delete
                </button>
            </div>
        </div>
    )
};

export default DeleteNoteConfirmation;
