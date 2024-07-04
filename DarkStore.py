import os
import time

usuarios = [
    {'usuario': 'eydi', 'senha': 'senha', 'admin': True}    
]

produtos = [
    {'nome': 'Celular', 'preco': 2000.00, 'descricao': 'Smartphone Samsung Galaxy S23 256GB'}
]

produtos_carrinho = [
    {}
]

historico_compra = [
    {}
]

def titulo():
    print("""\n
    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ─████████████───██████████████─████████████████───██████──████████─██████████████─██████████████─██████████████─████████████████───██████████████─
    ─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
    ─██░░████░░░░██─██░░██████░░██─██░░████████░░██───██░░██──██░░████─██░░██████████─██████░░██████─██░░██████░░██─██░░████████░░██───██░░██████████─
    ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██───██░░██─────────────██░░██─────██░░██──██░░██─██░░██────██░░██───██░░██─────────
    ─██░░██──██░░██─██░░██████░░██─██░░████████░░██───██░░██████░░██───██░░██████████─────██░░██─────██░░██──██░░██─██░░████████░░██───██░░██████████─
    ─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██───██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
    ─██░░██──██░░██─██░░██████░░██─██░░██████░░████───██░░██████░░██───██████████░░██─────██░░██─────██░░██──██░░██─██░░██████░░████───██░░██████████─
    ─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██───────────██░░██─────██░░██─────██░░██──██░░██─██░░██──██░░██─────██░░██─────────
    ─██░░████░░░░██─██░░██──██░░██─██░░██──██░░██████─██░░██──██░░████─██████████░░██─────██░░██─────██░░██████░░██─██░░██──██░░██████─██░░██████████─
    ─██░░░░░░░░████─██░░██──██░░██─██░░██──██░░░░░░██─██░░██──██░░░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─
    ─████████████───██████──██████─██████──██████████─██████──████████─██████████████─────██████─────██████████████─██████──██████████─██████████████─
    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n""")

def menu_login():
    print("1.	Cadastrar")
    print("2.	Login")
    print()

def menu():
    print("""
█▀▄▀█ █▀▀ █▄░█ █░█ ▀
█░▀░█ ██▄ █░▀█ █▄█ ▄\n""")
    print("1.	Catálogo de Produtos")
    print("2.	Adicionar Produtos ao Carrinho")
    print("3.	Remover Produtos do Carrinho")
    print("4.	Visualização de Carrinho")
    print("5.	Comprar")
    print("6.	Histórico de Compras")
    print("0.	Sair")
    print()

def menu_admin():
    print("""
█▀▄▀█ █▀▀ █▄░█ █░█   ▄▀█ █▀▄ █▀▄▀█
█░▀░█ ██▄ █░▀█ █▄█   █▀█ █▄▀ █░▀░█\n""")
    print("1.	Catálogo de Produtos")
    print("2.	Adicionar Produtos ao Carrinho")
    print("3.	Remover Produtos do Carrinho")
    print("4.	Visualização de Carrinho")
    print("5.	Comprar")
    print("6.	Histórico de Compras")
    print("7.	Administração de Estoque")
    print("0.	Sair")
    print()

def limpar_tela():
    os.system('cls')

