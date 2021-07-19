from Client import UDPClient, TCPClient

"""
def main():
    client = TCPClient("127.0.0.1")
    while True:
        value = input("value:")
        if value == "q":
            break
        client.connect()
        client.send("Eye", value)
        client.disconnect()
"""

def main():
    client = UDPClient("127.0.0.1")
    while True:
        value = input("value:")
        client.send("Eye", value)

if __name__ == "__main__":
    main()
