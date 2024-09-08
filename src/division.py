def evaluar(dividendo, divisor):
    # Verificar si el divisor es 0 antes de realizar la operación
    if divisor == 0:
        return "Operación inválida"
    
    # Calcular cociente y residuo
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    
    if residuo == 0:
        respuestaexa = "La división es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
        return respuestaexa
    
    else:    
        respuestanoexa = "La división no es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
        return respuestanoexa

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
