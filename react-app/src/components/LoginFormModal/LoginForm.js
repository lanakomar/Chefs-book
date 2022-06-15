import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Redirect } from "react-router-dom";


import { login } from '../../store/session';
import ErrorMessage from "../ErrorMessage";
import './LoginForm.css';

const LoginForm = ({ setShowModal }) => {
    const dispatch = useDispatch();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessages, setErrorMessages] = useState({});
    const user = useSelector((state) => state.session.user);


    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await dispatch(login(email, password));
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
        } else {
            setShowModal(false);
        }
    }

    if (user) {
        return <Redirect to="/" />;
    }

    return (
        <div className='login-form-container'>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <ErrorMessage label={""} message={errorMessages.overall} />
                <div className='input-container'>
                    <label htmlFor='email'>Email</label>
                    <input
                        autoComplete="false"
                        type='text'
                        id='email'
                        name='email'
                        value={email}
                        required
                        onChange={(e) => setEmail(e.target.value)}
                    />
                    <ErrorMessage label={""} message={errorMessages.email} />
                </div>
                <div className='input-container'>
                    <label htmlFor='password'>Password</label>
                    <input
                        autoComplete="false"
                        type='password'
                        id='password'
                        name='password'
                        required
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                    <ErrorMessage label={""} message={errorMessages.password} />
                </div>
                <div className="login-btn-container">
                    <button className="login-form" type='submit'>Login</button>
                    <button className="login-form" type='button' onClick={() => setShowModal(false)}>Cancel</button>
                </div>
            </form>
        </div>
    )
};

export default LoginForm;
