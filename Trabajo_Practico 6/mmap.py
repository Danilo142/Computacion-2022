
import getopt, sys, os, mmap, signal

try:
    opts, args = getopt.getopt(sys.argv[1:], "f:")
    if len(opts) != 1:
        print ("no ha ingresado la cantidad de argumentos correcta")
        sys.exit(2)
except getopt.GetoptError:
    print ("Error en los parametros")
    sys.exit(2)

for (op, ar) in opts:
    if op == "-f":
        path = str(ar)

memoria = mmap.mmap(-1, 100)

def handler_padre(signum, frame):
    global continuar
    if signum == signal.SIGUSR1:
        print ("Padre: recibido SIGUSR1")
        memoria.seek(0)
        print ("Padre: recibido: " + memoria.readline())

    if signum == signal.SIGUSR2:
        print ("Padre: recibido SIGUSR2")
        sys.exit(0)

def handler_hijo(signum, frame):
    global continuar
    if signum == signal.SIGUSR1:
        print ("Hijo: recibido SIGUSR1")
 
        sys.exit(0)
    if signum == signal.SIGUSR2:
        print ("Hijo: recibido SIGUSR2")

        sys.exit(0)

pidh1 = os.fork()
if pidh1 == 0:
    print(f'Hijo 1: PID {os.getpid()}')
    for linea in sys.stdin:
        if linea == 'bye\n':
            print('Hijo 1: recibido: ' + linea) 
          
            memoria.write(linea.encode())
        else:
            print('Hijo 1: recibido: ' + linea) 
            memoria.write(linea.encode() + b' ')
            
pidh2 = os.fork()
if pidh2 == 0:
    print(f'Hijo 2: PID {os.getpid()}')
    for linea in sys.stdin:
        if linea == 'bye\n':
            print('Hijo 2: recibido: ' + linea) 
            memoria.write(linea.encode())
        else:
            print('Hijo 2: recibido: ' + linea) 
         
            memoria.write(linea.encode() + b' ')

continuar = True
print(f'Padre: PID {os.getpid()}')
signal.signal(signal.SIGUSR1, handler_padre)
signal.signal(signal.SIGUSR2, handler_padre)
while continuar:
    signal.pause()
else:
    for i in range(2):
        os.wait()
    print(f'Padre: terminado')



