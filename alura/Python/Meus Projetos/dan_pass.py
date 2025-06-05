import random


class GerenciadorSenhas:
    """
    Classe responsável por gerenciar senhas de usuários e registros.
    Permite gerar senhas, gravar em arquivo, buscar e apagar registros.
    """
    
    def __init__(self, arquivo_path):
        """
        Inicializa o gerenciador com o caminho do arquivo de registros.
        :param arquivo_path: Caminho do arquivo onde as senhas são armazenadas.
        """
        self.arquivo_path = arquivo_path

    def obtem_dados(self):
        """
        Obtém os dados de registro do usuário e senha. Caso o campo de senha seja deixado em branco,
        uma senha aleatória será gerada e salva automaticamente.
        :return: Tupla contendo (registro, usuário, senha)
        """
        registro = input('Nome do registro: ').title().strip()
        usuario = input('Nome de usuário: ').strip()
        senha = input('Digite a senha (deixe em branco para gerar uma senha aleatória): ').strip()
        categoria = 'geral'  # Categoria não utilizada, mas pode ser estendida futuramente.

        if senha == '':
            senha = self.gerar_senha()
            self.grava_senha(registro, usuario, senha)
        return registro, usuario, senha

    def gerar_senha(self):
        """
        Gera uma senha aleatória baseada na escolha do usuário (alfanumérica ou apenas numérica).
        :return: Senha gerada como string.
        """
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

    def grava_senha(self, registro, usuario, senha):
        """
        Grava a senha no arquivo, evitando duplicatas de registro+usuário.
        :param registro: Nome do serviço ou site.
        :param usuario: Nome de usuário associado.
        :param senha: Senha gerada ou informada.
        """
        with open(self.arquivo_path, 'r') as arquivo:
            for linha in arquivo:
                v_registros = linha.split(',')
                if registro == v_registros[0] and usuario == v_registros[1]:
                    print('Registro existente')
                    return

        with open(self.arquivo_path, 'a') as arquivo:
            arquivo.write(f'\n{registro},{usuario},{senha}')
            print(f'Novo registro gravado como: registro: {registro} - usuário: {usuario} - senha: {senha}')

    def apaga_reg(self):
        """
        Apaga um registro específico com base no nome do registro e do usuário.
        """
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

    def busca_senha(self):
        """
        Busca e exibe a senha associada a um registro informado pelo usuário.
        """
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


class Seguranca:
    """
    Classe responsável por controlar o acesso ao gerenciador de senhas.
    Valida usuários e permite cadastrar novos acessos.
    """
    
    def __init__(self, arquivo_path_seg):
        """
        Inicializa com o caminho para o arquivo de segurança (usuários autorizados).
        :param arquivo_path_seg: Caminho do arquivo com usuários e senhas autorizadas.
        """
        self.arquivo_path_seg = arquivo_path_seg

    def seguranca(self):
        """
        Verifica se o usuário está autorizado. Caso não esteja, permite cadastro.
        :return: Tupla com (usuário, senha, conjunto de usuários cadastrados)
        """
        seg_usuario = input('Usuario dan_pass: ').lower().strip()
        seg_senha = input('Senha dan_pass: ').strip()

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
            cadastrar = input('Senha não encontrada! \ndigite (n) para cadastrar Nova Senha \nDigite (s) para Sair:  ').lower().strip()
            if cadastrar == 'n':
                self.cadastro_usuario(seg_usuario, seg_senha, usuarios_cadastrados)
            elif cadastrar != 'n':
                exit()

        return seg_usuario, seg_senha, usuarios_cadastrados

    def cadastro_usuario(self, seg_usuario, seg_senha, usuarios_cadastrados):
        """
        Cadastra novo usuário e senha no arquivo de segurança.
        :param seg_usuario: Novo nome de usuário.
        :param seg_senha: Senha do novo usuário.
        :param usuarios_cadastrados: Conjunto de usuários já registrados.
        """
        if seg_usuario in usuarios_cadastrados:
            print('Nome de usuário já cadastrado!')
        else:
            with open(arquivo_path_seg, 'a') as arquivo:
                arquivo.write(f'\n{seg_usuario},{seg_senha}')
                print(f'Novo usuário {seg_usuario} cadastrado com senha {seg_senha}')


# Caminhos dos arquivos onde os dados são armazenados
arquivo_path = '/home/daniel/PycharmProjects/Meus Projetos/arquivos/dan_pass.txt'
arquivo_path_seg = '/home/daniel/PycharmProjects/Meus Projetos/arquivos/dan_pass_seg.txt'

# Instancia as classes de segurança e gerenciador de senhas
seguranca = Seguranca(arquivo_path_seg)
gerenciador = GerenciadorSenhas(arquivo_path)

# Executa verificação de segurança antes de liberar o acesso
seg_usuario, seg_senha, usuarios_cadastrados = seguranca.seguranca()

# Loop principal do programa
while True:
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
