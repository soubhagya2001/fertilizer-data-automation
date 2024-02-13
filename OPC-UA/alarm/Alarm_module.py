#The code for the level of alarm for the whole tank is processed here.
#Divided into 4 levels of
something = 0
import db

def alarm(sensor_val):
    if sensor_val <= 25:
        db.sensor_value_db(sensor_val)
        print("The Stage of alarm is Low-Low")
    elif sensor_val <= 50 and sensor_val > 25:
        db.sensor_value_db(sensor_val)
        print("the Stage of alarm is Low")
    elif sensor_val <= 75 and sensor_val > 50:
        db.sensor_value_db(sensor_val)
        print("The stage of alarm is High")
    else:
        db.sensor_value_db(sensor_val)
        print("The stage of alarm is High-High")

    if sensor_val == 1:
        db.alarm_db(sensor_val,"Low-Low")
    elif sensor_val == 25:
        something = 0
        db.alarm_db(sensor_val,"Low")
    elif sensor_val == 50:
        something = 0
        db.alarm_db(sensor_val, "High")
    elif sensor_val == 75:
        something = 0
        db.alarm_db(sensor_val,"Higi-High")