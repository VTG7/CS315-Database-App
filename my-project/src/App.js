import React from 'react';
import { BrowserRouter, Routes, Route, Link} from "react-router-dom"
import Home from "./components/homepage"
import Login from "./components/login"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/login" element={<Login/>} />
      </Routes>
    </BrowserRouter>
  )
}