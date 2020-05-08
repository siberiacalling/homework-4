###Тестирование проекта https://e.mail.ru/addressbook

###Запуск тестов

Необходимо изменить путь к драйверам(убунту или мак) в файле `./node.sh`

`./grid.sh`

`./node.sh`

`python3 run_tests.py`

###Чек-лист [@siberiacalling](https://github.com/siberiacalling)
<p>1. Редактирование контакта</p>
	<p>&emsp;&emsp;а) Попытка перехода к редактированию из списка контактов</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; при не выбранном ни одном контакте</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; при выбранных двух контактах</p>
	<p>&emsp;&emsp;b) Успешное редактирование с вводом новой информации:</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; из карточки контакта</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; из списка контактов при выбранном одном контакте</p>
	<p>&emsp;&emsp;c) Попытка удалить всю информацию и сохранить пустой контакт</p>
	<p>&emsp;&emsp;d) Попытка добавления нового e-mail с неверным форматом</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; символы кириллицей</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; без формата почты (без строки вида «@(a-z).(a-z)»</p>
	<p>&emsp;&emsp;e) Добавление еще одного поля через кнопку напротив поля</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; e-mail</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Мобильный</p>
	<p>&emsp;&emsp;f) Добавление еще одного поля через кнопку «Добавить поле» внизу формы</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; e-mail</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Телефон</p>
	<p>&emsp;&emsp;g) Добавление поля через кнопку «Добавить поле» с проверкой, что оно больше не отображается в выпадающем списке</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Псевдоним</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Должность</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Руководитель</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Пол</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Адрес</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Соц. Сети и мессенджеры</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; День рождения</p>
	<p>&emsp;&emsp;h) Удаление дополнительного поля:</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; E-mail</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Телефон</p>
	<p>&emsp;&emsp;i) Удаление дополнительного поля с проверкой, что оно снова отображается в выпадающем списке:</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Псевдоним</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Должность</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Руководитель</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Пол</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Адрес</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Соц. Сети и мессенджеры</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; День рождения</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Отмена редактирования</p>
<p>2. Написать письмо</p>
	<p>&emsp;&emsp;а) Успешный редирект на форму письма из списка контактов:</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Одного контакта</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Двух контактов</p>
	<p>&emsp;&emsp;b) Попытка написать (кнопка «Написать») при не выбранном ни одном контакте </p>
<p>3. Переходы и пагинация</p>
	<p>&emsp;&emsp;а) Переход в список моих контактов из карточки контакта этой группы</p>
	<p>&emsp;&emsp;b) Отсутствие возможности перехода в «мои контакты» из карточки контакта не из этой группы</p>
	<p>&emsp;&emsp;c) Переход в список пользовательской группы из карточки контакта этой группы</p>
	<p>&emsp;&emsp;d) Отсутствие возможности перехода в пользовательскую группу из карточки контакта не из этой группы</p>
	<p>&emsp;&emsp;e) Переключение контактов кнопками  на карточке контактов:</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Вперед</p>
	<p>&emsp;&emsp;&emsp;&emsp;&bull; Назад</p>
