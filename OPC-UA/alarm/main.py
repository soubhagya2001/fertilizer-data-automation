import time
import Alarm_module

direction = 1
sensor_val = 0
while 1:
    while direction == 1:
        sensor_val += 1
        print(sensor_val)
        Alarm_module.alarm(sensor_val)
        # time.sleep(2)
        if sensor_val == 100:
            direction = -1

    while direction == -1:
        sensor_val -= 1
        print(sensor_val)
        Alarm_module.alarm(sensor_val)
        # time.sleep(2)
        if sensor_val == 0:
            direction = 1

