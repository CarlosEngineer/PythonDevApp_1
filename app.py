import os 

restaurantes = [{'nome': 'pizza', 'categoria':'massa', 'ativo': False},
                {'nome': 'Nahoe', 'categoria':'japanese', 'ativo': True },
                {'nome': 'burguers', 'categoria':'massa', 'ativo': False}]

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
\n''')

def exibir_opcao():
    print('1. Cadastrar Cliente ')
    print('2. Listar Restaurante ')
    print('3. Alternar estado do Restaurante  ')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')
    
def voltar_ao_menu_principal():
    input('\n\nDigite uma tecla para voltar ao menu principal: \n\n\n')
    main()

def opcao_invalida():
    print('\nOpção inválida! Tente novamente.\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*'* (len(texto))
    print(f'\n{linha}\n{texto}\n{linha}')
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    clategoria = input(f'Digite a categoria do restaurante: {nome_do_restaurante}: \n')
    dados_do_restaurante =  {'nome': nome_do_restaurante, 'categoria':clategoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print('\n\nRestaurante {} foi adicionado com sucesso!\n'.format(nome_do_restaurante))
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('listando restaurante')
    print(f"{'Nome do restaurante'.ljust(21)} | {'categoria'.ljust(20)} | status")

    for restaurante in  restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante ['ativo'] else 'desativado' 

        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def Ativar_Restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alternar o estado \n')
    restaurante_encontrado = False 



    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']  # muda o status para o contrário
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante['ativo'] else "O restaurante foi desativado com sucesso!"
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontratdo')


    voltar_ao_menu_principal()


    


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao:'))
        print(f'Voce escolheu a opcao: {opcao_escolhida}')

        if (opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif (opcao_escolhida == 2):
            listar_restaurante()
        elif (opcao_escolhida == 3):
            Ativar_Restaurante()
        elif (opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()



def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()


if __name__== '__main__':
    main()