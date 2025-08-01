
import type { ReactNode } from 'react';
import Header from './Header';
import Footer from './Footer';



type LayoutProps = {
  children: ReactNode;
};

const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="site-wrapper">
      <Header />
      <main className="site-wrapper__content">
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default Layout;