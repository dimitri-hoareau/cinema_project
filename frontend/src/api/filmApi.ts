const API_BASE_URL = "http://localhost:8000/api";

export const getFilms = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/films/`, {});

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || `Erreur HTTP: ${response.status}`);
    }
    return response.json();
  } catch (error) {
    console.error("Error on the films fetch:", error);
    throw error;
  }
};
