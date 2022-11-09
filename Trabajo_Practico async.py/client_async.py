import getopt, socket, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "p:", ["port="])
    if len(opts) != 1:
        print ("no ha ingresado la cantidad de argumentos correcta")
        sys.exit(2)
except getopt.GetoptError as err:
    print("Error en los parametros")
    sys.exit(2)

for (op, ar) in opts:
    if op in ("-p", "--port"):
        port = int(ar)
    if op in ("-h", "--host"):
        host = str(ar)

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, data):
        self.socket.send(data.encode())

    def receive(self):
        data = self.socket.recv(1024)
        return data.decode()

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    client = Client("localhost", port)
    print ("Conexion establecida")
    while True:
        command = input("Ingrese el comando: ")
        if command == "exit":
            client.close()
            break
        client.send(command)
        print (client.receive())
    print ("Conexion terminada")

