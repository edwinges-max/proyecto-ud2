import sys
import csv

entrada = sys.argv[1]
salida = sys.argv[2]

with open(entrada, "r") as f:
    lineas = f.readlines()

with open(salida, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["linea"])
    for linea in lineas:
        writer.writerow([linea.strip()])