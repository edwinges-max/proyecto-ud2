# proyecto-ud2

## Objetivo
Proyecto reproducible y versionado para demostrar higiene de software en bioinformática.

## Estructura
- datos-raw: datos de entrada
- datos-intermedios: resultados temporales
- resultados: salidas finales
- scripts: código del proyecto
- docs: documentación
- config: configuraciones
- entorno: dependencias

## Entradas
datos-raw/test.txt

## Salidas
resultados/2026-04-08-exp01/salida.csv

## Dependencias
Python 3

## Ejecución
py scripts/procesar_datos.py datos-raw/test.txt resultados/2026-04-08-exp01/salida.csv

## Reproducibilidad
Ejecutar el script con los mismos datos produce el mismo resultado.
