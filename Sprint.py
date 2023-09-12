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

def VerReviewsUsuario():
    return 2

def FazerPostUsuario():
    return 3

def VerPostsUsuario():
    return 4

def DarNota():
    return 5


'Def MENU'

def CadastraEstabelecimento(estabelecimento):
    emailEstabelecimento = input('Cadastre seu email')
    if emailEstabelecimento in estabelecimento:
        print('Você já está cadastrado')
    else:
        nomeEstabelecimento = input('Qual é o nome do seu estabelecimento?')
        senhaEstabelecimento = input('Cadastre sua senha')
        cnpj = input('Cadastre seu cnpj')
        tipoEstabelecimento = input('Tipo de estabelecimento')
        print('Cadastro realizado com sucesso')
        estabelecimento[emailEstabelecimento] = {
            'estabelecimento': nomeEstabelecimento,
            'cnpj': cnpj,
            'TipodeEstabelecimento': tipoEstabelecimento,
            'senha': senhaEstabelecimento
        }
        print(estabelecimento)
        
    

def CadastraUsuario():
    return 2


def LoginEstabelecimento():
    menuEstabelecimento = int(input())
    match menuEstabelecimento:
        case 1: CadastrarCupom()
        case 2: VerReviwsEstabelecimento()
        case 3: FazerPostEstabelecimento()

def LoginUsuario():
    menuUsuario = int(input())
    match menuUsuario:
        case 1: FazerNovaReview()
        case 2: VerReviewsUsuario()
        case 3: FazerPostUsuario()
        case 4: VerPostsUsuario()
        case 5: DarNota()

menu = int(input())
match menu:
    case 1: 
        CadastraEstabelecimento(estabelecimento)
    case 2:
        CadastraUsuario()
    case 3:
        LoginEstabelecimento()
    case 4:
        LoginUsuario()
