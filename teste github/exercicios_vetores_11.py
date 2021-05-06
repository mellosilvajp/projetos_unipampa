lista_numeros = []
lista_pares = []
lista_impares = []
numero = 0
print('Digite 20 números')
for i in range(20):
    lista_numeros.append(float(input('Digite um número: \n')))
    numero = lista_numeros[i]
    if numero %2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print('='*30)
print('Lista de todos os números digitados:',lista_numeros)
print('Lista de números pares:',lista_pares)
print('Lista de números ímpares:',lista_impares)

