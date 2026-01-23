import { useState, useEffect } from "react";
import { getAllActivitiesWithDatesAndAttendees } from "../services/dates";

export function SearchByDate() {
  const [allRows, setAllRows] = useState([]);
  const [selectedDate, setSelectedDate] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  function formatDateDisplay(isoDate) {
  if (!isoDate) return "";
  const [year, month, day] = isoDate.split("-");
  return `${day}/${month}/${year}`; // e.g. 2024-06-01 -> 01/06/2024
}

  useEffect(() => {
    (async () => {
      setLoading(true);
      setError("");
      try {
        const data = await getAllActivitiesWithDatesAndAttendees();
        setAllRows(data);
      } catch (err) {
        console.error(err);
        setError("Could not load dates. Please try again.");
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  function handleSearch(e) {
    e.preventDefault();
    setError("");
    setResults([]);

    if (!selectedDate) {
      setError("Please select a date.");
      return;
    }

    const rowsForDate = allRows.filter((row) => row.date === selectedDate);
    setResults(rowsForDate);
  }

  // unique list of dates for the dropdown
  const uniqueDates = [...new Set(allRows.map((row) => row.date))].sort(
  (a, b) => new Date(b) - new Date(a)
);

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
          value={selectedDate}
          onChange={(e) => setSelectedDate(e.target.value)}
          style={{ padding: "4px 8px", marginRight: 8, color: "white" }}
        >
          <option value="">Select a date...</option>
          {uniqueDates.map((d) => (
            <option key={d} value={d}>
                {formatDateDisplay(d)}
            </option>
            ))}
        </select>

        <button
          type="submit"
          disabled={loading || !uniqueDates.length}
          style={{ color: "white" }}
        >
          {loading ? "Loading..." : "Show activities & attendees"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {results.length > 0 && (
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
                colSpan={3}
                style={{
                  borderBottom: "1px solid white",
                  color: "white",
                  fontSize: "24px",
                }}
              >
                ACTIVITIES AND ATTENDEES ON: {selectedDate}
              </th>
            </tr>
            <tr>
              <th style={{ color: "white", textAlign: "left" }}>Activity</th>
              <th style={{ color: "white", textAlign: "left" }}>First name</th>
              <th style={{ color: "white", textAlign: "left" }}>Last name</th>
            </tr>
          </thead>
          <tbody>
            {results.map((row, index) => (
              <tr key={index}>
                <td style={{ padding: "4px 8px", color: "white" }}>
                  {row.activity}
                </td>
                <td style={{ padding: "4px 8px", color: "white" }}>
                  {row.first_name}
                </td>
                <td style={{ padding: "4px 8px", color: "white" }}>
                  {row.last_name}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}