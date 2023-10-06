Клонируем репозиторий

устанавливаем виртуальное окружение 
python -m venv venv

запускаем Виртуальнео окружение
venv\Scripts\activate.bat

Устанавливаем библиотеки
pip install -r requirements.txt


Создаем базу данных в PgAdmin с именем <shop_internet>

создаем файл .pgpass
чтобы указать в нем пароль от Postgres вконце
localhost:5432:shop_internet:postgres:<password>

Загрузить бузу данных из afqlf fill