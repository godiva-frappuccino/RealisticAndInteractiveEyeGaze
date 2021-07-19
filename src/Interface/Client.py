import socket
import json

class UDPClient:
    def __init__(self, ip, port=50007):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, axis, angle):
        message = json.dumps({axis:str(angle)})
        self.client.sendto(message.encode('utf-8'), (self.ip, self.port))

    def sendEyeRotation(self, eyeAngle):
        message = json.dumps({"EyeX":round(eyeAngle[0],2), "EyeY":round(eyeAngle[1],2)})
        self.client.sendto(message.encode('utf-8'), (self.ip, self.port))

class TCPClient:
    def __init__(self, ip, port=50007):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client.connect((self.ip, self.port))

    def send(self, axis, angle):
        message = json.dumps({axis:angle})
        self.client.send(message.encode('utf-8'))

    def disconnect(self):
        self.client.close()
