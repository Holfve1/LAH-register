const API_URL = import.meta.env.VITE_BACKEND_URL;

export async function createAttendee(first_name, last_name, suburb) {

    const payload = {
        first_name: first_name,
        last_name: last_name,
        suburb: suburb
    }
    const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload),
    };
    let response = await fetch(`${API_URL}/attendees`, requestOptions);

    if (response.status === 201) {
        return await response.json();
    } else {
        throw new Error(
            `Recieved status ${response.status} when creating attendee. Expected 201`
        );
    }
}