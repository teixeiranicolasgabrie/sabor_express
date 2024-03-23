print('5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.')

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")
