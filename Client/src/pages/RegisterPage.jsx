import { AttendeeForm } from "../components/AttendeeForm";
import { LogoutButton } from "../components/LogoutButton";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export function RegisterPage() {
  const navigate = useNavigate();

  useEffect(() => {
    if (localStorage.getItem("isLoggedIn") !== "true") {
      navigate("/login");
    }
  }, [navigate]);

  return (
    <main className="pt-24">
      <div className="flex justify-end p-4">
        <LogoutButton />
      </div>

      <div>
        <AttendeeForm />
      </div>
      <div className="flex justify-center p-8">
        <button
          type="button"
          onClick={() => navigate("/view")}
          className="p-3 w-fit rounded bg-[#ea5136] text-white font-medium hover:bg-[#d1442d] transition cursor-pointer"
        >
          View Registrations
        </button>
      </div>
    </main>
  );
}