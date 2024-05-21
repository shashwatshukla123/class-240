import socket
from threading import Thread

IP_address='127.0.0.1'
PORT=8080
SERVER=None
BUFFER_SIZE=4096

def setup():
        global PORT
        global IP_address
        global SERVER
        SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        SERVER.connect((IP_address,PORT))

setup()