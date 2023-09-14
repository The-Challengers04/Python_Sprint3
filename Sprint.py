import json

# Dicionário para armazenar várias listas
data = {}

# Para recuperar os dados do arquivo JSON
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Agora você pode acessar cada lista individualmente
listaEstabelecimentos = data['listaEstabelecimentos']
listaUsuarios = data['listaUsuarios']
listaPostsUsuario = data['listaPostsUsuario']
listaPostsEstabelecimento = data['listaPostsEstabelecimento']
listaReviews = data['listaReviews']
listaCupons = data['listaCupons']
listaNotas = data['listaNotas']


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
    reviews_estabelecimento = []
    nomeestabelecimento = input('Qual é o nome do seu estabelecimento? ')
    for review in listaReviews:
        if review['estabelecimento'] == nomeestabelecimento:
            reviews_estabelecimento.append(review)

    if not reviews_estabelecimento:
        print('Nenhuma review encontrada para este estabelecimento.')
    else:
        print('Reviews do estabelecimento:')
        for review in reviews_estabelecimento:
            print(f'Usuário: {review["usuario"]}')
            print(f'Review: {review["review"]}')
            print('-' * 20)


def FazerPostEstabelecimento(listaPostsEstabelecimento):
    while True:
        postEstabelecimento = input('Escreva seu post: ')
        if any(user['post'] == postEstabelecimento for user in listaPostsEstabelecimento):
            print('Post já cadastrado')
        else:
            postEstabelecimento = {'usuário': 'biafarah123',
                    'post': postEstabelecimento}
            
            listaPostsEstabelecimento.append(postEstabelecimento)
            print('Post cadastrado com sucesso')
            break


'Menu usuários'
def MenuUsuario():
    menuUsuario = int(input('Seja bem vindo de volta ao Inclui+! \n Escolha uma opção: \n 1 - Fazer nova review \n 2 - ver suas reviews \n 3 - fazer um novo post na comunidade \n 4 - ver seus posts na comunidade \n 5 - dar nota para um estabelecimento: '))
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

def menuEstabelecimento():
    menuEstabelecimento = int(input('Seja bem vindo de volta ao Inclui+! \n Escolha uma opção: \n 1 - Cadastrar cupom \n 2 - Ver reviews do seu estabelecimento \n 3 - Fazer um novo post na comunidade:'))
    if menuEstabelecimento == 1:
        CadastrarCupom(listaCupons)
    elif menuEstabelecimento == 2:
        VerReviwsEstabelecimento()
    elif menuEstabelecimento == 3:
        FazerPostEstabelecimento(listaPostsEstabelecimento)

def FazerNovaReview():
    while True:
        nomeEstabelecimentoReview = input('Qual é o nome do estabelecimento que você deseja fazer uma review? ')
        if any(user['estabelecimento'] == nomeEstabelecimentoReview for user in listaReviews):
            print('Review já cadastrada')
        else:
            review = input('Escreva sua review: ')
            usuario = ()
            usuario = obterUsuario(emailusuario)
            reviewUsuario = {'usuario': usuario,
                    'estabelecimento': nomeEstabelecimentoReview,
                    'review': review}
            
            listaReviews.append(reviewUsuario)
            print('Review cadastrada com sucesso')
            break

def VerReviewsUsuario():
    reviews_usuario = []
    login_usuario = input('Qual é seu nome de usuário? ')
    for review in listaReviews:
        if review['usuario'] == login_usuario:
            reviews_usuario.append(review)
    print(reviews_usuario)

    if not reviews_usuario:
        print('Nenhuma review encontrada para este estabelecimento.')
    else:
        print('Reviews do estabelecimento:')
        for review in reviews_usuario:
            print(f'Usuário: {review["usuario"]}')
            print(f'Estabelecimento: {review["estabelecimento"]}')
            print(f'Review: {review["review"]}')
            print('-' * 20)

def FazerPostUsuario(listaPostsUsuario):
    while True:
        postUsuario = input('Escreva seu post: ')
        if any(user['post'] == postUsuario for user in listaPostsUsuario):
            print('Post já cadastrado')
        else:
            usuario = ()
            usuario = obterUsuario(emailusuario)
            postUsuario = {'usuário': usuario,
                    'post': postUsuario}
            
            listaPostsUsuario.append(postUsuario)
            print('Post cadastrado com sucesso')
            break

