#Importando a bibilioteca Json e a função exit do sys
import json
from sys import exit

#Definindo o data, onde serão armazenados todos os dados obtidos
data = {}

#Puxando dados do arquivo data.json
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

#Listas para armazenamento dentro do código
listaEstabelecimentos = data['listaEstabelecimentos']
listaUsuarios = data['listaUsuarios']
listaPostsUsuario = data['listaPostsUsuario']
listaPostsEstabelecimento = data['listaPostsEstabelecimento']
listaReviews = data['listaReviews']
listaCupons = data['listaCupons']
listaNotas = data['listaNotas']

#Função de cadastro de cupom
def CadastrarCupom(listaCupons):
    while True:
        print('-' * 40)
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

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print('Cupom cadastrado com sucesso')
            break

#Função para visualizar as reviews
def VerReviwsEstabelecimento(listaReviews):
    print('-' * 40)
    nomeEstabelecimento = obterEstabelecimento(emailestabelecimento)
    reviews_estabelecimento = []
    for review in listaReviews:
        if review['estabelecimento'] == nomeEstabelecimento:
            reviews_estabelecimento.append(review)

    if not reviews_estabelecimento:
        print('Nenhuma review encontrada para este estabelecimento.')
    else:
        print('Reviews do estabelecimento:')
        for review in reviews_estabelecimento:
            print(f'Usuário: {review["usuario"]}')
            print(f'Review: {review["review"]}')
            print('-' * 40)

#Função de Criação de post
def FazerPostEstabelecimento(listaPostsEstabelecimento):
    while True:
        print('-' * 40)
        postEstabelecimento = input('Escreva seu post: ')
        if any(user['post'] == postEstabelecimento for user in listaPostsEstabelecimento):
            print('Post já cadastrado')
        else:
            estabelecimento = obterEstabelecimento(emailestabelecimento)
            postEstabelecimento = {'usuário': estabelecimento,
                    'post': postEstabelecimento}
            
            listaPostsEstabelecimento.append(postEstabelecimento)

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print('Post cadastrado com sucesso')
            break

#Função para menu para cliente
def MenuUsuario():
    while True:
        try:
            print('-' * 40)
            menuUsuario = int(input('Seja bem vindo de volta ao Inclui+! \n Escolha uma opção: \n 1 - Fazer nova review \n 2 - Ver suas reviews \n 3 - Fazer um novo post na comunidade \n 4 - Ver seus posts na comunidade \n 5 - Dar nota para um estabelecimento \n 6 - Sair \n 7 - Logout \n'))
            match menuUsuario:
                case 1:
                    FazerNovaReview(listaReviews)
                case 2:
                    VerReviewsUsuario(listaReviews)
                case 3:
                    FazerPostUsuario(listaPostsUsuario)
                case 4:
                    VerPostsUsuario(listaPostsUsuario)
                case 5:
                    DarNota(listaNotas)
                case 6:
                    exit()
                case 7:
                    break
        except ValueError:
            print('Opção inválida')

#Função de menu para estabelecimentos
def menuEstabelecimento():
    while True:
        try:
            print('-' * 40)
            menuEstabelecimento = int(input('Seja bem vindo de volta ao Inclui+! \n Escolha uma opção: \n 1 - Cadastrar cupom \n 2 - Ver reviews do seu estabelecimento \n 3 - Fazer um novo post na comunidade \n 4 - Sair \n 5 - Logout \n'))
            match menuEstabelecimento:    
                case 1:
                    CadastrarCupom(listaCupons)
                case 2:
                    VerReviwsEstabelecimento(listaReviews)
                case 3:
                    FazerPostEstabelecimento(listaPostsEstabelecimento)
                case 4:
                    exit()
                case 5:
                    break
        except ValueError:
            print('Opção inválida')

#Função de criação de Review
def FazerNovaReview(listaReviews):
    while True:
        print('-' * 40)
        nomeEstabelecimentoReview = input('Qual é o nome do estabelecimento que você deseja fazer uma review? ')
        if any(user['estabelecimento'] == nomeEstabelecimentoReview for user in listaReviews):
            print('Review já cadastrada')
        else:
            review = input('Escreva sua review: ')
            usuario = obterUsuario(emailusuario)
            reviewUsuario = {'usuario': usuario,
                    'estabelecimento': nomeEstabelecimentoReview,
                    'review': review}
            
            listaReviews.append(reviewUsuario)

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print('Review cadastrada com sucesso')
            break

#Função de visualização de reviews
def VerReviewsUsuario(listaReviews):
    print('-' * 40)
    reviews_usuario = []
    login_usuario = obterUsuario(emailusuario)
    for review in listaReviews:
        if review['usuario'] == login_usuario:
            reviews_usuario.append(review)

    if not reviews_usuario:
        print('Nenhuma review encontrada')
    else:
        print('Reviews do usuário:')
        for review in reviews_usuario:
            print(f'Usuário: {review["usuario"]}')
            print(f'Estabelecimento: {review["estabelecimento"]}')
            print(f'Review: {review["review"]}')
            print('-' * 20)

