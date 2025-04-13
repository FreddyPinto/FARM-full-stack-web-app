import {
  createBrowserRouter,
  Route,
  createRoutesFromElements,
  RouterProvider,
} from "react-router-dom";
import RootLayout from "./layouts/RootLayout";
import Cars from "./pages/Cars";
import { carsLoader } from "./loaders/carsLoader";
import Home from "./pages/Home";
import Login from "./pages/Login";
import NewCar from "./pages/NewCar";
import SingleCar from "./pages/SingleCar";
import NotFound from "./pages/NotFound";
import { AuthProvider } from "./contexts/AuthProvider";
import AuthRequired from "./components/AuthRequired";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      <Route index element={<Home />} />
      <Route path="/cars" element={<Cars />} loader={carsLoader} />
      <Route element={<AuthRequired />}>
        <Route path="/new-car" element={<NewCar />} />
      </Route>
      <Route path="/cars/:id" element={<SingleCar />} />
      <Route path="/login" element={<Login />} />
      <Route path="*" element={<NotFound />} />
    </Route>
  )
);
export default function App() {
  return (
    <AuthProvider>
      <RouterProvider router={router} />;
    </AuthProvider>
  );
}
