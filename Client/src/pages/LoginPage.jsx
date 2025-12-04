import { useState } from "react";
import { useNavigate } from "react-router-dom";

const API_URL = import.meta.env.VITE_BACKEND_URL;

export function LoginPage() {
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  async function handleLogin(e) {
    e.preventDefault();
    try {
      const res = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password }),
      });
      const data = await res.json();
      if (data.success) {
        localStorage.setItem("isLoggedIn", "true");
        navigate("/register");
      } else {
        alert("Invalid password");
      }
    } catch (error) {
      console.error(error);
      alert("Error connecting to server");
    }
  }

  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-4">
      <h2>Admin Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type="password"
          placeholder="Enter admin password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
    </main>
  );
}