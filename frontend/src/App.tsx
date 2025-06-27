import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/layout/Layout";
import HomePage from "./pages/HomePage";
import MovieDetailPage from "./pages/MovieDetailPage";

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/films" element={<HomePage />} />
          <Route path="/films/:id" element={<MovieDetailPage />} />
          {/* <Route path="/authors" element={<HomePage />} /> */}
          {/* <Route path="/authors/<id>" element={<HomePage />} /> */}
          {/* <Route path="/login" element={<HomePage />} /> */}
          {/* <Route path="/register" element={<HomePage />} /> */}
          {/* <Route path="/profil" element={<HomePage />} /> */}
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
