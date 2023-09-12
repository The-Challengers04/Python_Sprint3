lista = []
cupom = {'Nomeestabelecimento':'Jota', 'duração(dias)': '15', 'data_inicio': '11/09/2023', 'valor(%)': '15',
         'descricao': 'Cupom de desconto de 15% em qualquer produto da loja'}
estabelecimento = {'email':'oiii', 'estabelecimento': 'Jota', 'cnpj': '123456789', 'TipodeEstabelecimento': 'Restaurante', 'senha': '1234'}
reviews = {'usuario': 'biafarah123', 'estabelecimento': 'Jota', 'review': 'Gostei mt do restaurante'}
usuario = {'usuario': 'biafarah123', 'email': 'biaafarah@gmail.com', 'senha': '1234', 'cpf': '12345645678901'}
post = {'usuário': 'biafarah123', 'post': 'Esse é meu primeiro post'}
nota = {'estabelecimento': 'Jota', 'TipodeEstabelecimento': 'Restaurante', 'nota': '10'}

'Menu Estabelecimento'
def CadastrarCupom():
    return 1

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

def FazerPostUsuario():
    return 3

def VerPostsUsuario():
    return 4

def DarNota():
    return 5

'Def MENU'
def CadastraEstabelecimento(lista):
    while True:
        emailEstabelecimento = input('Cadastre seu email: ')
        if any(user['email'] == emailEstabelecimento for user in lista):
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
            
            lista.append(usuario)
            print('Cadastro realizado com sucesso')
            print(lista)
            break

def CadastraUsuario():
    return 3

def LoginEstabelecimento():
    menuEstabelecimento = int(input())
    if menuEstabelecimento == 1:
        CadastrarCupom()
    elif menuEstabelecimento == 2:
        VerReviwsEstabelecimento()
    elif menuEstabelecimento == 3:
        FazerPostEstabelecimento()

def LoginUsuario():
    menuUsuario = int(input())
    if menuUsuario == 1:
        FazerNovaReview()
    elif menuUsuario == 2:
        VerReviewsUsuario()
    elif menuUsuario == 3:
        FazerPostUsuario()
    elif menuUsuario == 4:
        VerPostsUsuario()
    elif menuUsuario == 5:
        DarNota()

menu = int(input('Escolha uma opção (1 para cadastrar estabelecimento, 2 para cadastrar usuário, 3 para login estabelecimento, 4 para login usuário): '))
if menu == 1:
    CadastraEstabelecimento(lista)
elif menu == 2:
    CadastraUsuario()
elif menu == 3:
    LoginEstabelecimento()
elif menu == 4:
    LoginUsuario()
