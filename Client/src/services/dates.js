const API_URL = import.meta.env.VITE_BACKEND_URL;

export async function createDate(date, activity_id) {
    const payload = {
        date: date,
        activity_id: activity_id
    };
    const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload)
    };
    let response = await fetch(`${API_URL}/dates`, requestOptions);

    if (response.status === 201) {
        return await response.json();
    } else {
        throw new Error(
            `Recieved status ${response.status} when creating date. Expected 201`
        );
    }
}