export const carsLoader = async () => {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/cars?limit=30`);

  const response = await res.json();

  if (!res.ok) {
    throw new Error(response.message);
  }

  return response["cars"];
};
