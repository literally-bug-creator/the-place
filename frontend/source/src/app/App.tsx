import { BrowserRouter, Routes, Route } from 'react-router-dom'
import NavBar from './components/NavBar'
import Home from './pages/Home'
import About from './pages/About'
import Section from './pages/Section'
import Forum from './pages/Forum'
import CreatePost from './pages/CreatePost'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/section/:sectionId" element={<Section />} />
        <Route path="/forum" element={<Forum />} />
        <Route path="/create" element={<CreatePost />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App