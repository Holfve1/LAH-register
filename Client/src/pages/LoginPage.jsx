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
      <h2 className="text-3xl text-white font-semibold mb-6">Admin Login</h2>
      <form 
        onSubmit={handleLogin}
        className="flex flex-col gap-4 w-full max-w-xs items-center">
        <input
          type="password"
          placeholder="Enter admin password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-3 rounded bg-white text-black placeholder-gray-500 shadow focus:outline-none focus:ring-2 focus:ring-[#ea5136]"
        />
        <button 
        type="submit"
        className="p-3 w-fit rounded bg-[#ea5136] text-white font-medium hover:bg-[#d1442d] transition"
        >
          Login
        </button>
        <button 
        type="submit"
        className="p-3 w-fit rounded text-white font-medium hover:transition"
        >
          Forgot Password
        </button>
      </form>
    </main>
  );
}