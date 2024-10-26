import { BrowserRouter, Routes, Route } from "react-router-dom"
import Accueil from "./pages/Accueil"
import About from "./pages/About"
import Projets from "./pages/Projets"
import Dashboard from "./pages/Dashboard"
import Connexion from "./comptes/Connexion"
import Inscription from "./comptes/Inscription"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Accueil />} />
        <Route path="/about" element={<About />} />
        <Route path="/projets" element={<Projets />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/comptes/connexion" element={<Connexion />} />
        <Route path="/comptes/inscription" element={<Inscription />} />
      </Routes>
    </BrowserRouter>
  )
}
