from opcua import Server
from random import randint
import datetime
import time

server = Server()

url = "opc.tcp://10.10.32.65:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace,"Parameters")

Temp = Param.add_variable(addspace,"Temperature",0)
Press = Param.add_variable(addspace,"Pressure",0)
Time = Param.add_variable(addspace,"Time",0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print("Server started at {}".format(url))

print(f"Temperature Node Address : {Temp},\nPressure Node Address : {Press},\nTime Node Address : {Time}")

while True:
    Temperature = randint(10,50)
    Pressure = randint(200,999)
    TIME = datetime.datetime.now()

    print(f"Temperature : {Temperature}\nPressure : {Pressure}\nTime : {TIME}\n")    

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(2)
     