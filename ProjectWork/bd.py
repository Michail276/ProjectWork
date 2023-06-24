import mysql.connector
from config import read_config
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Qwerty535",
  database="Project_Data_Base"
)
def view_logs(fil_ip=None, fil_start_date=None, fil_end_date=None):
    cursor = db.cursor()
    sql = "SELECT * FROM access_logs"
    conditions = []
    if fil_ip:
        conditions.append("ip = %s")
    if fil_start_date:
        conditions.append("date >= %s")
    if fil_end_date:
        conditions.append("date <= %s")
    if conditions:
        sql += " WHERE " + " AND ".join(conditions)
    values = []
    if fil_ip:
        values.append(fil_ip)
    if fil_start_date:
        values.append(fil_start_date)
    if fil_end_date:
        values.append(fil_end_date)
    cursor.execute(sql, tuple(values))
    result = cursor.fetchall()
    for row in result:
        print(row)
view_logs(fil_ip='127.0.0.1')
view_logs(fil_start_date='2023-01-01', fil_end_date='2023-12-31')
view_logs(fil_ip='127.0.0.1', fil_start_date='2023-01-01', fil_end_date='2023-12-31')
log_path, log_file_mask = read_config('config.ini')
db.close()
