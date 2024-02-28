
def gerador_nome_banda():
    """
    Gerador de Nome de Bandas
    =========================

    Método que gera o nome de uma banda com base nas respostas do usuário.

    :return: None

    Método responsável por solicitar ao usuário o nome da cidade onde nasceu e o nome do seu pet.
    Em seguida, concatena essas informações para formar o nome da banda e imprime na tela.

    Exemplo de uso:
    ---------------
        gerador_nome_banda()

    Saídas esperadas:
    -----------------
        Bem vindo ao gerador de nome de bandas!
        Qual o nome da cidade que você nasceu?
        [Aguarda entrada do usuário]
        Qual o nome do seu pet?
        [Aguarda entrada do usuário]
        O nome da sua banda será: [Nome Da Cidade] [Nome Do Pet]
    """
    print("Bem vindo ao gerador de nome de bandas!")

    cid = input("Qual o nome da cidade que você nasceu?\n")
    pet = input("Qual o nome do seu pet?\n")

    print(f"O nome da sua banda será: {cid} {pet}\n")