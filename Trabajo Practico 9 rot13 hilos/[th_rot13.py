import threading , codecs, sys, queue, os

def target_hilo1(w, q):
    sys.stdin = open(0)
    line = sys.stdin.readline()
    os.write(w, line.encode('ascii'))
    line = q.get()
    q.task_done()
    print(f'H1 indent: {threading.current_thread().ident} encriptacion recuperada: ({line[:-1]})')

def target_hilo2(q, r):
    line = os.read(r, 100).decode()
    line = rot13(line)
    q.put(line)
    q.join()

def rot13(line):
    line_rot13 = codecs.encode(line, 'rot_13')
    return line_rot13

def main():
    r, w = os.pipe()
    q = queue.LifoQueue()

    t1 = threading.Thread(target=target_hilo1, args=(w, q))
    t2 = threading.Thread(target=target_hilo2, args=(q, r))

    t1.start()
    t2.start()

    t1.join()   # Espera a que termine el hilo t1
    t2.join()   # Espera a que terminen los hilos

    print('Fin del programa')


   
    
