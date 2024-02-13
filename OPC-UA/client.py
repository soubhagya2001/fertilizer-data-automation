from opcua import Client
import time
url = "opc.tcp://10.10.32.65:4840"

client = Client(url)
client.connect()
print("Client Connected")

while True:
    TIME = client.get_node("ns=2;i=4")
    TIMEValue = TIME.get_value()
    print(TIMEValue)

    # Pressure = client.get_values("Temperature")
    # print(Pressure)

    TEMPERATURE = client.get_node("ns=2;i=2")
    Temp = TEMPERATURE.get_value()
    print(f"Temperature : {Temp}")
    
    time.sleep(2)