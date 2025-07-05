import type { FilmStatusType } from "../types/types";

const API_BASE_URL = "http://localhost:8000/api";

export const getFilms = async (status: FilmStatusType | "") => {
  let url = `${API_BASE_URL}/films/`;

  if (status) {
    url += `?status=${status.toLowerCase()}`;
  }

  try {
    const response = await fetch(url);
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.detail || `HTTP Error: ${response.status}`);
    }

    return data;
  } catch (error) {
    console.error("Error on the films fetch:", error);
    throw error;
  }
};
