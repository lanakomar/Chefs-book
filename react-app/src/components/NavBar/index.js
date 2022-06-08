
import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink } from 'react-router-dom';

import LogoutButton from '../auth/LogoutButton';
import ProfileButtons from './ProfileButtons';
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';
import { login } from '../../store/session';

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
      <>
        <button className="btn-nav" to="/login" onClick={demoLogin}>Demo user</button>
        <LoginFormModal />
        <SignupFormModal />
      </>
    )
  }


  return (
    <nav>
      <div>
        <div>
          <NavLink to='/' exact={true} activeClassName='active'>
            Home/Logo
          </NavLink>
        </div>
        <div>{sessionLinks}</div>
      </div>
    </nav>
  );
}

export default NavBar;
