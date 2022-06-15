import React, { useState } from "react";
import { Link } from "react-router-dom";

import LogoutButton from '../auth/LogoutButton';
import GroceryListModal from '../GroceryList';


function ProfileButtons () {
    const [showMenu, setShowMenu] = useState(false);

    const openMenu = () => {
        if (showMenu) {
            setShowMenu(false)
        };
        setShowMenu(true);
    };

    const closeMenu = () => {
        setShowMenu(false);
    };

    return (
        <div className="links-loggedin">
            <div className="grocery-list-btn">
            <GroceryListModal />
            </div>
            <Link
                onMouseEnter={closeMenu}
                to='/recipe-box'
            >Your Recipe Box</Link>
            <div className="gear-menu" onMouseLeave={closeMenu}>
                <div
                    className="gear"
                    onMouseEnter={closeMenu}
                >
                    <i className="fa-solid fa-gear"
                        onMouseEnter={openMenu}
                    ></i></div>
                <div
                    style={{ display: showMenu ? "block" : "none" }}
                    className="dropdown-menu"
                >
                    <ul onMouseLeave={closeMenu}>
                        <li><LogoutButton /></li>
                    </ul>
                </div>
            </div>

        </div>
    );
}

export default ProfileButtons;
