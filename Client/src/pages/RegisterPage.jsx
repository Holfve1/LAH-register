import { useState } from "react";
import { createAttendee } from "../services/attendees";




const API_URL = import.meta.env.VITE_BACKEND_URL;

export function RegisterPage() {
  const [first_name, setFirst_name] = useState("");
  const [last_name, setLast_name] = useState("");
  const [suburb, setSuburb] = useState("");
  const [error, setError] = useState("");
  
  
  const handleSubmit = async (event) => {
    event.preventDefault();
    setError("")

    if (!first_name) {
      setError("First name required");
      return;
    }
    try {
      const res = await createAttendee(
        first_name,
        last_name,
        suburb
      )
    } catch (err) {
      console.error("Create attendee failed:", err);
      setError("Could not create Attendee. Please try again.");
    }
  }
  
  
  return (
    <div style={{ padding: 24, fontFamily: 'system-ui, sans-serif' }}>
      <form onSubmit={handleSubmit}>
        <div>
          <label>First Name</label>
          <input 
          type="text"
          placeholder="First Name"
          value={first_name}
          onChange={(e) => setFirst_name(e.target.value)}
          />
        </div>
        <div>
          <label>Last Name</label>
          <input 
          type="text"
          placeholder="Last Name"
          value={last_name}
          onChange={(e) => setLast_name(e.target.value)}
          />
        </div>
        <div>
          <label>Suburb</label>
          <input 
          type="text"
          placeholder="Suburb"
          value={suburb}
          onChange={(e) => setSuburb(e.target.value)}
          />
        </div>
        <button>submit</button>
      </form>
    </div>
  )
}