from fastapi import FastAPI, WebSocket
import db
import asyncio

app = FastAPI()

# Establish connection to OPC UA server
from opcua import Client
client = Client("opc.tcp://10.58.13.221:4840")
client.connect()
print("Client Connected")


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




async def websocket_sender(websocket: WebSocket):
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
        # Store data in the database
        db.sensorDataToDb(timeStamp=TIMEValue, temp=Temp, press=Press, humi=Hum, sensorId=1,processId=pNum)

        # Check temperature and raise alarm
        alarmForTemperature(TIMEValue, Temp, pNum)

        # Prepare data to send through WebSocket
        data = {
            "timeStamp": TIMEValue,
            "temperature": Temp,
            "pressure": Press,
            "humidity": Hum,
            "sensorId": 1,
            "processId": pNum
        }

        # Send data through WebSocket
        await websocket.send_json(data)
        await asyncio.sleep(4)

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket_sender(websocket)
