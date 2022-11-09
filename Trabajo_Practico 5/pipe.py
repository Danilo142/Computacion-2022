import getopt, sys, os

try:
    opts, args = getopt.getopt(sys.argv[1:], "i:o:")
except getopt.GetoptError:
    print ("Error en los parametros")
    sys.exit(2)

for (op, ar) in opts:
    if op == "-i":
        input_file = ar
    elif op == "-o":
        output_file = ar

def read_file(name: str):
    fd = open(name, 'r')
    return fd.readlines()

def write_file(name: str):
    fd = open(name, 'w')
    return fd

lines_recieved = []
def cerate_son(line):
    if not os.fork():
        os.write(1, line.encode())
        os._exit(0)
    else:
        value = os.read(0, 100)
        lines_recieved.append(value.decode())
    
def main():
    lines = read_file(input_file)
    for line in lines:
        cerate_son(line)
    fd = write_file(output_file)
    for line in lines_recieved:
        fd.write(line)
    fd.close()

if __name__ == "__main__":
    main()

