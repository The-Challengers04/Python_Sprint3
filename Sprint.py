listaEstabelecimentos = []
listaUsuarios = []
listaPostsUsuario = []
listaPostsEstabelecimento = []
listaReviews = []
listaCupons = []
listaNotas = []

cupom = {'Nomeestabelecimento':'Jota', 'duração(dias)': '15', 'data_inicio': '11/09/2023', 'valor(%)': '15',
         'descricao': 'Cupom de desconto de 15% em qualquer produto da loja'}
estabelecimento = {'email':'oiii', 'estabelecimento': 'Jota', 'cnpj': '123456789', 'TipodeEstabelecimento': 'Restaurante', 'senha': '1234'}
reviews = {'usuario': 'biafarah123', 'estabelecimento': 'Jota', 'review': 'Gostei mt do restaurante'}
usuario = {'usuario': 'biafarah123', 'email': 'biaafarah@gmail.com', 'senha': '1234', 'cpf': '12345645678901'}
post = {'usuário': 'biafarah123', 'post': 'Esse é meu primeiro post'}
nota = {'estabelecimento': 'Jota', 'TipodeEstabelecimento': 'Restaurante', 'nota': '10'}

'Menu Estabelecimento'
def CadastrarCupom(listaCupons):
    while True:
        nomecupom = input('Qual é o nome do seu cupom? ')
        if any(user['Nomeestabelecimento'] == nomecupom for user in listaCupons):
            print('Cupom já cadastrado')
        else:
            duracao = input('Qual é a duração do seu cupom? ')
            data_inicio = input('Qual é a data de início do seu cupom? ')
            valor = input('Qual é o valor do seu cupom? ')
            descricao = input('Qual é a descrição do seu cupom? ')
            
            cupom = {'Nomeestabelecimento': nomecupom,
                     'duração(dias)': duracao,
                     'data_inicio': data_inicio,
                     'valor(%)': valor,
                     'descricao': descricao}
            
            listaCupons.append(cupom)
            print('Cupom cadastrado com sucesso')
            break

def VerReviwsEstabelecimento():
    return 2

def FazerPostEstabelecimento():
    return 3


'Menu usuários'
def FazerNovaReview():
    return 1
1

def VerReviewsUsuario():
    return 2

def FazerPostUsuario(listaPostsUsuario):
    while True:
        postUsuario = input('Escreva seu post: ')
        if any(user['post'] == postUsuario for user in listaPostsUsuario):
            print('Post já cadastrado')
        else:
            postUsuario = {'usuário': 'biafarah123',
                    'post': postUsuario}
            
            listaPostsUsuario.append(postUsuario)
            print('Post cadastrado com sucesso')
            break

def VerPostsUsuario():
    return 4

def DarNota(listaNotas):
    while True:
        nomeEstabelecimentoNota = input('Qual é o nome do estabelecimento que você deseja dar nota? ')
        notaEstabelecimento = input('Qual é a nota que você deseja dar? ')
        TipoEstabelecimento = input('Qual é o tipo do estabelecimento? ')

        Notas = {'TipodeEstabelecimento': TipoEstabelecimento,
                'estabelecimento': nomeEstabelecimentoNota,
                'nota': notaEstabelecimento}
        listaNotas.append(Notas)
        print('Nota cadastrada com sucesso')
        break

'Def MENU'
def CadastraEstabelecimento(listaEstabeelecimentos):
    while True:
        emailEstabelecimento = input('Cadastre seu email: ')
        if any(user['email'] == emailEstabelecimento for user in listaEstabeelecimentos):
            print('Email já cadastrado')
        else:
            nomeEstabelecimento = input('Qual é o nome do seu estabelecimento? ')
            senhaEstabelecimento = input('Cadastre sua senha: ')
            cnpj = input('Cadastre seu cnpj: ')
            tipoEstabelecimento = input('Tipo de estabelecimento: ')
            
            usuario = {'email': emailEstabelecimento,
                       'estabelecimento': nomeEstabelecimento,
                       'cnpj': cnpj,
                       'TipodeEstabelecimento': tipoEstabelecimento,
                       'senha': senhaEstabelecimento}
            
            listaEstabeelecimentos.append(usuario)
            print('Cadastro realizado com sucesso')
            print(listaEstabeelecimentos)
            break

def CadastraUsuario(listausuarios):
        while True:
            emailusuario = input('Cadastre seu email: ')
            if any(user['email'] == emailusuario for user in listaUsuarios):
                print('Email já cadastrado')
            else:
                LoginUsuario = input('Cadastre seu login: ')
                senhaUsuario = input('Cadastre sua senha: ')
                cpfusuario = input('Cadastre seu cpf: ')
                
                usuario = {'usuario': LoginUsuario,
                           'email': emailusuario,
                            'senha': senhaUsuario,
                            'cpf': cpfusuario}
                
                listausuarios.append(usuario)
                print('Cadastro realizado com sucesso')
                break

def LoginEstabelecimento():
    menuEstabelecimento = int(input())
    if menuEstabelecimento == 1:
        CadastrarCupom(listaCupons)
    elif menuEstabelecimento == 2:
        VerReviwsEstabelecimento(listaReviews)
    elif menuEstabelecimento == 3:
        FazerPostEstabelecimento(listaPostsEstabelecimento)

def LoginUsuario():
    menuUsuario = int(input('Seja bem vindo ao Inclui+! \n Escolha uma opção: \n 1 - cadastrar estabelecimento \n 2 - cadastrar usuário \n 3 - login estabelecimento \n 4 - login usuário: '))
    if menuUsuario == 1:
        FazerNovaReview(listaReviews)
    elif menuUsuario == 2:
        VerReviewsUsuario(listaReviews)
    elif menuUsuario == 3:
        FazerPostUsuario(listaPostsUsuario)
    elif menuUsuario == 4:
        VerPostsUsuario(listaPostsUsuario)
    elif menuUsuario == 5:
        DarNota(listaNotas)

menu = int(input('Seja bem vindo ao Inclui+! \n Escolha uma opção: \n 1 - cadastrar estabelecimento \n 2 - cadastrar usuário \n 3 - login estabelecimento \n 4 - login usuário: '))
if menu == 1:
    CadastraEstabelecimento(listaEstabelecimentos)
elif menu == 2:
    CadastraUsuario(listaUsuarios)
elif menu == 3:
    LoginEstabelecimento()
elif menu == 4:
    LoginUsuario()

