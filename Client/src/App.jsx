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
      <header className="header-bar">
        <img src="/LAH_Logo.png" alt="LAH" className="header-logo" />
      </header>

      <RouterProvider router={router} />

      <video
        className="bg-video"
        src="/logo.mp4"
        autoPlay
        muted
        loop
      />
      <div className="footer-bar" />
    </>
  );
}

export default App;
