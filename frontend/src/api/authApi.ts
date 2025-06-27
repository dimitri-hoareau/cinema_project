import type { Spectator } from "../types/types";

const API_BASE_URL = "http://localhost:8000/api";

type RegistrationData = Omit<
  Spectator,
  "id" | "films_favoris" | "avatar" | "bio"
> & {
  password: string;
};

const registerUser = async (userData: RegistrationData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/register/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    });

    console.log(JSON.stringify(userData));

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

export default registerUser;
