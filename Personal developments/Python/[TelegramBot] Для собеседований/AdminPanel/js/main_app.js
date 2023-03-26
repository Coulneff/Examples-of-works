// Получаем ссылки на кнопки "Редактировать" и "Удалить"
const editButtons = document.querySelectorAll('td button:first-child');
const deleteButtons = document.querySelectorAll('td button:last-child');

// Функция для обработки нажатий на кнопку "Редактировать"
function handleEditButtonClick(event) {
  const row = event.target.closest('tr'); // Находим ближайшую строку (tr)
  // Далее можно реализовать логику для редактирования данных
}

// Функция для обработки нажатий на кнопку "Удалить"
function handleDeleteButtonClick(event) {
  const row = event.target.closest('tr'); // Находим ближайшую строку (tr)
  row.remove(); // Удаляем строку из таблицы
}

// Добавляем обработчики нажатий на кнопки
editButtons.forEach(button => {
  button.addEventListener('click', handleEditButtonClick);
});

deleteButtons.forEach(button => {
  button.addEventListener('click', handleDeleteButtonClick);
});