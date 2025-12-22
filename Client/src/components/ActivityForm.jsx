import { useState, useEffect } from "react";
import { createActivity, getAllActivities } from "../services/activities";

export function ActivityForm({ onSelectActivity }) {
  const [activity, setActivity] = useState("");
  const [activities, setActivities] = useState([]);
  const [error, setError] = useState("");
  const [showSuggestions, setShowSuggestions] = useState(false);

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

  const handleChange = (e) => {
    setActivity(e.target.value);
    setShowSuggestions(true);
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
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
        if (onSelectActivity) onSelectActivity(existing);
      } else {
        const created = await createActivity(trimmed);
        if (onSelectActivity) onSelectActivity(created.activity);
      }
      setShowSuggestions(false);
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

  const handleSelectSuggestion = (a) => {
    setActivity(a.activity);
    setShowSuggestions(false);
    if (onSelectActivity) onSelectActivity(a);
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
            onChange={handleChange}
          />

          {showSuggestions && filteredActivities.length > 0 && (
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
                  onClick={() => handleSelectSuggestion(a)}
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