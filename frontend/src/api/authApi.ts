import type { Spectator } from "../types/types";

const API_BASE_URL = "http://localhost:8000/api";

type RegistrationData = Omit<
  Spectator,
  "id" | "films_favoris" | "avatar" | "bio"
> & {
  password: string;
};

export const registerUser = async (userData: RegistrationData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/register/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || `Erreur HTTP: ${response.status}`);
    }
    return response.json();
  } catch (error) {
    console.error("Error in registerUser:", error);
    throw error;
  }
};

type LoginData = {
  username: string;
  password: string;
};

export const loginUser = async (userData: LoginData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/login/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || `Erreur HTTP: ${response.status}`);
    }

    return data;
  } catch (error) {
    console.error("Error in LoginUser:", error);
    throw error;
  }
};
