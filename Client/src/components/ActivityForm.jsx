import { useState, useEffect, useRef } from "react";
import { createActivity, getAllActivities } from "../services/activities";

export function ActivityForm({ onSelectActivity }) {
  const [activity, setActivity] = useState("");
  const [activities, setActivities] = useState([]);
  const [error, setError] = useState("");
  const [showSuggestions, setShowSuggestions] = useState(false);
  const inputRef = useRef(null);

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

    if (inputRef.current) {
    inputRef.current.blur();
    }

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
    if (inputRef.current) inputRef.current.blur();
  };

  return (
    <div className="p-6 font-sans">
      <form onSubmit={handleSubmit}>
        <div className="relative inline-block w-72">
          <div className="mb-6">
            <label className="text-3xl text-white mb-6">Register</label>  
          </div>
          <input
            ref={inputRef}
            type="text"
            placeholder="Activity"
            value={activity}
            onChange={handleChange}
            className="w-full p-3 rounded bg-white text-black placeholder-gray-500 shadow focus:outline-none focus:ring-2 focus:ring-[#ea5136]"
          />

          {showSuggestions && filteredActivities.length > 0 && (
            <ul className=
            "absolute left-0 top-full z-10 mt-1 w-full bg-white border border-gray-300 rounded shadow list-none m-0 p-0">
              {filteredActivities.map((a) => (
                <li key={a.id} className="px-2 py-1 cursor-pointer hover:bg-gray-100" onClick={() => handleSelectSuggestion(a)} >
                  {a.activity}
                </li>
              ))}
            </ul>
          )}
        </div>

        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>
    </div>
  );
}

export default ActivityForm;