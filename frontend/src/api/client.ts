const API_BASE_URL = "http://localhost:8000/api";

export const fetchWithAuth = async (
  endpoint: string,
  options: RequestInit = {}
) => {
  const headers = new Headers({
    "Content-Type": "application/json",
    ...(options.headers || {}),
  });

  const storedTokens = localStorage.getItem("jwtTokens");
  if (storedTokens) {
    const tokens = JSON.parse(storedTokens);
    headers.set("Authorization", `Bearer ${tokens.access}`);
  }

  try {
    const response = await fetch(`${API_BASE_URL}/${endpoint}`, {
      headers: headers,
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || `Erreur HTTP: ${response.status}`);
    }
    return data;
  } catch (error) {
    console.error("Error:", error);
    throw error;
  }
};
