import json
from matplotlib import pyplot
y_client = []
x_client = []
y_server = []
x_server = []
with open("./client.json") as client:
    client_data = json.load(client)
    client_packets = client_data["intervals"]
    for packet in client_packets:
        x_client.append(packet["streams"][0]["end"])
        y_client.append(packet["streams"][0]["bits_per_second"])
with open("./server.json") as server:
    server_data = json.load(server)
    server_packets = server_data["intervals"]
    for packet in server_packets:
        x_server.append(packet["streams"][0]["end"])
        y_server.append(packet["streams"][0]["bits_per_second"])
pyplot.plot(x_client, y_client, marker='o',
            color='b', label='Client')
pyplot.plot(x_server, y_server, marker='o',
            color='g', label='Server')
pyplot.legend(loc='upper right')
pyplot.ylabel("bit per second")
pyplot.xlabel("time")
pyplot.show()
