import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

import "./index.css";

import logo from "../../images/logo.png";
import notFound from "../../images/notFound.jpeg";

const NotFound = () => {
  const history = useHistory();
  const [timeLeft, setTimeLeft] = useState(3);

  useEffect(() => {
    const timer = setTimeout(() => {
      history.push("/");
    }, 3000);
    return () => clearTimeout(timer);
  }, [history]);

  useEffect(() => {
    if (!timeLeft) return;
    const intervalId = setInterval(() => {
      setTimeLeft(timeLeft - 1);
    }, 1000);
    return () => clearInterval(intervalId);
  }, [timeLeft]);

  const handleOnClick = () => {
    history.push("/")
  }

  return (
    <div className="not-found-container">
      <img src={logo} className="logo-404" alt="logo" onClick={handleOnClick}/>
      <div className="not-found-msg">
        You will be redirected to home page in <span>{timeLeft}</span>{" "}
        seconds...
      </div>
      <div className="notFound-img"><img src={notFound} alt="page-not-found" /></div>
    </div>
  );
};

export default NotFound;
