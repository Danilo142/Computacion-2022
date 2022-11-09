import getopt, sys, os, time 

try:
    opt, arg = getopt.getopt(sys.argv[1:], 'h', ['help'])
    if len(opt) != 3:
        raise getopt.GetoptError('Error en la cantidad de parametros')
except getopt.GetoptError as err:
    print(err)
    print('Uso: python3 fork.py -h')
    sys.exit(2)

modo_verboso = False

for (op,ar) in opt:
    if op == '-n':
        n = int(ar)
    elif op == '-m':
        m = int(ar)
     
    elif op == '-v':
        modo_verboso = True



if modo_verboso:
    print('Modo verboso activado')



pid = os.fork()

if pid == 0:
    print('Soy el proceso hijo')
    time.sleep(5)
    print('Termino el proceso hijo')
else:
    print('Soy el proceso padre')
    time.sleep(10)
    print('Termino el proceso padre')

def escribir_archivo(name: str):
    fd =open(name, 'w')
    return fd

def leer_archivo(name: str):
    fd = open(name, 'r')
    return fd

if __name__ == '__main__':
    fd = escribir_archivo('archivo.txt')
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print('Soy el proceso hijo', os.getpid())
            fd.write(str(os.getpid()) + ' ')
            time.sleep(5)
            print('Termino el proceso hijo', os.getpid())
            sys.exit(0)
        else:
            print('Soy el proceso padre', os.getpid())
            time.sleep(10)
            print('Termino el proceso padre', os.getpid())
            fd.close()
            fd = leer_archivo('archivo.txt')
            print(fd.read())
            fd.close()

        