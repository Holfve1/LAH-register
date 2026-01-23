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

      <div className="mt-24">
        <AttendeeForm />
      </div>
    </main>
  );
}