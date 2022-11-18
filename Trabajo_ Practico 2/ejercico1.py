
import sys, getopt, subprocess, datetime

try:
    opt, arg = getopt.getopt(sys.argv[1:], 'h', ['help'])
    if len(opt) != 3:
        raise getopt.GetoptError('Error en la cantidad de parametros')
except getopt.GetoptError as err:
    print(err)
    print('Uso: python3 ejercicio1.py -h')
    sys.exit(2)

command = '  '
output_file = '  '
log_file = '  '

for (op, ar) in opt:
    if op in ('-h', '--help'):
        print('Uso: python3 ejercicio1.py -c "comando" -o "archivo de salida" -l "archivo de log"')
        sys.exit(0)
    elif op == '-c':
        command = ar
    elif op == '-o':
        output_file = ar
    elif op == '-l':
        log_file = ar

if command == '  ' or output_file == '  ' or log_file == '  ': 
    print('Faltan parametros')
    sys.exit(2)

try:
    with open(output_file, 'w') as file:
        subprocess.call(command, shell=True, stdout=file)
except FileNotFoundError as err:
    print(err)
    sys.exit(2)

try:
    with open(log_file, 'a') as file:
        file.write('Fecha y hora: ' + str(datetime.datetime.now()) + ' - Comando ejecutado: ' + command + ' - Archivo de salida: ' + output_file + ' - Archivo de log: ' + log_file + ' - Resultado: OK \r \n')
except FileNotFoundError as err:
    print(err)
    sys.exit(2)

print('OK')


