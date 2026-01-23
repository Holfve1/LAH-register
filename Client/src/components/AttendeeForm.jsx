// Client/src/components/AttendeeForm.jsx
import { useState } from "react";
import { createAttendee } from "../services/attendees";
import { createDate } from "../services/dates";
import { createRegistration } from "../services/registrations";
import { ActivityForm } from "./ActivityForm";
import { DateForm } from "./DateForm";

export function AttendeeForm() {
  const [selectedActivityId, setSelectedActivityId] = useState(null);
  const [selectedDate, setSelectedDate] = useState("");
  const [first_name, setFirst_name] = useState("");
  const [last_name, setLast_name] = useState("");
  const [suburb, setSuburb] = useState("");
  const [error, setError] = useState("");
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    console.log("Submit with:", {
      selectedActivityId,
      selectedDate,
      first_name,
      last_name,
      suburb,
    });

    if (!first_name) {
      setError("First name required");
      return;
    }
    if (!last_name) {
      setError("Last name required");
      return;
    }
    if (!selectedActivityId) {
      setError("Activity required");
      return;
    }
    if (!selectedDate) {
      setError("Date required");
      return;
    }

    try {
      const createdDate = await createDate(selectedDate, selectedActivityId);
      console.log("createdDate from API:", createdDate);
      const res = await createAttendee(first_name, last_name, suburb);
      console.log("attendee from API:", res);
      const attendeeId = res.attendee?.id;
      await createRegistration(createdDate.id, attendeeId);
      console.log("attendeeId:", attendeeId, "dateId:", createdDate.id);
    } catch (err) {
      console.error("Create attendee or registration failed:", err);
      setError("Could not create attendee/registration. Please try again.");
    }
  };

   return (
    <div className="p-6 font-sans">
      {/* child forms report up into this component */}
      <ActivityForm
        onSelectActivity={(activity) => setSelectedActivityId(activity.id)}
      />
      <DateForm
        date={selectedDate}
        onChangeDate={setSelectedDate}
      />

      <form onSubmit={handleSubmit}>
        <div>
          <input
            type="text"
            placeholder="First Name"
            value={first_name}
            onChange={(e) => setFirst_name(e.target.value)}
            className="w-72 p-3 mb-4 rounded bg-white text-black placeholder-gray-500 shadow focus:outline-none focus:ring-2 focus:ring-[#ea5136]"
          />
        </div>
        <div>
          <input
            type="text"
            placeholder="Last Name"
            value={last_name}
            onChange={(e) => setLast_name(e.target.value)}
            className="w-72 p-3 mb-4 rounded bg-white text-black placeholder-gray-500 shadow focus:outline-none focus:ring-2 focus:ring-[#ea5136]"
          />
        </div>
        <div>
          <input
            type="text"
            placeholder="Suburb"
            value={suburb}
            onChange={(e) => setSuburb(e.target.value)}
            className="w-72 p-3 mb-4 rounded bg-white text-black placeholder-gray-500 shadow focus:outline-none focus:ring-2 focus:ring-[#ea5136]"
          />
        </div>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <button>submit</button>
      </form>
    </div>
  );
}

export default AttendeeForm;