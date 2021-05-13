# suma.py
# Python 3.8.5
# Suma de precios

import json
import os

# Retorna el JSON de una ruta
def get_data(ruta):
    with open(ruta) as contenido:
        objeto = json.load(contenido)
        
    return objeto;
# -------------------------------------------------------------------------------------
# Genera un .txt (storage) con la suma de ventas por departamento
def ventas_departamento(data, storage):
    # suma el campo "price" en los elementos por "department"
    total = {}
    for elemento in data:
        total[elemento['department']] = total.get(elemento['department'], 0) + elemento['price']

    # guarda el archivo en el directorio storage
    with open(storage + 'VENTAS_DEPARTAMENTO.json', 'w') as json_file:
        json.dump(total, json_file)
# -------------------------------------------------------------------------------------
# Genera un .txt (storage) con la suma de ventas por material
def ventas_material(data, storage):
    # suma el campo "price" en los elementos por "material"
    total = {}
    for elemento in data:
        total[elemento['material']] = total.get(elemento['material'], 0) + elemento['price']

    # guarda el archivo en el directorio storage
    with open(storage + 'VENTAS_MATERIAL.json', 'w') as json_file:
        json.dump(total, json_file)
# -------------------------------------------------------------------------------------
# Genera un .txt (storage) con la suma de ventas por color
def ventas_color(data, storage):
    # suma el campo "price" en los elementos por "color"
    total = {}
    for elemento in data:
        total[elemento['color']] = total.get(elemento['color'], 0) + elemento['price']

    # guarda el archivo en el directorio storage
    with open(storage + 'VENTAS_COLOR.json', 'w') as json_file:
        json.dump(total, json_file)
# -------------------------------------------------------------------------------------
# Genera un .txt (storage) con la suma de ventas por categoria
# Nota : La categoria es la ultima palabra del campo "product_name"
def ventas_categoria(data, storage):
    # suma el campo "price" en los elementos por "categoria"
    total = {}
    for elemento in data:
        total[str(elemento['product_name']).split()[-1]] = total.get(str(elemento['product_name']).split()[-1], 0) + elemento['price']

    # guarda el archivo en el directorio storage
    with open(storage + 'VENTAS_CATEGORIA.json', 'w') as json_file:
        json.dump(total, json_file)
# -------------------------------------------------------------------------------------

# main
if __name__ == '__main__':
    base = 'D:/Universidad/electiva_profesional/SumaVentas/'
    storage = base + 'storage/'
    file = 'random_commerce1.json' # archivo
    ruta = os.path.join(base, file)
    data = get_data(ruta)
    # Por departamento
    #ventas_departamento(data, storage)
    ventas_categoria(data, storage)
    #ventas_material(data, storage)
    #ventas_color(data, storage)
