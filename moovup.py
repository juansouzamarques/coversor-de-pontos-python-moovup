import json

ARQUIVO = "usuarios.json"
VALOR_POR_PONTO = 0.0091
postagens = {
    "foto": 5,
    "video": 15,
    "story": 3,
    "reels": 20
}
usuarios = []


def salvar_usuarios():
    """Salva a lista de usuarios no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


def carregar_usuarios():
    """Carrega os usuarios. Se o arquivo nao existir, inicia uma lista vazia."""
    global usuarios
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = []


def buscar_usuario(email):
    """Retorna o usuario com o e-mail informado, ou None."""
    for usuario in usuarios:
        if usuario["email"] == email.lower():
            return usuario
    return None


def ler_numero(mensagem, minimo, maximo):
    """Le um numero inteiro dentro de um intervalo."""
    while True:
        try:
            numero = int(input(mensagem))
            if minimo <= numero <= maximo:
                return numero
        except ValueError:
            pass
        print("Opcao invalida.")


def cadastrar_usuario():
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip().lower()

    if not nome or "@" not in email:
        print("Nome ou e-mail invalido.")
    elif buscar_usuario(email):
        print("Este e-mail ja esta cadastrado.")
    else:
        usuarios.append({"nome": nome, "email": email, "pontos": 0, "historico": []})
        salvar_usuarios()
        print("Usuario cadastrado com sucesso!")


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuario cadastrado.")
    for indice, usuario in enumerate(usuarios, start=1):
        print(f"{indice} - {usuario['nome']} | {usuario['email']} | {usuario['pontos']} pontos")


def consultar_usuario():
    usuario = buscar_usuario(input("E-mail: ").strip())
    if usuario:
        print(f"Nome: {usuario['nome']}")
        print(f"E-mail: {usuario['email']}")
        print(f"Pontos: {usuario['pontos']}")
    else:
        print("Usuario nao encontrado.")


def editar_usuario():
    usuario = buscar_usuario(input("E-mail atual: ").strip())
    if not usuario:
        print("Usuario nao encontrado.")
        return

    nome = input(f"Novo nome [{usuario['nome']}]: ").strip()
    email = input(f"Novo e-mail [{usuario['email']}]: ").strip().lower()

    if nome:
        usuario["nome"] = nome
    if email:
        outro_usuario = buscar_usuario(email)
        if outro_usuario and outro_usuario != usuario:
            print("Este e-mail ja esta cadastrado.")
            return
        usuario["email"] = email

    salvar_usuarios()
    print("Usuario atualizado!")


def excluir_usuario():
    usuario = buscar_usuario(input("E-mail: ").strip())
    if not usuario:
        print("Usuario nao encontrado.")
        return

    confirmar = input(f"Excluir {usuario['nome']}? (S/N): ").strip().upper()
    if confirmar == "S":
        usuarios.remove(usuario)
        salvar_usuarios()
        print("Usuario excluido!")
    else:
        print("Exclusao cancelada.")


def registrar_postagem():
    usuario = buscar_usuario(input("Seu e-mail: ").strip())
    if not usuario:
        print("Usuario nao encontrado.")
        return

    tipos = list(postagens)
    for indice, tipo in enumerate(tipos, start=1):
        print(f"{indice} - {tipo} (+{postagens[tipo]} pontos)")

    tipo = tipos[ler_numero("Escolha o tipo: ", 1, len(tipos)) - 1]
    quantidade = ler_numero("Quantidade (1 a 5): ", 1, 5)
    pontos_ganhos = postagens[tipo] * quantidade

    usuario["pontos"] += pontos_ganhos
    usuario["historico"].append(f"{quantidade}x {tipo}: +{pontos_ganhos} pontos")
    salvar_usuarios()
    print(f"Voce ganhou {pontos_ganhos} pontos!")


def converter_pontos():
    try:
        usuario = buscar_usuario(input("Seu e-mail: ").strip())
        if not usuario:
            print("Usuario nao encontrado.")
            return
        if usuario["pontos"] == 0:
            print("Voce nao possui pontos para converter.")
            return

        print(f"Cada ponto vale R$ {VALOR_POR_PONTO:.4f}.")
        usar = int(input("Quantos pontos deseja converter? "))
        if usar < 1 or usar > usuario["pontos"]:
            print("Quantidade de pontos invalida.")
            return

        valor = usar * VALOR_POR_PONTO
        usuario["pontos"] -= usar
        usuario["historico"].append(f"Conversao: -{usar} pontos = R$ {valor:.2f}")
        salvar_usuarios()
        print(f"Valor estimado: R$ {valor:.2f}")
    except ValueError:
        print("Digite apenas numeros para a quantidade de pontos.")
    except OSError:
        print("Nao foi possivel salvar a conversao.")


def consultar_saldo():
    usuario = buscar_usuario(input("Seu e-mail: ").strip())
    if not usuario:
        print("Usuario nao encontrado.")
        return

    valor = usuario["pontos"] * VALOR_POR_PONTO
    print(f"\nNome: {usuario['nome']}")
    print(f"Pontos: {usuario['pontos']}")
    print(f"Valor estimado: R$ {valor:.2f}")
    print("Historico:")
    for item in usuario["historico"]:
        print("-", item)


def menu_usuarios():
    while True:
        print("\n1 - Cadastrar | 2 - Listar | 3 - Consultar")
        print("4 - Editar | 5 - Excluir | 0 - Voltar")
        opcao = input("Opcao: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            consultar_usuario()
        elif opcao == "4":
            editar_usuario()
        elif opcao == "5":
            excluir_usuario()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


def menu():
    while True:
        print("\n===== SOUL UP =====")
        print("1 - Usuarios")
        print("2 - Registrar postagem")
        print("3 - Converter pontos")
        print("4 - Consultar saldo")
        print("0 - Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            menu_usuarios()
        elif opcao == "2":
            registrar_postagem()
        elif opcao == "3":
            converter_pontos()
        elif opcao == "4":
            consultar_saldo()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")



carregar_usuarios()
menu()