#Função para fazer Posts apenas pra clientes
def FazerPostUsuario(listaPostsUsuario):
    while True:
        print('-' * 40)
        postUsuario = input('Escreva seu post: ')
        if any(user['post'] == postUsuario for user in listaPostsUsuario):
            print('Post já cadastrado')
        else:
            usuario = ()
            usuario = obterUsuario(emailusuario)
            postUsuario = {'usuário': usuario,
                    'post': postUsuario}
            
            listaPostsUsuario.append(postUsuario)

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print('Post cadastrado com sucesso')
            break

#Função para ver Posts
def VerPostsUsuario(listaPostsUsuario):
    print('-' * 40)
    posts_usuario = []
    login_usuario = obterUsuario(emailusuario)
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

#Função para dar nota aos estabelecimentos
def DarNota(listaNotas):
    while True:
        print('-' * 40)
        nomeEstabelecimentoNota = input('Qual é o nome do estabelecimento que você deseja dar nota? ')
        while True:
            try:
                notaEstabelecimento = int(input(f'Digite uma nota (de 0 a 5) para a acessibilidade dentro do estabelecimento {nomeEstabelecimentoNota}: ')) 
                break
            except ValueError:
                print('Digite apenas números') 
        if notaEstabelecimento <= 5:
            TipoEstabelecimento = input('Qual é o tipo do estabelecimento? ')

            Notas = {'TipodeEstabelecimento': TipoEstabelecimento,
                    'estabelecimento': nomeEstabelecimentoNota,
                    'nota': notaEstabelecimento}
            listaNotas.append(Notas)

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print('Nota cadastrada com sucesso')
            break

        else:
            print('Digite um valor válido!')
            break

#Função de cadastro de Estabelecimento
def CadastraEstabelecimento(listaEstabeelecimentos):
    while True:
        print('-' * 40)
        emailEstabelecimento = input('Cadastre seu email: ')
        if any(user['email'] == emailEstabelecimento for user in listaEstabeelecimentos):
            print('Email já cadastrado')
        else:
            nomeEstabelecimento = input('Qual é o nome do seu estabelecimento? ')
            senhaEstabelecimento = input('Cadastre sua senha: ')
            while True:
                try:
                    cnpj = int(input('Cadastre seu cnpj (Digite apenas números): '))
                    break
                except ValueError:
                    print('Digite apenas números!')

            tipoEstabelecimento = input('Tipo de estabelecimento: ')
            
            usuario = {'email': emailEstabelecimento,
                       'estabelecimento': nomeEstabelecimento,
                       'cnpj': cnpj,
                       'TipodeEstabelecimento': tipoEstabelecimento,
                       'senha': senhaEstabelecimento}
            
            listaEstabeelecimentos.append(usuario)

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print('Cadastro realizado com sucesso')

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            break

#Função de Cadastro de cliente
def CadastraUsuario(listausuarios):
        while True:
            try:
                print('-' * 40)
                emailusuario = input('Cadastre seu email: ')
                if any(user['email'] == emailusuario for user in listaUsuarios):
                    print('Email já cadastrado')
                else:
                    LoginUsuario = input('Cadastre seu login: ')
                    senhaUsuario = input('Cadastre sua senha: ')
                    while True:
                        try:    
                            cpfusuario = input('Cadastre seu cpf: ')
                            break
                        except ValueError:
                            print('Digite apenas números!')

                    usuario = {'usuario': LoginUsuario,
                            'email': emailusuario,
                                'senha': senhaUsuario,
                                'cpf': cpfusuario}
                    
                    listausuarios.append(usuario)

                    with open('data.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)

                    print('Cadastro realizado com sucesso')
                    break
            except ValueError:
                print('Valor inválido')

#Função de login para estabelecimentos
def LoginEstabelecimento(*args):
    global emailestabelecimento
    print('-' * 40)
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

#Função de login para usuários
def LoginUsuario(listaUsuarios):
    global emailusuario
    print('-' * 40)
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

#Função para obter o nome do cliente com base no email
def obterUsuario(emailusuario):
    for usuario in listaUsuarios:
        if usuario["email"] == emailusuario:
            return usuario["usuario"]

#Função para obter o nome do cliente com base no email
def obterEstabelecimento(emailestabelecimento):
    for estabelecimento in listaEstabelecimentos:
        if estabelecimento["email"] == emailestabelecimento:
            return estabelecimento["estabelecimento"]

#Função do menu principal
def main():
    while True:
        try:
            print('-' * 40)
            menu = int(input('Seja bem vindo ao Inclui+! \n Escolha uma opção: \n 1 - Cadastrar estabelecimento \n 2 - Cadastrar usuário \n 3 - Login estabelecimento \n 4 - Login usuário \n 5 - sair \n'))
            match menu:
                case 1: 
                    CadastraEstabelecimento(listaEstabelecimentos)
                case 2: 
                    CadastraUsuario(listaUsuarios)
                case 3: 
                    LoginEstabelecimento()
                case 4:
                    LoginUsuario(listaUsuarios)
                case 5:
                    break
                case other: 
                    print('Opção inválida')  
        except ValueError:
            print('Opção inválida')  

main()