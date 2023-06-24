from flask import Flask, jsonify, request
import mysql.connector
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Qwerty535",
  database="Project_Data_Base"
)
app = Flask(__name__)
@app.route('/logs', methods=['GET'])
def get_logs():
    cursor = db.cursor()
    sql = "SELECT * FROM access_logs"
    conditions = []
    fil_ip = request.args.get('ip')
    fil_start_date = request.args.get('start_date')
    fil_end_date = request.args.get('end_date')
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
    logs = []
    for row in result:
        log = {
            'id': row[0],
            'ip': row[1],
            'date': row[2].strftime("%Y-%m-%d %H:%M:%S")
        }
        logs.append(log)
    return jsonify(logs)
if __name__ == '__main__':
    app.run()
db.close()
