import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App.tsx";
import { AuthProvider } from "./context/AuthContext.tsx"; // On importe notre Provider
import "./styles/main.scss";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    {/* On enveloppe notre composant App principal avec le AuthProvider */}
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>
);
