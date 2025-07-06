import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { useNavigate } from "react-router-dom";
import "../../styles/components/_navbar.scss";

const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/");
  };
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
        {user ? (
          <>
            <Link to="/profile" className="main-nav__link">
              {user.username}
            </Link>

            <button onClick={handleLogout} className="button button--secondary">
              Déconnexion
            </button>
          </>
        ) : (
          <>
            <Link to="/login" className="button button--ghost">
              Login
            </Link>
            <Link to="/register" className="button button--primary">
              Register
            </Link>
          </>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
