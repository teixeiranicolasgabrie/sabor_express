print('Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais.')
pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))
