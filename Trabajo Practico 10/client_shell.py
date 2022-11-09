import socket, getopt, sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "p:")
    if len(opts) != 3:
        print ("no ha ingresado la cantidad de argumentos correcta")
        sys.exit(2)
except getopt.GetoptError: 
    print ("Error en los parametros")
    sys.exit(2)

for (op, ar) in opts:
    if op == "-p":
        port = int(ar)
    if op == "-h":
        host = str(ar)
    if op == "-a":
        args = str(ar)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Ingrese el comando: ")
    s.send(command.encode())
    if command == "exit":
        break
    result = s.recv(1024)
    print (result.decode())

s.close()

