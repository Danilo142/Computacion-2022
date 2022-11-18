
import socketserver, sys , getopt, subprocess, socket

try:
    opts, args = getopt.getopt(sys.argv[1:], "p:")
    if len(opts) != 3:
        print("la cantidadd de parametros es incorrecta")
except getopt.GetoptError:
    print("cantidad de parametros es incorrect")
    sys.exit(2)


for (op, ar) in opts:
    if op == "-p":
        port = int(ar)
    if op == "-h":
        host = str(ar)
    if op == "-a":
        args = str(ar)

class Thread(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Process(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadIPV6(socketserver.ThreadingMixIn, socketserver.TCPServer):
    ip_family = socket.AF_INET6

class ProccesIPV6(socketserver.ForkingMixIn, socketserver.TCPServer):
    ip_type = socket.AF_INET6

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Conexion establecida")
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print("Comando recibido: " + data.decode())
            proc = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            self.request.send(stdout_value)
        print("Conexion terminada")

def server(direction, port):
    socketserver.TCPServer.allow_reuse_address = True
    if direction[0] == socket.AF_INET and args == "t":
        print(" servidor ipv4 con hilos (port= {port})".format(port=port))
        server = Thread((host, port), Handler)
    elif direction[0] == socket.AF_INET and args == "p":
        print(" servidor ipv4 con procesos (port= {port})".format(port=port))
        server = Process((host, port), Handler)
    elif direction[0] == socket.AF_INET6 and args == "t":
        print(" servidor ipv6 con hilos (port= {port})".format(port=port))
        server = ThreadIPV6((host, port), Handler)
    elif direction[0] == socket.AF_INET6 and args == "p":
        print(" servidor ipv6 con procesos (port= {port})".format(port=port))
        server = ProccesIPV6((host, port), Handler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Servidor detenido")
        sys.exit(0)

if __name__ == "__main__":
    if host == "localhost":
        host = " "
    try:
        direction = socket.getaddrinfo(host, port)
        server(direction, port)
    except socket.gaierror:
        print("Direccion invalida")
        sys.exit(2)
    
    


