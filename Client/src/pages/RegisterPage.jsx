import { ActivityForm } from "../components/ActivityForm";
import AttendeeForm from "../components/AttendeeForm";





const API_URL = import.meta.env.VITE_BACKEND_URL;

export function RegisterPage() {
  
  return (
    <>
    <ActivityForm/>
    <AttendeeForm/>
    </>
  )
}