
from celery import Celery
from tareas import potencia, raiz, logaritmo
import getopt, sys

try:
    opt,arg = getopt.getopt(sys.argv[1:],"n:")
except getopt.GetoptError:
    print("Error en los parametros")

app = Celery('celery_app', broker='amqp://guest@localhost//')

for (op,ar) in opt:
    if op == '-n':
        n = str(ar)
    if op == '-m':
        m = str(ar)

def matriz(n,m):
    matriz = [[0 for x in range(n)] for y in range(m)]
    return matriz

def llenar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(input("Ingrese el valor de la posicion "+str(i)+","+str(j)+": "))
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j],end=" ")
        print("")

def calcular_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 0:
                matriz[i][j] = potencia(matriz[i][j])
            elif matriz[i][j] < 0:
                matriz[i][j] = raiz(matriz[i][j])
            else:
                matriz[i][j] = logaritmo(matriz[i][j])
    return matriz

def main():
    matriz = matriz(n,m)
    matriz = llenar_matriz(matriz)
    matriz = calcular_matriz(matriz)
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()



