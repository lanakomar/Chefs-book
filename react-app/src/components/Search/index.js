import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import ReactTooltip from "react-tooltip";

import './index.css';

const Search = () => {
    const history = useHistory();
    const [query, setQuery] = useState("");
    const [tipMsg, setTipMsg] = useState(true);

    const handleInput = (e) => {
        setQuery(e.target.value);
        if (query.trim().length && query.replace(/[^a-zA-Z0-9 ]/g, '')) {
            setTipMsg(false);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (query && query.trim().length && query.replace(/[^a-zA-Z0-9 ]/g, '')) {
            setTipMsg(false);
            history.push(`/search/${query}`);
            setQuery("");
        };
    };

    const handleEnterKey = (e) => {
        if (e.key === 'Enter') {
            handleSubmit(e);
        }
    };

    return (
        <form id="search" onSubmit={handleSubmit}>
            <input
                type="text"
                value={query}
                onChange={handleInput}
                placeholder="Search recipes, i.e. beef"
                onKeyPress={handleEnterKey}
            />
            <button type="submit"
                    data-tip={tipMsg ? "Search cannot be empty" : null}
            >
                <i
                    className="fa-solid fa-magnifying-glass"
                    style={{cursor: tipMsg ? "not-allowed" : "pointer"}}
                />
            </button>
            <ReactTooltip place="right" type="warning" effect="solid" />
        </form>
    );
};

export default Search;
