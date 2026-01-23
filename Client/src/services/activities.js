const API_URL = import.meta.env.VITE_BACKEND_URL;

export async function createActivity(activity) {
    const payload = {
        activity: activity
    };
    const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload)
    };
    let response = await fetch(`${API_URL}/activities`, requestOptions);

    if (response.status === 201) {
        return await response.json();
    } else {
        throw new Error(
            `Recieved status ${response.status} when creating activity. Expected 201`
        );
    }
}

export async function getAllActivities() {
  const requestOptions = { method: "GET" };

  const response = await fetch(`${API_URL}/activities`, requestOptions);

  if (response.status !== 200) {
    throw new Error("Unable to fetch Activities");
  }

  const data = await response.json();

  const uniqueByName = [
    ...new Map(data.map(activity => [activity.activity, activity])).values(),
  ];

  return uniqueByName;
}