def opc_invalida(is_admin=False):
    limpar_tela()
    print("\nOpção inválida!\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def escolha_login():
    try:
        escolha_opc_login = int(input("\nEscolha uma opção: "))
        
        if escolha_opc_login == 1:
            cadastro_usuario()
        elif escolha_opc_login == 2:
            login_usuario()
        else:
            opc_invalida()  # Chama opc_invalida apenas se a escolha não for 1 ou 2
    except ValueError:  # Captura apenas exceções de ValueError (para input não numérico)
        opc_invalida()

def escolha(is_admin=False):
    try:
        escolha_opc = int(input("\nEscolha uma opção: "))
        
        if escolha_opc == 1:
            catalogo_produtos(is_admin)
        elif escolha_opc == 2:
            add_produto_carrinho(produtos, produtos_carrinho, is_admin)
        elif escolha_opc == 3:
            remove_produto_carrinho(produtos_carrinho, is_admin)
        elif escolha_opc == 4:
            vizu_carrinho(is_admin)
        elif escolha_opc == 5:
            compra(is_admin)
        elif escolha_opc == 6:
            print("6. Histórico de Compras")
        elif escolha_opc == 0:
            limpar_tela()
            print('Saindo...\n')
            time.sleep(2)
            main()
        elif is_admin and escolha_opc == 7:
            print("7. Administração de Estoque")
        else:
            if is_admin:
                    darkstore_admin()
            else:
                darkstore()
    except ValueError:  # Captura apenas exceções de ValueError (para input não numérico)
        if is_admin:
            darkstore_admin()
        else:
            darkstore()

def cadastro_usuario():
    limpar_tela()
    nome_usuario = input('Como gostaria de ser chamado: ')
    senha_usuario = input('Digite uma senha: ')
    senha_usuario_con = input('Confirme a senha: ')
    if senha_usuario == senha_usuario_con:
        dados_usuario = {'usuario':nome_usuario, 'senha':senha_usuario, 'admin': False}
        usuarios.append(dados_usuario)
        sucess = 'Usuário cadastrado com sucesso!'
        linha = '*' * (len(sucess))
        print(f'\n{linha}')
        print(sucess)
        print(f'{linha}\n')
        time.sleep(2)
        print('Voltando para a tela inicial...\n')
        time.sleep(2)
        main()
    else:
        time.sleep(2)
        print('''\n
              Erro!
              A senha de confirmação não corresponde a senha informada''')
        time.sleep(2)
        print('\nRealize novamente o cadastro...')
        time.sleep(3)
        cadastro_usuario()

def login_usuario():
    limpar_tela()
    usuario_login = input('Usuário: ')
    senha_login = input('Senha: ')

    # Check if user exists
    usuario_encontrado = False
    usuario_admin = False
    
    for usuario in usuarios:
        if usuario_login == usuario['usuario']:
            if senha_login == usuario['senha']:
                usuario_encontrado = True
                usuario_admin = usuario['admin']
                break
    
    if usuario_encontrado:
        login_sucess = 'Login feito com sucesso'
        linha = '*' * (len(login_sucess))
        print(f'\n{linha}')
        print(login_sucess)
        print(f'{linha}\n')
        time.sleep(2)

        limpar_tela()
        print('''

        █▄▄ █▀▀ █▀▄▀█   █░█ █ █▄░█ █▀▄ █▀█ █
        █▄█ ██▄ █░▀░█   ▀▄▀ █ █░▀█ █▄▀ █▄█ ▄

                            ''')
        time.sleep(2)
        
        if usuario_admin:
            darkstore_admin()
        else:
            darkstore()
    else:    
        time.sleep(2)
        print('\nUsuário ou senha incorretos ou usuário não cadastrado.\n')
        time.sleep(2)
        print('Tente novamente...')
        time.sleep(2)
        main()

def catalogo_produtos(is_admin=False):
    while True:
        limpar_tela()
        print('''
█░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀█ █▀█ █▀█ █▀▄ █░█ ▀█▀ █▀█ █▀
█▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   █▀▀ █▀▄ █▄█ █▄▀ █▄█ ░█░ █▄█ ▄█\n''')

        print(f'{"NOME DO PRODUTO".ljust(20)} | {"PREÇO".ljust(20)} | DESCRIÇÃO')
        print('-' * 60)

        for produto in produtos:
            nome_produto = produto['nome']
            preco_produto = produto['preco']
            descricao_produto = produto['descricao']
            preco_formatado = f'R${preco_produto:,.2f}'
            print(f'{nome_produto.ljust(20)} | {preco_formatado.ljust(20)} | {descricao_produto}')
        
        print("\nDigite 's' para sair do catálogo e voltar ao menu principal.")
        escolha = input("Escolha: ").strip().lower()

        if escolha == 's':
            if is_admin:
                darkstore_admin()
            else:
                darkstore()
            break

def add_produto_carrinho(produtos, produtos_carrinho, is_admin=False):
    while True:
        limpar_tela()
        print('''
▄▀█ █▀▄ █ █▀▀ █ █▀█ █▄░█ ▄▀█ █▀█   █▀█ █▀█ █▀█ █▀▄ █░█ ▀█▀ █▀█ █▀   ▄▀█ █▀█   █▀▀ ▄▀█ █▀█ █▀█ █ █▄░█ █░█ █▀█
█▀█ █▄▀ █ █▄▄ █ █▄█ █░▀█ █▀█ █▀▄   █▀▀ █▀▄ █▄█ █▄▀ █▄█ ░█░ █▄█ ▄█   █▀█ █▄█   █▄▄ █▀█ █▀▄ █▀▄ █ █░▀█ █▀█ █▄█\n''')
        
        nome_produto = input('Digite o nome do produto que deseja adicionar ao carrinho: ')

        produto_encontrado = None
        for produto in produtos:
            if produto['nome'] == nome_produto:
                produto_encontrado = produto
                break
        
        if produto_encontrado:
            print(f'''
            O produto que deseja adicionar ao carrinho é:
            Nome: {produto_encontrado['nome']}
            Preço: R${produto_encontrado['preco']:,.2f}
            Descrição: {produto_encontrado['descricao']}''')

            escolha = input("\nDigite 's' para adicionar o produto ao carrinho: ").strip().lower()

            if escolha == 's':
                produtos_carrinho.append(produto_encontrado)
                print("\nProduto adicionado ao carrinho!")

        else:
            print(f"\nProduto '{nome_produto}' não encontrado.")

        continuar = input("\nDeseja adicionar outro produto ao carrinho? (s/n): ").strip().lower()
        if continuar != 's':
            if is_admin:
                darkstore_admin()
            else:
                darkstore()
            break

def remove_produto_carrinho(produtos_carrinho, is_admin=False):
    while True:
        limpar_tela()
        print('''
█▀█ █▀▀ █▀▄▀█ █▀█ █░█ █▀▀ █▀█   █▀█ █▀█ █▀█ █▀▄ █░█ ▀█▀ █▀█ █▀   █▀▄ █▀█   █▀▀ ▄▀█ █▀█ █▀█ █ █▄░█ █░█ █▀█
█▀▄ ██▄ █░▀░█ █▄█ ▀▄▀ ██▄ █▀▄   █▀▀ █▀▄ █▄█ █▄▀ █▄█ ░█░ █▄█ ▄█   █▄▀ █▄█   █▄▄ █▀█ █▀▄ █▀▄ █ █░▀█ █▀█ █▄█\n''')
        
        nome_produto = input('Digite o nome do produto que deseja remover do carrinho: ')

        # Verifica se o produto está no carrinho
        produto_encontrado = None
        for produto in produtos_carrinho:
            if 'nome' in produto and produto['nome'].lower() == nome_produto.lower():
                produto_encontrado = produto
                break
        
        if produto_encontrado:
            print(f'''
            O produto que deseja remover do carrinho é:
            Nome: {produto_encontrado['nome']}
            Preço: R${produto_encontrado['preco']:,.2f}
            Descrição: {produto_encontrado['descricao']}''')

            escolha = input("\nDigite 's' para remover o produto do carrinho: ").strip().lower()

            if escolha == 's':
                produtos_carrinho.remove(produto_encontrado)
                print("\nProduto removido do carrinho!")

        else:
            print(f"\nProduto '{nome_produto}' não encontrado no carrinho.")

        continuar = input("\nDeseja remover outro produto do carrinho? (s/n): ").strip().lower()
        if continuar != 's':
            if is_admin:
                darkstore_admin()
            else:
                darkstore()
            break

def vizu_carrinho(is_admin=False):
    while True:
        limpar_tela()
        print('''
█▀▀ ▄▀█ █▀█ █▀█ █ █▄░█ █░█ █▀█
█▄▄ █▀█ █▀▄ █▀▄ █ █░▀█ █▀█ █▄█\n''')

        if produtos_carrinho:
            print(f'{"NOME DO PRODUTO".ljust(20)} | {"PREÇO".ljust(20)} | DESCRIÇÃO')
            print('-' * 60)
            for produto in produtos_carrinho:
                if 'nome' in produto and 'preco' in produto and 'descricao' in produto:
                    nome_produto = produto['nome']
                    preco_produto = produto['preco']
                    descricao_produto = produto['descricao']
                    preco_formatado = f'R${preco_produto:,.2f}'
                    print(f'{nome_produto.ljust(20)} | {preco_formatado.ljust(20)} | {descricao_produto}')

        print("\nDigite 's' para sair do carrinho e voltar ao menu principal.")
        escolha = input("Escolha: ").strip().lower()

        if escolha == 's':
            if is_admin:
                darkstore_admin()
            else:
                darkstore()
            break

def compra(is_admin=False):
    cont = 0
    limpar_tela()
    print('''
█▀▀ █▀█ █▀▄▀█ █▀█ █▀█ ▄▀█ █▀█
█▄▄ █▄█ █░▀░█ █▀▀ █▀▄ █▀█ █▀▄\n''')

    while True:
        if produtos_carrinho:
            print(f'{"NOME DO PRODUTO".ljust(20)} | {"PREÇO".ljust(20)} | DESCRIÇÃO')
            print('-' * 60)
            for produto in produtos_carrinho:
                if 'nome' in produto and 'preco' in produto and 'descricao' in produto:
                    nome_produto = produto['nome']
                    preco_produto = produto['preco']
                    descricao_produto = produto['descricao']
                    preco_formatado = f'R${preco_produto:,.2f}'
                    print(f'{nome_produto.ljust(20)} | {preco_formatado.ljust(20)} | {descricao_produto}')
                    cont = cont + 1

        print()
        print("1.	Finalizar Compra")
        print("2.	Remover Produto")
        print("3.	Continuar Comprando")
        print("4.	Voltar para o Menu")

        escolha = input("\nEscolha: ").strip()

        if escolha == '1':
            if cont > 0:
                finalizar_compra()
            elif cont == 0:
                print("Não há produtos no carrinho. Adicione produtos antes de finalizar a compra.\n")
                time.sleep(2)
                catalogo_produtos()
                print()
        elif escolha == '2':
            remove_produto_carrinho(produtos_carrinho, is_admin)
        elif escolha == '3':
            add_produto_carrinho(produtos, produtos_carrinho, is_admin)
        elif escolha == '4':
            if is_admin:
                darkstore_admin()
            else:
                darkstore()
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")
            limpar_tela()

def finalizar_compra(is_admin=False):
    limpar_tela()
    print('''
█▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀█ █░█ ▀█▀
█▄▄ █▀█ ██▄ █▄▄ █░█ █▄█ █▄█ ░█░\n''')
    
    nome = input('Nome: ')
    email = input('Email: ')
    endereco = input('Endereço: ')
    
    while True:
        print('''
        Forma de pagamento:
            1.	Pix
            2.	Cartão de crédito
    ''')
    
        forma_pag = input('Qual será a forma de pagamento: ').strip()

        if forma_pag == '1':
            limpar_tela()
            print('Criando qrcode...')
            time.sleep(2)

            print('''
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬛️
⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️
⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️
⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️
⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬛️⬜️
⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️
⬜️⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬜️
⬜️⬛️⬜️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬛️
⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬛️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬛️⬛️
⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬛️⬜️
⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️
⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬛️⬛️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬛️
⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️
⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬜️
⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️
⬛️⬜️⬛️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️
⬛️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬛️⬛️

Chave pix: pix@darkstore.com
''')
            input('Digite uma tecla para voltar ao menu')
            for produto in produtos_carrinho:
                historico_compra.append(produto)
            
            produtos_carrinho.clear()
            
            if is_admin:
                darkstore_admin()
            else:
                darkstore()
            break
        elif forma_pag == '2':
            limpar_tela()
            numero_cartao = input('Número do cartão: ')
            codigo_seguranca = input('Código de segurança: ')
            nome_cartao = input('Nome do cartão: ')
            data_validade = input('Data de validade: ')
            
            print("\nConcluindo pagamento...")
            time.sleep(2)
            
            for produto in produtos_carrinho:
                historico_compra.append(produto)
            
            produtos_carrinho.clear()
            
            pag_sucesso = 'Pagamento concluído!'
            linha = '*' * (len(pag_sucesso))
            print(f'\n{linha}')
            print(pag_sucesso)
            print(f'{linha}\n')
            time.sleep(2)
            if is_admin:
                darkstore_admin()
            else:
                darkstore()
            break
            
        else:
            print('Opção inválida. Escolha uma opção válida.')
            limpar_tela()

def main():
    limpar_tela()
    titulo()
    menu_login()
    escolha_login()

def darkstore():
    limpar_tela()
    titulo()
    menu()
    escolha()

def darkstore_admin():
    limpar_tela()
    titulo()
    menu_admin()
    escolha(is_admin=True)


if __name__ == '__main__':
    main()
