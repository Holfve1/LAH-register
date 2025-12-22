const API_URL = import.meta.env.VITE_BACKEND_URL;

export async function createRegistration(date_id, attendee_id) {
    const payload = {
        date_id: date_id,
        attendee_id: attendee_id
    }
    const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload)
    };
    let response = await fetch(`${API_URL}/registrations`, requestOptions);

    if (response.status === 201) {
        return await response.json();
    } else {
        throw new Error(
            `Recieved status ${response.status} when creating registration. Expected 201`
        );
    }
}