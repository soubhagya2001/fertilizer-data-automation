from opcua import Client
import time


opc_server_url = "opc.tcp://LAPTOP-1J49HHKT:53530/OPCUA/SimulationServer"

try:
    client = Client(opc_server_url)
    client.connect()

    print("Connected to OPC UA server")

    root_node = client.get_root_node()

    node_id = "ns=3;i=1003"

    while True:
        node_to_read = client.get_node(node_id)

        value = node_to_read.get_value()
        print("Value of the node:", value)

        time.sleep(1)

except Exception as e:
    print("Error:", e)