import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="",database="fertilizer")

if connection.is_connected():
    print("Connected successfully")
    mycursor = connection.cursor()

    # mycursor.execute("create DATABASE if not exists fertiliser;")
    # mycursor.execute("use fertiliser")

else:
    print("Failed to connect")


def sensorDataToDb(timeStamp, temp, press, humi, sensorId, processId):
    mycursor.execute("USE fertilizer")
    insert_sql = "INSERT INTO sensorsData (timestamp, temp, press, humi, sensorId, processId) VALUES (%s, %s, %s, %s, %s, %s)"
    insert_value = (timeStamp, temp, press, humi, sensorId, processId)
    mycursor.execute(insert_sql, insert_value)
    connection.commit()
    print("Sensor value inserted in database")


def alarmDataToDb(alarmId, timeStamp, description, processId):
    mycursor.execute("USE fertilizer")
    insert_sql = ("Insert into alarmData(alarmId,timestamp,description,processId) values (%s,%s,%s,%s)")
    insert_value = (alarmId, timeStamp, description, processId)
    mycursor.execute(insert_sql, insert_value)
    connection.commit()
    print("Alarm data value inserted in database")
