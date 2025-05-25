export default function CreatePost() {
  return (
    <div className="page-container">
      <h1>Создать пост</h1>
      <form>
        <div>
          <label>Заголовок:</label><br />
          <input type="text" name="title" />
        </div>
        <div>
          <label>Содержание:</label><br />
          <textarea name="content" rows={5} />
        </div>
        <div>
          <label>Форматирование:</label>
          <p>Поддержка **жирного**, _курсива_, #заголовков, &gt; цитат и пр.</p>
        </div>
        <div>
          <label>Разделы:</label><br />
          <input type="checkbox" name="sections" value="home" /> Главная<br />
          <input type="checkbox" name="sections" value="gi" /> Г.И.<br />
          <input type="checkbox" name="sections" value="sm" /> С.М.<br />
          <input type="checkbox" name="sections" value="as" /> А.С.<br />
          <input type="checkbox" name="sections" value="chp" /> Ч.П.<br />
        </div>
        <div>
          <label>Медиа (Фото/Видео/Аудио):</label>
          <input type="file" name="media" multiple />
        </div>
        <button type="submit">Опубликовать</button>
      </form>
    </div>
  )
}