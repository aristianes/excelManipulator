import sys

if len(sys.argv) > 1:
    print("Argumentos passados:")
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("Nenhum argumento foi passado.")
