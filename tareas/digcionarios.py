iccionario = {
    "cocina": 'plato',
    'baño': 'ducha',
    'cuarto':'cama',
    "numero":"567491"}

def menKey(key, diccion):
    if key not in diccion:
        return f" {key} no existe en el diccionario"
    else:
        s = diccion[key]
        t = type(s)
        if t is str:
            t = "Cadena"
        elif t is int:
            t = "Entero"
        else:
            t = "Flotante"
        return f"El valor de {key} es: {s} y es de tipo de dato es: {t}"
    
print(menKey(input("Escriba la parte de la casa: "), diccion))