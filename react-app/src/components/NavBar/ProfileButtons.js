import React from "react";
import { Link } from "react-router-dom";

// import './Navigation.css';
import LogoutButton from '../auth/LogoutButton';


function ProfileButtons () {

    return (
        <div className="links-loggedin">
            <button>Your Grocery List</button>
            <Link to='/recipe-box'> Your Recipe Box</Link>
            <div>
                <span>gear icon</span>
                <div>
                    <ul>
                        <li>Profile</li>
                        <li><LogoutButton /></li>
                    </ul>
                </div>
            </div>

        </div>
    );
}

export default ProfileButtons;
