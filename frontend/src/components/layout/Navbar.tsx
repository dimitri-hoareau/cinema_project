const Navbar = () => {
  return (
    <nav className="main-nav">
      <ul className="main-nav__list">
        <li className="main-nav__item">
          <a href="/" className="main-nav__link">Home</a>
        </li>
        <li className="main-nav__item">
          <a href="/films" className="main-nav__link">Films</a>
        </li>
        <li className="main-nav__item">
          <a href="/authors" className="main-nav__link">Authors</a>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;