from opcua import Client
import time
import db
import asyncio
import websockets

def alarmForTemperature(timeValue, temp, pId):
    descr = ""
    if temp >= 40:
        descr = "High High"

    if temp<40 and temp>=30:
        descr = "High"

    if temp<30 and temp>=20:
        descr = "Low"

    if temp<20 and temp>=10:
        descr = "Low Low"
        
    db.alarmDataToDb(alarmId=1, timeStamp=timeValue, description=descr, processId=pId)


# async def sendData(websocket):
#     await websocket.send()


url = "opc.tcp://10.10.32.60:4840"
client = Client(url)
client.connect()
print("Client Connected")

pNum = 0
while True:
    TIME = client.get_node("ns=2;i=4")
    TIMEValue = TIME.get_value()

    TEMPERATURE = client.get_node("ns=2;i=2")
    Temp = TEMPERATURE.get_value()

    PRESSURE = client.get_node("ns=2;i=3")
    Press = PRESSURE.get_value()

    HUMIDITY = client.get_node("ns=2;i=5")
    Hum = HUMIDITY.get_value()

    pNum += 1
    db.sensorDataToDb(timeStamp=TIMEValue, temp=Temp, press=Press, humi=Hum, sensorId=1, processId=pNum)
    alarmForTemperature(TIMEValue, Temp, pNum)
    time.sleep(4)


