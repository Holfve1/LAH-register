import { useState, useEffect } from "react";
import { createActivity, getAllActivities } from "../services/activities";

export function ActivityForm() {
  const [activity, setActivity] = useState("");
  const [activities, setActivities] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadActivities() {
      try {
        const data = await getAllActivities();
        setActivities(data);
      } catch (err) {
        console.error("Failed to load activities:", err);
        setError("Could not load activities.");
      }
    }
    loadActivities();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError("");

    const trimmed = activity.trim();
    if (!trimmed) {
      setError("Activity required");
      return;
    }

    const existing = activities.find(
      (a) => a.activity.toLowerCase() === trimmed.toLowerCase()
    );

    try {
      if (existing) {
        console.log("Using existing activity:", existing);
      } else {
        await createActivity(trimmed);
      }
    } catch (err) {
      console.error("Create activity failed:", err);
      setError("Could not create activity. Please try again.");
    }
  };

  const filteredActivities =
    activity.trim().length === 0
      ? []
      : activities.filter((a) =>
          a.activity.toLowerCase().includes(activity.toLowerCase())
        );

  const handleSelectSuggestion = (name) => {
    setActivity(name);
  };

  return (
    <div style={{ padding: 24, fontFamily: "system-ui, sans-serif" }}>
      <form onSubmit={handleSubmit}>
        <div style={{ position: "relative" }}>
          <label>Activity</label>
          <input
            type="text"
            placeholder="Activity"
            value={activity}
            onChange={(e) => setActivity(e.target.value)}
          />

          {filteredActivities.length > 0 && (
            <ul
              style={{
                position: "absolute",
                zIndex: 1,
                background: "white",
                border: "1px solid #ccc",
                listStyle: "none",
                margin: 0,
                padding: 0,
                width: "100%",
              }}
            >
              {filteredActivities.map((a) => (
                <li
                  key={a.id}
                  style={{ padding: "4px 8px", cursor: "pointer" }}
                  onClick={() => handleSelectSuggestion(a.activity)}
                >
                  {a.activity}
                </li>
              ))}
            </ul>
          )}
        </div>

        {error && <p style={{ color: "red" }}>{error}</p>}

        <button>submit</button>
      </form>
    </div>
  );
}

export default ActivityForm;