def VerPostsUsuario(listaPostsUsuario):
    posts_usuario = []
    login_usuario = input('Qual é seu nome de usuário? ')
    for post in listaPostsUsuario:
        if post['usuario'] == login_usuario:
            posts_usuario.append(post)

    if not posts_usuario:
        print('Nenhum post encontrado. ')
    else:
        print('Posts do estabelecimento:')
        for post in posts_usuario:
            print(f'Usuário: {post["usuario"]}')
            print(f'Estabelecimento: {post["estabelecimento"]}')
            print(f'Post: {post["post"]}')
            print('-' * 20)

def DarNota(listaNotas):
    while True:
        nomeEstabelecimentoNota = input('Qual é o nome do estabelecimento que você deseja dar nota? ')
        notaEstabelecimento = int(input(f'Digite uma nota (de 0 a 5) para a acessibilidade dentro do estabelecimento {nomeEstabelecimentoNota}: '))  # Solicita uma nota de acessibilidade ao estabelecimento
        if notaEstabelecimento <= 5:
            TipoEstabelecimento = input('Qual é o tipo do estabelecimento? ')

            Notas = {'TipodeEstabelecimento': TipoEstabelecimento,
                    'estabelecimento': nomeEstabelecimentoNota,
                    'nota': notaEstabelecimento}
            listaNotas.append(Notas)
            print('Nota cadastrada com sucesso')
            break

        else:
            print('Digite um valor válido!')
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
            cnpj = int(input('Cadastre seu cnpj (Digite apenas números): '))
            tipoEstabelecimento = input('Tipo de estabelecimento: ')
            
            usuario = {'email': emailEstabelecimento,
                       'estabelecimento': nomeEstabelecimento,
                       'cnpj': cnpj,
                       'TipodeEstabelecimento': tipoEstabelecimento,
                       'senha': senhaEstabelecimento}
            
            listaEstabeelecimentos.append(usuario)
            print('Cadastro realizado com sucesso')
            print(listaEstabeelecimentos)

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

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

                with open('data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)

                print('Cadastro realizado com sucesso')
                break

def LoginEstabelecimento(*args):
    global emailestabelecimento
    emailestabelecimento = input('Bem vindo de volta a Inclui+! Qual é seu email? ')
    if any(user['email'] == emailestabelecimento for user in listaEstabelecimentos):
        senhaEstabelecimento = input('Qual é sua senha?: ')
        if any(user['senha'] == senhaEstabelecimento for user in listaEstabelecimentos):
            print('Login realizado com sucesso')
            menuEstabelecimento()
        else:
            print('Senha incorreta')
            LoginEstabelecimento(listaEstabelecimentos)
    else:
        print('Email não cadastrado')
        CadastraEstabelecimento(listaEstabelecimentos)

def LoginUsuario(listaUsuarios):
    global emailusuario
    emailusuario = input('Bem vindo de volta a Inclui+! Qual é seu email? ')
    if any(user['email'] == emailusuario for user in listaUsuarios):
        senhaUsuario = input('Qual é sua senha?: ')
        if any(user['senha'] == senhaUsuario for user in listaUsuarios):
            print('Login realizado com sucesso')
            MenuUsuario()
        else:
            print('Senha incorreta')
            LoginUsuario(listaUsuarios)
    else:
        print('Email não cadastrado')
        CadastraUsuario(listaUsuarios)

def obterUsuario(emailusuario):
    for usuario in listaUsuarios:
        if usuario["email"] == emailusuario:
            return usuario["usuario"]

def obterEstabelecimento(emailestabelecimento):
    for estabelecimento in listaUsuarios:
        if estabelecimento["email"] == emailestabelecimento:
            return estabelecimento["estabelecimento"]



try:
    menu = int(input('Seja bem vindo ao Inclui+! \n Escolha uma opção: \n 1 - Cadastrar estabelecimento \n 2 - Cadastrar usuário \n 3 - Login estabelecimento \n 4 - Login usuário \n'))
    match menu:
        case 1: 
            CadastraEstabelecimento(listaEstabelecimentos)
        case 2: 
            CadastraUsuario(listaUsuarios)
        case 3: 
            LoginEstabelecimento()
        case 4:
            LoginUsuario(listaUsuarios)
        case other: 
            print('Opção inválida')  
except ValueError:
    print('Opção inválida')  