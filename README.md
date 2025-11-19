# VolgaIT_QA_Final
<h2>Замечания</h2>
<ul>
  <li>Сайт не выполняет метод проверки совпадаемости паролей!</li>
</ul>
<h2>Положительный тест-кейс №1</h2>
<h3>Заполнение всех требующихся полей формы - Тест 1</h3>
<strong>Предусловия:</strong> Открыта страница (https://way2automation.com/way2auto_jquery/registration.php#load_box)</br>
<strong>Шаги</strong>
<ul>
  <li>Заполнить поле "First Name"</li>
  <li>Заполнить поле "Last Name"</li>
  <li>Нажать на все ячейки Hobby</li>
  <li>Заполнить поле "Phone Number"</li>
  <li>Заполнить поле "Username"</li>
  <li>Заполнить поле "E-mail"</li>
  <li>Заполнить поле "Password"</li>
  <li>Заполнить поле "Confirm Password"</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Переход на тот же сайт, где поля уже пустые"

<h2>Положительный тест-кейс №2</h2>
<h3>Заполнение всех полей - Тест 2</h3>
<strong>Предусловия:</strong> Открыта страница (https://way2automation.com/way2auto_jquery/registration.php#load_box)</br>
Готовые данные, где у каждого выбраны разные RadioBox</br>
<strong>Шаги</strong>
<ul>
  <li>Заполнить поле "First Name"</li>
  <li>Заполнить поле "Last Name"</li>
  <li>Выбран один из "RadioBox"</li>
  <li>Нажать на все ячейки Hobby</li>
  <li>Выбрана страна "India"</li>
  <li>Выбран месяц "1"</li>
  <li>Выбран день "1"</li>
  <li>Выбран год "2014"</li>
  <li>Заполнить поле "Phone Number"</li>
  <li>Заполнить поле "Username"</li>
  <li>Заполнить поле "E-mail"</li>
  <li>Вставка фотографии в "Your Profile Picture"</li>
  <li>Заполнение поле ответами по задачам 1-3 в поле "About Yourself"</li>
  <li>Заполнить поле "Password"</li>
  <li>Заполнить поле "Confirm Password"</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Переход на тот же сайт, где поля уже пустые"

<h2>Негативный тест-кейс №1</h2>
<h3>Заполнение не всех требующихся полей - Тест 3</h3>
<strong>Предусловия:</strong> Открыта страница (https://practice-automation.com/popups/)</br>
<strong>Шаги</strong>
<ul>
  <li>Заполнить поле "Last Name"</li>
  <li>Нажать на все ячейки Hobby</li>
  <li>Заполнить поле "Phone Number"</li>
  <li>Заполнить поле "Username"</li>
  <li>Заполнить поле "E-mail"</li>
  <li>Заполнить поле "Password"</li>
  <li>Заполнить поле "Confirm Password"</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Появление красного текста "This field is required." ниже поле "First Name"

<h2>Негативный тест-кейс №2</h2>
<h3>Заполнение всех требующихся полей с невалидной почтой - Тест 4</h3>
<strong>Предусловия:</strong> Открыта страница (https://practice-automation.com/popups/)</br>
<strong>Шаги</strong>
<ul>
  <li>Заполнить поле "First Name"</li>
  <li>Заполнить поле "Last Name"</li>
  <li>Нажать на все ячейки Hobby</li>
  <li>Заполнить поле "Phone Number"</li>
  <li>Заполнить поле "Username"</li>
  <li>Заполнить поле "E-mail"</li>
  <li>Заполнить поле "Password"</li>
  <li>Заполнить поле "Confirm Password"</li>
  <li>Нажать на кнопку "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Появление красного текста "Please enter a valid email address." ниже поле "E-mail"

<h2>Негативный тест-кейс №3</h2>
<h3>Потдверждение регистрации без заполнения полей - Тест 5</h3>
<strong>Предусловия:</strong> Открыта страница (https://practice-automation.com/popups/)</br>
<strong>Шаги</strong>
<ul>
  <li>Нажатие кнопки "Submit"</li>
</ul>
<strong>Ожидаемый результат</strong> - Появление 7 красных текстов "This field is required."

<h2>Отчеты на Allure</h2>
<div align="center">
  <strong>ПК не имел возможности выполнять команды <code>allure serve</code> для получения визуального результата</strong>
</div>

<h2>Установка и запуск</h2>
<ol>
    <li>Клонировать репозиторий</li>
    <li>Установить зависимости: <code>pip install -r requirements.txt</code></li>
    <li>Настроить переменные окружения в <code>.venv</code></li>
    <li>Запустить тесты с нужными вам параметрами: <code>pytest -v -s</code> - это выдаст подробное описание тестов и все print</li>
    <li><strong>Запустить параллельные тесты</strong>: <code>pytest -n auto</code></li>
    <li>Если вам нужен конректные тесты (Поиск элементов, Положительные или Негативные тесты), то запускайте так - <code>cd tests</code>, потом <code>pytest *Название файла*</code></li>
    <li>Если вам нужен тест какой-то из тест-кейса (функцию), то запускайте так - <code>pytest tests/*Название файла*::*Название класса*::*Название самого теста (Функция)*</code></li>
    <li>Если сайт из allure-report не открывается, можете локально запустить свой - <code>allure serve results</code></li>
</ol>
