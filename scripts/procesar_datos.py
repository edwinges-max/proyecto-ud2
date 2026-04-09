import sys
import csv

entrada = sys.argv[1]
salida = sys.argv[2]

with open(entrada) as f:
    lineas = f.readlines()

with open(salida, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID","Valor","Doble"])

    for linea in lineas:
        nombre, valor = linea.strip().split(",")
        valor = int(valor)
        writer.writerow([nombre, valor, valor*2])
