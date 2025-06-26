import Navbar from "./Navbar";

const Header = () => {
  return (
    <header className="site-header">
      <div className="site-header__logo">
        <a href="/">CinéApp</a>
      </div>
      <Navbar />
    </header>
  );
};

export default Header;