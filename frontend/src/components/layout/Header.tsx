import Navbar from "./Navbar";
import "../../styles/components/_header.scss";

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
