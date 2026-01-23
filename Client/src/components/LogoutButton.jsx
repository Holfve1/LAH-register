import { useNavigate } from "react-router-dom";

export function LogoutButton() {
  const navigate = useNavigate();

  function handleLogout() {
    // Remove login flag
    localStorage.removeItem("isLoggedIn");

    // Redirect to login page
    navigate("/login");
  }

  return (
    <button
      onClick={handleLogout}
      className="p-3 w-fit rounded bg-[#ea5136] text-white font-medium hover:bg-[#d1442d] transition"
    >
      Logout
    </button>
  );
}