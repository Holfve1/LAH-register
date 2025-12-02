import { createBrowserRouter, RouterProvider } from "react-router-dom";


import { LoginPage } from "./pages/LoginPage";
import { RegisterPage } from "./pages/RegisterPage";
import { ViewPage } from "./pages/ViewPage";

const router = createBrowserRouter([

    {path: "/", element: <LoginPage />,},
    {path: "/login", element: <LoginPage />,},
    {path: "/register", element: <RegisterPage />,},
    {path: "/view", element: <ViewPage />,},
    
]);

function App() {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
