import { useState, useEffect } from "react";
import { getAllActivities } from "../services/activities";
import { getDatesAndAttendeesByActivityId, getAllActivitiesWithDatesAndAttendees } from "../services/dates";

const API_URL = import.meta.env.VITE_BACKEND_URL;


export function SearchByActivity() {
  const [activities, setActivities] = useState([]);
  const [dates, setDates] = useState([]);
  const [selectedActivityId, setSelectedActivityId] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [selectedDate, setSelectedDate] = useState("");
  const [attendees, setAttendees] = useState([]);
  const [selectedAttendeeName, setSelectedAttendeeName] = useState("");
  const [attendeeActivities, setAttendeeActivities] = useState([]);

function formatDateDisplay(isoDate) {
  if (!isoDate) return "";
  const [year, month, day] = isoDate.split("-");
  return `${day}/${month}/${year}`; // 2024-06-01 -> 01/06/2024
}

  useEffect(() => {
    (async () => {
      try {
        const data = await getAllActivities();
        setActivities(data);
      } catch (err) {
        console.error(err);
        setError("Could not load activities. Please try again.");
      }
    })();
  }, []);

  async function handleSearch(e) {
    e.preventDefault();
    setError("");
    setDates([]);
    setAttendees([]);
    setSelectedDate("");
    setLoading(true);

    try {
      if (!selectedActivityId) {
        setError("Please select an activity.");
        return;
      }

      const result = await getDatesAndAttendeesByActivityId(selectedActivityId);
      setDates(result);
    } catch (err) {
      console.error(err);
      setError("Could not load dates for that activity.");
    } finally {
      setLoading(false);
    }
  }

  function handleDateClick(date) {
    setSelectedDate(date);
    const peopleForDate = dates.filter((item) => item.date === date);
    setAttendees(peopleForDate);
  }

  const selectedActivity = activities.find(
    (a) => String(a.id) === String(selectedActivityId)
  );

  async function handleAttendeeClick(person) {
  setSelectedAttendeeName(`${person.first_name} ${person.last_name}`);
  setAttendeeActivities([]);
  setLoading(true);
  setError("");

  try {
    const allRows = await getAllActivitiesWithDatesAndAttendees();
    const rowsForThisPerson = allRows.filter(
      (row) =>
        row.first_name === person.first_name &&
        row.last_name === person.last_name
    );
    setAttendeeActivities(rowsForThisPerson);
  } catch (err) {
    console.error(err);
    setError("Could not load activities for that attendee.");
  } finally {
    setLoading(false);
  }
}

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: "system-ui, sans-serif",
        padding: 24,
        marginTop: 80,
        marginBottom: 65,
      }}
    >
      <form onSubmit={handleSearch} style={{ marginBottom: 16 }}>
        <select
          value={selectedActivityId}
          onChange={(e) => setSelectedActivityId(e.target.value)}
          style={{ padding: "4px 8px", marginRight: 8, color: "white"}}
        >
          <option value="">Select an activity...</option>
          {activities.map((activity) => (
            <option key={activity.id} value={activity.id}>
              {activity.activity}
            </option>
          ))}
        </select>

        <button
          type="submit"
          disabled={loading || !activities.length}
          style={{ color: "white" }}
        >
          {loading ? "Searching..." : "Show dates"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {dates.length > 0 && (
        <table
          style={{
            marginTop: 16,
            borderCollapse: "collapse",
            width: "100%",
          }}
        >
          <thead>
            <tr>
              <th
                style={{
                  borderBottom: "1px solid white",
                  color: "white",
                  fontSize: "30px",
                }}
              >
              {selectedActivity ? selectedActivity.activity : "Activity"} Dates
              </th>
            </tr>
          </thead>
          <tbody>
            {dates.map((item, index) => (
              <tr
                key={index}
                onClick={() => handleDateClick(item.date)}
                style={{ cursor: "pointer" }}
              >
                <td style={{ padding: "4px 8px", color: "white" }}>
                  {formatDateDisplay(item.date)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {attendees.length > 0 && (
        <table
          style={{
            marginTop: 16,
            borderCollapse: "collapse",
            width: "100%",
          }}
        >
          <thead>
            <tr>
              <th
                colSpan={2}
                style={{
                  borderBottom: "1px solid white",
                  color: "white",
                  fontSize: "30px",
                }}
              >
                Attendees for {selectedActivity ? selectedActivity.activity : "Activity"} on {formatDateDisplay(selectedDate)}
              </th>
            </tr>
            <tr>
              <th style={{ color: "white", textAlign: "left", fontSize: "20px" }}>First name</th>
              <th style={{ color: "white", textAlign: "left", fontSize: "20px"  }}>Last name</th>
            </tr>
          </thead>
          <tbody>
            {attendees.map((person, index) => (
              <tr key={index}>
                <td
                  style={{ padding: "4px 8px", color: "white", cursor: "pointer" }}
                  onClick={() => handleAttendeeClick(person)}
                >
                  {person.first_name}
                </td>
                <td
                  style={{ padding: "4px 8px", color: "white", cursor: "pointer" }}
                  onClick={() => handleAttendeeClick(person)}
                >
                  {person.last_name}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      {attendeeActivities.length > 0 && (
  <table
    style={{
      marginTop: 16,
      borderCollapse: "collapse",
      width: "100%",
    }}
  >
    <thead>
      <tr>
        <th
          colSpan={2}
          style={{
            borderBottom: "1px solid white",
            color: "white",
            fontSize: "30px",
          }}
        >
          Activities {selectedAttendeeName} Attended
        </th>
      </tr>
      <tr>
        <th style={{ color: "white", textAlign: "left" }}>Activity</th>
        <th style={{ color: "white", textAlign: "left" }}>Date</th>
      </tr>
    </thead>
    <tbody>
      {attendeeActivities.map((item, index) => (
        <tr key={index}>
          <td style={{ padding: "4px 8px", color: "white" }}>
            {item.activity}
          </td>
          <td style={{ padding: "4px 8px", color: "white" }}>
            {item.date}
          </td>
        </tr>
      ))}
    </tbody>
  </table>
)}
    </div>
  );
}