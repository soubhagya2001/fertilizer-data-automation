# to install mysqlclient

# Assume you are activating Python 3 venv
# brew install mysql pkg-config
# pip install mysqlclient
#pip install --upgrade mysql-connector-python



import mysql.connector

Db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "rootroot")
cursorObject= Db.cursor()

cursorObject.execute("create DATABASE if not exists Fertiliser_automation;")
cursorObject.execute("use Fertiliser_automation;")

table_create_fertiliser_alarm = """CREATE TABLE IF NOT EXISTS fertiliser_alarm(
                Timestamp Timestamp default CURRENT_TIMESTAMP,
                Sensor_id int,
                measurement int,
                alarm_level VARCHAR(20));"""

cursorObject.execute(table_create_fertiliser_alarm)

table_create_fertiliser_level = """CREATE TABLE IF NOT EXISTS fertiliser_level(
                Timestamp Timestamp default CURRENT_TIMESTAMP,
                Sensor_id int,
                measurement int
                );"""
cursorObject.execute(table_create_fertiliser_level)
#Alarm timestamp is stored i=by this function
def alarm_db(sensor_val,alarm_lvl ):
    insert_sql = ("insert into fertiliser_alarm(sensor_id, measurement, alarm_level) VALUES(1,%s, %s);")
    insert_value = (sensor_val,alarm_lvl)
    cursorObject.execute(insert_sql,insert_value)
    Db.commit()
    print("Alarm inserted in DB")

#continous sensor valus is stored by this function
def sensor_value_db(sensor_val):
    insert_sql = ("Insert into fertiliser_level(sensor_id, measurement) values (%s,%s)")
    insert_value = (1, sensor_val)
    cursorObject.execute(insert_sql,insert_value)
    Db.commit()
    print("Sensor value inserted in DB")