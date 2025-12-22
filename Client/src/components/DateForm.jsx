import { useState } from "react";

export function DateForm({ date, onChangeDate }) {
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const value = e.target.value;
    console.log("Date change:", value);
    onChangeDate(value);
    setError("");
    if (!value) {
      setError("Date required");
    }
  };

  return (
    <div style={{ padding: 24, fontFamily: "system-ui, sans-serif" }}>
      <div>
        <label>Date</label>
        <input
          type="date"
          value={date}
          onChange={handleChange}
        />
      </div>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

export default DateForm;