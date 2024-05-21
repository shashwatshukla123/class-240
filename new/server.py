import socket
from threading import Thread

IP_address='127.0.0.1'
PORT=8080
SERVER=None
client={}
def acceptConnections():
    global SERVER
    global clients
    while True:
        client, address=SERVER.accept()
        print(client)

def setup():
        global PORT
        global IP_address
        global SERVER
        SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        SERVER.bind((IP_address,PORT))
        SERVER.listen(100)
        print("SERVER is waiting for connection")
        acceptConnections()

setup_thread=Thread(target=setup)
setup_thread.start()