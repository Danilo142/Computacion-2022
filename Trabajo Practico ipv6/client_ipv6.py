
import getopt, socket, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "p:")
    if len(opts) != 3:
        print("la cantidadd de parametros es incorrecta")
except getopt.GetoptError:
    print("error ")
    sys.exit(2)

for (op, ar) in opts:
    if op == "-p":
        port = int(ar)
    if op == "-h":
        host = str(ar)
    if op == "-a":
        args = str(ar)

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Ingrese un comando: ")
    s.send(command.encode())
    if command == "exit":
        break
    data = s.recv(1024)
    print(data.decode())

s.close()

