import { Link } from "react-router-dom";
import "../../styles/components/_navbar.scss";

const Navbar = () => {
  return (
    <nav className="main-nav">
      <ul className="main-nav__list">
        <li className="main-nav__item">
          <Link to="/" className="main-nav__link">
            Home
          </Link>
        </li>
        <li className="main-nav__item">
          <Link to="/films" className="main-nav__link">
            Films
          </Link>
        </li>
        <li className="main-nav__item">
          <Link to="/authors" className="main-nav__link">
            Authors
          </Link>
        </li>
      </ul>
      <div className="main-nav__auth">
        <Link to="/login" className="button button--ghost">
          Login
        </Link>
        <Link to="/register" className="button button--primary">
          Register
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
