def validar_cuit(cuit):
    digitos="1234567890"
    pos = 0

    if len(cuit) != 13:
        print ("Error! el CUIT tiene la longitud equivocada")
        return False
    if cuit[2] != "-" or cuit[11] != "-":
        print("Error! el CUIT no tiene formato correcto")
        return False

    for caracter in cuit:
        if caracter not in digitos and pos != 2 and pos != 11:
            print("Error! el cuit tiene caracteres invalidos")
            return False
        pos += 1

    return True


def principal():
    print("portal de empleos")

    cuit = input("ingrese su numero de CUIT: ")
    descripcion = input("Ingrese la descripcion")
    validado = validar_cuit(cuit)

    print("el cuit " , cuit , "es " , validado)

principal()
    