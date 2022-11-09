import getopt, sys, multiprocessing
from math import sqrt, log10
from functools import partial

try:
    opts, args = getopt.getopt(sys.argv[1:], "f:")
    if len(opts) != 3:
        print ("no ha ingresado la cantidad de argumentos correcta")
        sys.exit(2)
except getopt.GetoptError:
    print ("Error en los parametros")
    sys.exit(2)

for (op, ar) in opts:
    if op == "-p":
        num_procesos = int(ar)
    if op == "-f":
        path = str(ar)
    if op == "-c":
        calculo = str(ar)

def leer_matriz(path):
    with open(path, 'r') as f:
        lineas = f.readlines()
        n = int(lineas[0])
        matriz = []
        for i in range(1, n+1):
            fila = lineas[i].split()
            matriz.append(fila)
        return matriz

def calcular(matriz, calculo):
    matriz_nueva: list = []
    if calculo == "log10":
        for fila in matriz:
            fila_nueva = []
            for elemento in fila:
                fila_nueva.append(log10(float(elemento)))
            matriz_nueva.append(fila_nueva)
    elif calculo == "sqrt":
        for fila in matriz:
            fila_nueva = []
            for elemento in fila:
                fila_nueva.append(sqrt(float(elemento)))
            matriz_nueva.append(fila_nueva)
    return matriz_nueva

def escribir_matriz(matriz, path):
    with open(path, 'w') as f:
        for fila in matriz:
            f.write(' '.join(fila))
            f.write(' ')

def main() -> None:
    pool = multiprocessing.Pool()
    resultado = pool.map(partial(calcular, calculo=calculo), leer_matriz(path))
    escribir_matriz(resultado, path)
    print(resultado[0])


if __name__ == '__main__':
    main()


        