
import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom';

import ProfileButtons from './ProfileButtons';
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';
import ErrorMessage from "../ErrorMessage";
import Search from '../Search';
import { login } from '../../store/session';
import logo from '../../images/logo.png'
import './index.css';

const NavBar = () => {
  const [errorMessages, setErrorMessages] = useState({});
  const session = useSelector((state => state.session.user));
  const dispatch = useDispatch();


  const demoLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("demo@aa.io", "password"));
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

  let sessionLinks;
  if (session) {
    sessionLinks = (
      <ProfileButtons />
    )
  } else {
    sessionLinks = (
      <div>
        <ErrorMessage label={""} message={errorMessages.overall} />
        <button className="btn-nav" to="/login" onClick={demoLogin}>Demo user</button>
        <LoginFormModal />
        <SignupFormModal />
      </div>
    )
  }

  return (
    <nav>
      <div>
        <NavLink to='/' exact={true} activeClassName='active'>
          <img className='logo' src={logo} alt="chef's-book-logo" />
        </NavLink>
      </div>
      <div className='search-container'>
        <Search />
      </div>
      {sessionLinks}
    </nav>
  );
}

export default NavBar;
