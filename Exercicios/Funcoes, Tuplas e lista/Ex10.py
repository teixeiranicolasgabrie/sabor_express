print('6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções')

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
