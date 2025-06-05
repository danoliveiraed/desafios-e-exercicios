
arquivo_path_seg = '/home/daniel/PycharmProjects/Meus Projetos/arquivos/dan_pass_seg.txt'

def cadastro_usuario(seg_usuario, seg_senha, usuarios_cadastrados):

    if seg_usuario in usuarios_cadastrados:
        print('Nome de usuário já cadastrado!')
    else:
        #Se o usuário não existe, faz o cadastro
        with open(arquivo_path_seg, 'a') as arquivo:
            arquivo.write(f'\n{seg_usuario},{seg_senha}')
            print(f'Novo usuário {seg_usuario} cadastrado com senha {seg_senha}')

def seguranca():
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
        cadastrar = input('Senha não encontrada! \ndegite (n) para cadastrar Nova Senha \nDigite (s) para Sair:  ')
        if cadastrar == 'n':
            cadastro_usuario(seg_usuario, seg_senha, usuarios_cadastrados)

    return seg_usuario, seg_senha, usuarios_cadastrados

seguranca()