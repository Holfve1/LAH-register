import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./App.css";


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
      <video
        className="bg-video"
        src="/CW_Logo_orange.mp4"
        autoPlay
        muted
        loop
      />
    </>
    
  );
}

export default App;
