import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { Route } from 'react-router-dom';

import { Modal } from '../../context/Modal';
import LoginForm from "../LoginFormModal/LoginForm";


const ProtectedRoute = props => {
  const user = useSelector(state => state.session.user)
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    if (!user) {
      setShowModal(true)
    }
},[user]);

  return (
    <Route {...props}>
      {(user) ? props.children : showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <LoginForm setShowModal={setShowModal} />
        </Modal>
      )}
    </Route>
  )
};


export default ProtectedRoute;
