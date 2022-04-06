import argparse, os
verboso = False


parser = argparse.ArgumentParser(add_help= False)
parser.add_argument("-n","--numero",type = int, help = "cantidad de procesos hijos a crear")
parser.add_argument("-v", "--verboso",action = "store_true",help= "Modo verboso")

argumentos = parser.parse_args()


def hijos():
    if os.fork():
        suma = sum([i for i in range(os.getpid()) if i % 2 == 0])
        if verboso == True:
            print ("comienzo del proceso " f'{os.getpid()}')
            print ("finalizando el proceso " f'{os.getpid()}')
            print ({os.getpid()}, "-", {os.getppid()},":", {suma}) 

        else:
            print ({os.getpid()}, "-", {os.getppid()},":", {suma}) 


try:
    
    if argumentos.verboso:
        verboso = True

    if   argumentos.numero > 0:
        for i in range(argumentos.numero):
            hijos()
except NameError:
    pass