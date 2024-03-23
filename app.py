import os

restaurantes = [
                {'nome':'PizzaWorld', 'categoria':'Pizza', 'ativa':False},
                {'nome':'LasanhaExpress', 'categoria':'Lasanha', 'ativa':False}
            ]

def exibir_nome_programa():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░

    """)

def exibir_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar Estado Restaurantes')
    print('4. Sair\n')

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
        - Nome do restaurante
        - Categoria

        Output:
        - Adiciona um novo restaurante à lista de restaurantes

    '''
    exibir_sub_titulos('Cadastrar Restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante: \n')
    categoria_restaurante = input(f'Digite a categoria do {nome_restaurante}: \n')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativa':False}
    
    restaurantes.append(dados_restaurante)
    
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal() 

def listar_restaurante():
    exibir_sub_titulos('Listando Restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativa'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_menu_principal()

def alterar_estado_restaurante():
    exibir_sub_titulos('Alterar Estado Restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja altenar: \n')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativa'] = not restaurante['ativa']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativa'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado')

    voltar_menu_principal()


def finalizar_app():
    exibir_sub_titulos('Encerrando o programa')

def opcao_invalida():
    exibir_sub_titulos('Opcao Invalida')
    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def exibir_sub_titulos(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao_com_if():
    try:

        opcao_escolhida = int(input('Escolha uma opcao: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    
    except:
        opcao_invalida()

def escolher_opcao_com_match():
    
    try:
        
        opcao_escolhida = int(input('Escolha uma opcao: '))

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao_com_if()
    #escolher_opcao_com_match()

if __name__ == '__main__':
    main()