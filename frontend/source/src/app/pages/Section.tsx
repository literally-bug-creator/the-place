import { useParams } from 'react-router-dom'

export default function Section() {
  const { sectionId } = useParams<{ sectionId: string }>()
  
  const titles: { [key: string]: string } = {
    gi: 'Гражданские инициативы (Г.И.)',
    sm: 'Советы мэру (С.М.)',
    as: 'Архитектурная справка (А.С.)',
    chp: 'Что поделать? (Ч.П.)',
  }

  return (
    <div className="page-container">
      <h1>{titles[sectionId || ''] || 'Раздел'}</h1>
      <p>Здесь публикуются посты раздела {titles[sectionId || ''] || sectionId}.</p>
    </div>
  )
}