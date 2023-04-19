user = 'root'
password = 123

while True:
    insertUser = input('Insira o seu uruário: ')
    insertpassword = int(input('Insira sua senha: '))
    if insertUser == user and insertpassword == password:
        print(f'Usuário {user} logado!')
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
