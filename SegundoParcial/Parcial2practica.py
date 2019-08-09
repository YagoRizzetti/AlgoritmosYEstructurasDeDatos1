def ControlTexto(texto):
    palabras_n = 0
    palabras_t = 0
    letras_pal = 0
    tiene_n = False
    empieza_t = False

    for l in texto:
        if l == " " or l == ".":
            if letras_pal > 4 and tiene_n:
                palabras_n += 1
            letras_pal = 0
            tiene_n = False
            if empieza_t:
                palabras_t += 1
                letras_palt += letras_pal
        else:
            letras_pal += 1
            if l == "n":
                tiene_n = True
            if letras_pal == 1 and letras_pal == "t"
                empieza_t = True
    return palabras_n

def main():
    texto = input("Ingrese un texto que termine con un punto.")
    tex = ControlTexto(texto)
    print(tex)


main()