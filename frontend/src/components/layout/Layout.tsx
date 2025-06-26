import Header from './Header';
import Footer from './Footer'; 
import type { ReactNode } from 'react';

type LayoutProps = {
  children: ReactNode;
};

const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="site-wrapper">
      <Header />
      <main className="site-wrapper__main-content">
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default Layout;