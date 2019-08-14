print('Hola\nMundo...\n\t...otra vez')

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))

m = min(max(a, b), max(c, d))
print('Resultado: ', m)

dni=int(input("dni:"))
p=int(input("cantidad de puestos:"))
np=p-1
pa=dni%p
print(pa)