import socket
import json

class UDPClient:
    def __init__(self, ip, port=50007):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, axis, angle):
        message = json.dumps({axis:angle})
        self.client.sendto(message.encode('utf-8'), (self.ip, self.port))
