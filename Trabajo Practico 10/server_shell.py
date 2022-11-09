import socketserver, subprocess, sys, getopt

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

class Process(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class Thread(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        print ("Conexion establecida")
        while True:
            data = self.request.recv(1024)
            if not data:
             break
            print ("Comando recibido: " + data.decode())
            proc = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            self.request.send(stdout_value)
        print ("Conexion terminada")

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    if args == "p":
        server = Process((host, port), Handler)
        print ("Servidor con procesos (Port= {port})".format(port=port))
    elif args == "t":
        server = Thread((host, port), Handler)
        print ("Servidor con hilos (Port= {port})".format(port=port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print ("Servidor detenido")
        sys.exit(0)

