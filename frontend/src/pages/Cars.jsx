import { useLoaderData } from "react-router-dom";
import CarCard from "../components/CarCard";

const Cars = () => {
  const cars = useLoaderData();
  return (
    <div>
      <h1>Available cars</h1>
      <div className="md:grid md:grid-cols-3 sm:grid sm:grid-cols-2 gap-5">
        {cars.map((car) => (
          <CarCard key={car.id} car={car} />
        ))}
      </div>
    </div>
  );
};

export default Cars;
