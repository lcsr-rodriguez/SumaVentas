# suma.py
# Python 3.8.5
# Suma de precios

from functools import reduce
import json
import os

# Retorna el JSON de una ruta
def get_data(ruta):
    with open(ruta) as contenido:
        objeto = json.load(contenido)
        
    return objeto;

# Genera un .txt (storage) con la suma de ventas por departamento
def ventas_departamento(data, storage):
    # suma el campo "price" en los elementos por "department"
    total = {}
    for elemento in data:
        total[elemento['department']] = total.get(elemento['department'], 0) + elemento['price']

    # guarda el archivo en el directorio storage
    with open(storage + 'VENTAS_DEPARTAMENTO.json', 'w') as json_file:
        json.dump(total, json_file)

# main
if __name__ == '__main__':
    base = 'D:/Universidad/electiva_profesional/SumaVentas/'
    storage = base + 'storage/'
    file = 'random_commerce1.json' # archivo
    ruta = os.path.join(base, file)
    data = get_data(ruta)
    # Por departamento
    ventas_departamento(data, storage)
