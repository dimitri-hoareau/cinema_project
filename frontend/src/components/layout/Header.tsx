import Navbar from "./Navbar";

const Header = () => {
  return (
    <header className="site-header">
      <div className="site-header__logo">
        <a href="/">CinéApp</a>
      </div>
      <Navbar />
      <div className="site-header__auth-buttons">
      </div>
    </header>
  );
};

export default Header;