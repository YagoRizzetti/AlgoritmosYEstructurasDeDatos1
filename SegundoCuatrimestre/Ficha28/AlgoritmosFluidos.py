def greedy_change(x):
    monedas = [25,10,5,1]
    contador = 0
    acumulador = 0
    if x in monedas:
        for i in monedas:
            if i == x:
                return 1
    else:
        for i in monedas:
            while acumulador + i <= x:
                acumulador += i
                contador += 1
            if acumulador == x:
                break
        return contador

def main():
    x = int(input("Ingrese x: "))
    cant = greedy_change(x)
    print("La cantidad de monedas es: ", cant)

main()