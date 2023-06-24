1. Создайте пустую базу данных в MySQL.

2. Запустите базу данных при помощи команд: "create database Project_Data_Base;" и "use Project_Data_Base;".

3. В файлах API.py, bd.py, config.ini и main.py вставьте данные о своей базе данных в host, user, password и database.
Пример:
host="127.0.0.1",
user="root",
password="Qwerty535",
database="Project_Data_Base"

4. Вставьте пути до файла access в файлах main.py и config.ini в "log_file", а также путь до папки ProjectWork в файле config.ini в "log_path"
Пример: 
log_file = C:/Users/Lenovo LEGION 5-17/OneDrive/Документы/ProjectWork/access.log
log_path = C:/Users/Lenovo LEGION 5-17/OneDrive/Документы/ProjectWork/

5. Запустите файл main.py

6. После того как он прогрузится полностью, перейдите в MySQL и обновите вашу базу данных, после чего введите команду "select * from access_logs" чтобы просмотреть таблицу.

7. Теперь запустите файл API.py.

8. У вас должна появиться ссылка.
Пример:
http://127.0.0.1:5000

9. Скопируйте её и вставьте в браузер (у вас должна вывестись ошибка "Not Found").

10. Добавьте к ссылке "/logs".
Пример: 
http://127.0.0.1:5000/logs

11. После этого у вса должны появиться все логи из файла "access.log".

12. Скопируйте ссылку из пункта 10 и добавьте в неё "?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD"
Пример:
http://localhost:5000/logs?start_date=2001-01-01&end_date=2023-12-31

13. После этого у вас должны появиться логи, по отсортированные по указанным датам.

14. Скопируйте ссылку из пункта 10 и добавьте в неё "?ip=000.000.000.000"
Пример:
http://localhost:5000/logs?ip=89.107.177.18

15. После этого у вас должны появиться только те логи, у которых есть данный ip
