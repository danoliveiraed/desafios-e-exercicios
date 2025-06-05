import random


class GerenciadorSenhas:
    def __init__(self, arquivo_path):
        self.arquivo_path = arquivo_path

    # Função para obter dados de registro, usuário e senha
    def obtem_dados(self):

        registro = input('Nome do registro: ').title().strip()
        usuario = input('Nome de usuário: ').strip()
        senha = input('Digite a senha (deixe em branco para gerar uma senha aleatória): ').strip()
        categoria = 'geral'

        if senha == '':
            senha = self.gerar_senha()
            self.grava_senha(registro, usuario, senha)
        return registro, usuario, senha

    # Função para gerar uma senha aleatória
    def gerar_senha(self):
        senha = ''
        tipo = int(input('Para senha alfanumerica (1) \nPara senha numérica (2): '))
        length = int(input('Quantos caracteres terá a senha: '))
        chars = 'bacdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%.&*()0123456789'
        numeros = '0123456789'

        if tipo == 1:
            for _ in range(length):
                senha += random.choice(chars)
        elif tipo == 2:
            for _ in range(length):
                senha += random.choice(numeros)
        return senha

    # Função para gravar um registro no arquivo
    def grava_senha(self, registro, usuario, senha):
        with open(self.arquivo_path, 'r') as arquivo:
            for linha in arquivo:
                v_registros = linha.split(',')
                if registro == v_registros[0] and usuario == v_registros[1]:
                    print('Registro existente')
                    return

        with open(self.arquivo_path, 'a') as arquivo:
            arquivo.write(f'\n{registro},{usuario},{senha}')
            print(f'Novo registro gravado como: registro: {registro} - usuário: {usuario} - senha: {senha}')

    # Função para apagar um registro ou usuário
    def apaga_reg(self):
        print('Você está apagando um registro ou usuário... ')
        reg_apaga = input('Nome do registro: ').title().strip()
        usu_apaga = input('Nome de usuário: ').strip()

        with open(self.arquivo_path, 'r+') as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)

            for linha in linhas:
                v_registros = linha.split(',')
                if reg_apaga != v_registros[0] or usu_apaga != v_registros[1]:
                    arquivo.write(linha)
            arquivo.truncate()
            print(f'Você apagou o registro: {reg_apaga} ou o usuário: {usu_apaga}')

    # Função para buscar uma senha com base no registro
    def busca_senha(self):
        registro = input('Nome do registro: ').title().strip()
        busca = False

        with open(self.arquivo_path, 'r') as arquivo:
            for linha in arquivo:
                v_registros = linha.split(',')
                if registro == v_registros[0]:
                    usuario = v_registros[1]
                    senha = v_registros[2]
                    busca = True
                    print(f'Para o registro {registro} o usuário é: {usuario} e a senha é: {senha}')
        if busca == False:
            print('Registro não encontrado')

class Seguranca: #verifica quem pode acessar o programa
    def __init__(self, arquivo_path_seg):
        self.arquivo_path_seg = arquivo_path_seg

    def seguranca(self):
        seg_usuario = input('Usuario dan_pass: ').lower().strip()
        seg_senha = input('Senha dan_pass: ').strip()

        # Verifica se  o usuário já está cadastrado
        usuarios_cadastrados = set()
        senhas_cadastradas = set()
        with open(arquivo_path_seg, 'r') as arquivo:
            for linha in arquivo:
                cad_usu = linha.split(',')
                usuarios_cadastrados.add(cad_usu[0])
                senhas_cadastradas.add(cad_usu[1])
        if seg_usuario in usuarios_cadastrados and seg_senha in senhas_cadastradas:
            print('chamo o programa dan_pass')
        else:
            cadastrar = input('Senha não encontrada! \ndegite (n) para cadastrar Nova Senha \nDigite (s) para Sair:  ').lower().strip()
            if cadastrar == 'n':
                self.cadastro_usuario(seg_usuario, seg_senha, usuarios_cadastrados)
            elif cadastrar != 'n':
                exit()


        return seg_usuario, seg_senha, usuarios_cadastrados

    def cadastro_usuario(self, seg_usuario, seg_senha, usuarios_cadastrados):

        if seg_usuario in usuarios_cadastrados:
            print('Nome de usuário já cadastrado!')
        else:
            # Se o usuário não existe, faz o cadastro
            with open(arquivo_path_seg, 'a') as arquivo:
                arquivo.write(f'\n{seg_usuario},{seg_senha}')
                print(f'Novo usuário {seg_usuario} cadastrado com senha {seg_senha}')



# Define o caminho único do arquivo
arquivo_path = '/home/daniel/PycharmProjects/Meus Projetos/arquivos/dan_pass.txt'
arquivo_path_seg = '/home/daniel/PycharmProjects/Meus Projetos/arquivos/dan_pass_seg.txt'

seguranca = Seguranca(arquivo_path_seg)
# Cria uma instância do GerenciadorSenhas
gerenciador = GerenciadorSenhas(arquivo_path)

seg_usuario, seg_senha, usuarios_cadastrados = seguranca.seguranca()
while True:
    # Menu de escolha
    print('Bem-vindo ao gerador de senhas dan_pass')
    escolha = input('Para buscar (b) \nPara nova senha (n) \nPara apagar (a)  \nPara sair (s): ').lower()

    if escolha == 'n':
        registro, usuario, senha = gerenciador.obtem_dados()
    elif escolha == 'a':
        gerenciador.apaga_reg()
    elif escolha == 'b':
        gerenciador.busca_senha()
    elif escolha == 's':
                break