import { useLoaderData } from "react-router-dom";
import CarCard from "../components/CarCard";

const SingleCar = () => {
  const carData = useLoaderData();
  return <CarCard car={carData} />;
};

export default SingleCar;
