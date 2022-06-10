import React, { useState } from "react";
import { Link } from "react-router-dom";

import LogoutButton from '../auth/LogoutButton';


function ProfileButtons () {
    const [showMenu, setShowMenu] = useState(false);

    // const styles = {
    //     color: "#e33d26",
    //     backgroundColor: "#f2f3ef",
    //     border: "1px solid #ccc",
    //     borderBottom: "none",
    //     borderRadius: "2px 2px 0 0"
    // };

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
            <button >Your Grocery List</button>
            </div>
            <Link
                onMouseEnter={closeMenu}
                // style={isTab ? styles : null}
                to='/recipe-box'
            >Your Recipe Box</Link>
            <div className="gear-menu">
                <div
                    className="gear"
                    onMouseEnter={openMenu}
                >
                    <i className="fa-solid fa-gear"
                    ></i></div>
                <div
                    style={{ display: showMenu ? "block" : "none" }}
                    className="dropdown-menu"
                >
                    <ul onMouseLeave={closeMenu}>
                        <li>Profile</li>
                        <li><LogoutButton /></li>
                    </ul>
                </div>
            </div>

        </div>
    );
}

export default ProfileButtons;
