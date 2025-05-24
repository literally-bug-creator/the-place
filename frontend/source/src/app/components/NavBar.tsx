import { Link, useNavigate } from 'react-router-dom'
import './NavBar.css'

export default function NavBar() {
  const navigate = useNavigate()

  // Переход на страницу "О нас" при клике на логотип
  const handleLogoClick = () => {
    navigate('/about')
  }

  return (
    <nav className="navbar">
      <div className="logo" onClick={handleLogoClick}>
        The Place
      </div>
      <ul className="nav-links">
        <li><Link to="/">Главная</Link></li>
        <li><Link to="/section/gi">Г.И.</Link></li>
        <li><Link to="/section/sm">С.М.</Link></li>
        <li><Link to="/section/as">А.С.</Link></li>
        <li><Link to="/section/chp">Ч.П.</Link></li>
        <li><Link to="/forum">Форум (Г.И.)</Link></li>
        <li><Link to="/create">Создать пост</Link></li>
      </ul>
    </nav>
  )
}