import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import ErrorMessage from "../ErrorMessage";
import { signUp } from "../../store/session";
import './SignupForm.css';

function SignupForm({ setShowModal }) {
    const dispatch = useDispatch();
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [errorMessages, setErrorMessages] = useState({});
    const user = useSelector((state) => state.session.user);



    const handleSubmit = async (e) => {
        e.preventDefault();
        if (password === confirmPassword) {
            const data = await dispatch(
                signUp(username, email, password)
            );
            if (data) {
                const errors = {};
                if (Array.isArray(data.errors)) {
                    data.errors.forEach((error) => {
                        const label = error.split(":")[0].slice(0, -1);
                        const message = error.split(":")[1].slice(1);
                        errors[label] = message;
                    });
                } else {
                    errors.overall = data;
                }
                setErrorMessages(errors);
            }
        } else {
            const errors = {};
            errors.confirmPassword = "Confirm password doesn't match Password";
            setErrorMessages(errors);
        }
    };

    if (user) {
        return <Redirect to="/" />;
    }

    return (
        <div className='signup-form-container'>
            <h1>Sign Up</h1>
            <form onSubmit={handleSubmit}>
            <ErrorMessage label={""} message={errorMessages.overall} />
                <div className='input-container'>
                    <label htmlFor="email">Email</label>
                    <input
                        id="email"
                        autoComplete="false"
                        type="text"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                    <ErrorMessage label={""} message={errorMessages.email} />
                </div>
                <div className='input-container'>
                    <label htmlFor="username">Username</label>
                    <input
                        id="username"
                        autoComplete="false"
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                    <ErrorMessage label={""} message={errorMessages.username} />
                </div>
                <div className='input-container'>
                    <label htmlFor="password">Password</label>
                    <input
                        id="password"
                        autoComplete="false"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <ErrorMessage label={""} message={errorMessages.password} />
                </div>
                <div className='input-container'>
                    <label htmlFor="confirm-password">Confirm Password</label>
                    <input
                        id="confirm-password"
                        autoComplete="false"
                        type="password"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        required
                    />
                    <ErrorMessage label={""} message={errorMessages.confirmPassword} />
                </div>
                <div className="signup-btn-container">
                    <button className="sign-up-form" type="submit">Sign Up</button>
                    <button className="sign-up-form" type='button' onClick={() => setShowModal(false)}>Cancel</button>
                </div>
            </form>
        </div>
    );
}

export default SignupForm;
