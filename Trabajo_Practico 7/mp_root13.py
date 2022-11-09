import codecs, multiprocessing, sys, os

def objetivo_1(conn, queue):
    print(f'Hijo 1: PID {os.getpid()}')
    for linea in sys.stdin:
        if linea == 'bye\n':
            print('Hijo 1: recibido: ' + linea) 
            queue.put(linea)
        else:
            print('Hijo 1: recibido: ' + linea) 
            queue.put(linea + ' ')

def objetivo_2(conn, queue):
    print(f'Hijo 2: PID {os.getpid()}')
    for linea in sys.stdin:
        if linea == 'bye\n':
            print('Hijo 2: recibido: ' + linea) 
            queue.put(linea)
        else:
            print('Hijo 2: recibido: ' + linea) 
            queue.put(linea + ' ')

def objetivo_padre(conn, queue):
    print(f'Padre: PID {os.getpid()}')
    while True:
        linea = queue.get()
        if linea == 'bye\n':
            print('Padre: recibido: ' + linea) 
            conn.send(linea)
            break
        else:
            print('Padre: recibido: ' + linea) 
            conn.send(linea + ' ')

if __name__ == '__main__':
    queue = multiprocessing.Queue() # cola de mensajes
    conn1, conn2 = multiprocessing.Pipe() # canal de comunicación
    p1 = multiprocessing.Process(target=objetivo_1, args=(conn1, queue))
    p2 = multiprocessing.Process(target=objetivo_2, args=(conn1, queue))
    p3 = multiprocessing.Process(target=objetivo_padre, args=(conn2, queue))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

