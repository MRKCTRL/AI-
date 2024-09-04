const API_URL = "http://localhost:8000/api/v1";

export async function loginUser(credentials) {
  return fetch(`${API_URL}/auth/login/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  }).then((response) => response.json());
}

export async function getRecommendations() {
  return fetch(`${API_URL}/recommend/`).then((response) => response.json());
}

// Other API calls...
