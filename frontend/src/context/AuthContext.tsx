import { createContext, useState, useEffect, type ReactNode } from "react";
import { useContext } from "react";
import { jwtDecode } from "jwt-decode";
import type { Spectator, MyJwtPayload } from "../types/types";

type AuthContextType = {
  user: Spectator | null;
  login: (tokens: { access: string; refresh: string }) => void;
  logout: () => void;
} | null;

export const AuthContext = createContext<AuthContextType>(null);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<Spectator | null>(null);
  useEffect(() => {
    const tokens = localStorage.getItem("jwtTokens");
    if (tokens) {
      const serializedTokens = JSON.parse(tokens);

      const decodedToken: MyJwtPayload = jwtDecode(serializedTokens.access);
      if (decodedToken.exp * 1000 > Date.now()) {
        const userObj = {
          id: decodedToken.user_id,
          username: decodedToken.username,
        };
        setUser(userObj);
      } else {
        localStorage.removeItem("jwtTokens");
        setUser(null);
      }
    }
  }, []);

  const login = (tokens: { access: string; refresh: string }) => {
    localStorage.setItem("jwtTokens", JSON.stringify(tokens));
    const decodedToken: MyJwtPayload = jwtDecode(tokens.access);
    const userObj = {
      id: decodedToken.user_id,
      username: decodedToken.username,
    };
    console.log(decodedToken);
    setUser(userObj);
  };

  const logout = () => {
    localStorage.removeItem("jwtTokens");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth should be used inside an AuthProvider");
  }

  return context;
};
