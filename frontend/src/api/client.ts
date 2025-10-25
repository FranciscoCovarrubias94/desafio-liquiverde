import axios from "axios";

const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1",
    headers: {
        "Content-Type": "application/json"
    },
    timeout: 5000,
});

export default apiClient;
