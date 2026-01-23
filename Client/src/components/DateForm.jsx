import { useState, useRef  } from "react";

export function DateForm({ date, onChangeDate }) {
  const [error, setError] = useState("");
  const inputRef = useRef(null);

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
    <div className="flex flex-col items-center mb-6">
      <div className="relative flex items-center">
      <input
        ref={inputRef}
        type="date"
        value={date}
        onChange={handleChange}
        className="text-3xl text-white date-white pr-10 bg-transparent leading-none"
      />
      <button
        type="button"
        onClick={() => {
          if (inputRef.current?.showPicker) {
            inputRef.current.showPicker();
          } else {
            inputRef.current?.focus();
          }
        }}
        className="absolute right-2 items-center justify-center cursor-pointer"
        aria-label="Open date picker"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
          className="w-6 h-6 text-white"
        >
          <path d="M7 2a1 1 0 0 1 1 1v1h8V3a1 1 0 1 1 2 0v1h1a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1V3a1 1 0 0 1 1-1Zm12 9H5v9a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-9ZM5 8h14V6a1 1 0 0 0-1-1h-1v1a1 1 0 1 1-2 0V5H8v1a1 1 0 1 1-2 0V5H5a1 1 0 0 0-1 1v2Z"/>
        </svg>
      </button>
    </div>
    </div>
  );
}

export default DateForm;