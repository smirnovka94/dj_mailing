# Cервис Рассылок
Интерфейс системы содержит следующие экраны: 
список рассылок, 
отчет проведенных рассылок отдельно, 
создание рассылки, удаление рассылки,
создание пользователя, удаление пользователя, 
редактирование пользователя

## Установка и использование
Клонируем репозиторий

Устанавливаем виртуальное окружение 
```
python -m venv env
```
Запускаем Виртуальнео окружение
```
venv\Scripts\activate.bat
```
Устанавливаем библиотеки
```
pip install -r requirements.txt
```

Создаем базу данных в PgAdmin с именем <mailing>
Создаем файл<.env>
.env.template переименовать на .env

Загрузить базу данных
```
python manage.py loaddata b_data.json
python manage.py loaddata c_data.json
python manage.py loaddata m_data.json
python manage.py loaddata u_data.json
```
Создаем superuser
login: kirill@sky.pro
password: qwerty88
```
python manage.py super_user
```
Запускаем планировщик задач
```
python manage.py runapscheduler 
```

# Ход работы 

При регистрации если у пользователя почта оканчивается почта на sky.pro он получает права менеджера
в противном случае - права пользователя
