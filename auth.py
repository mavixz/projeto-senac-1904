
user = 'root'
password = 123

while True:
    insertUser = input('Insira o seu uruário: ')
    insertpassword = int(input('Insira sua senha: '))
    if insertUser == user and insertpassword == password:

        print(f'\nUsuário {user} logado!\n')
        # Sistema 
        valor=soma=H=C=M=K=Q=X=0
        opcao=''
        while opcao!='X':
            print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
Q       Queijo Prato    4,00
K       Coca-Cola       7,00
X       ENCERRAR PEDIDO \n
            ''')
            opcao=input().upper()[0]
            soma+=valor
            
            if opcao=='H':
                valor=5.50
                print("Hambúrguer adicionado!\n")
            elif opcao=='C':
                valor=6.80
                print("Cheeseburger adicionado!\n")
            elif opcao=='M':
                valor=4.50
                print("Misto Quente adicionado!\n")
            elif opcao=='K':
                valor=7.00
                print("Coca-Cola adicionado!\n")
            elif opcao=='Q':
                valor=4.00
                print("Queijo Prato adicionado!\n")
            elif opcao=='X':
                print("Finalizando compra...\n")
                break
            else:
                print('Opção inválida\n')

     
        print(f'O valor da conta é: {soma:.2f}')
        break

    else:
        if insertUser != user:
            print('Usuário Incorreto!')
        elif insertpassword != password:
            print('Senha incorreta!')
        while True: 
            option = input('Deseja recuperar a senha? S/N: ').upper()[0]
            if option == 'S':
                user = input('Insira um novo usuário: ')
                password = int(input('Insira uma nova senha: '))
                print('Login alterado!')
                break
            elif option == 'N':
                break
            else:
                print('Insira apenas S ou N!!')
