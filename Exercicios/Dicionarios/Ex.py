#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}


#2 - Utilizando o dicionário criado no item 1:

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']

#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

pessoa = {'nome': ‘Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")


#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
