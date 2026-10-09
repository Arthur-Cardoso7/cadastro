
class Pessoa:
    def __init__(self, nome, idade, cpf):
        if not nome.strip():
            raise ValueError("O nome nao pode ficar vazio.")
        if idade <= 0:
            raise ValueError("A idade deve ser maior que zero.")

        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_cpf(self):
        return self.__cpf
    
    def set_nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome nao pode ficar vazio.")
        self.__nome = nome

    def set_idade(self, idade):
        if idade <= 0:
            raise ValueError("A idade deve ser maior que zero.")
        self.__idade = idade

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def exibir(self):
        print("Nome:", self.__nome)
        print("Idade:", self.__idade)
        print("CPF:", self.__cpf)

    def apresentar(self):
        print("Sou uma pessoa.")


class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula, curso, notas=None):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self.curso = curso
        self.notas = notas if notas is not None else []

    def apresentar(self):
        print("Tipo: Aluno")

    def exibir(self):
        super().exibir()
        print("Matricula:", self.matricula)
        print("Curso:", self.curso)
        print("Notas:", self.notas)


class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, disciplina, titulacao):
        super().__init__(nome, idade, cpf)
        self.disciplina = disciplina
        self.titulacao = titulacao

    def apresentar(self):
        print("Tipo: Professor")

    def exibir(self):
        super().exibir()
        print("Disciplina:", self.disciplina)
        print("Titulacao:", self.titulacao)


# Lista que armazena todos os cadastros
pessoas = [
    Aluno("Arthur", 20, "11111111111", "A001", "Python", [8.5, 9.0]),
    Aluno("Ana", 22, "22222222222", "A002", "Java", [7.5, 8.0]),
    Aluno("Pedro", 19, "33333333333", "A003", "Banco de Dados", [9.0, 9.5]),
    Professor("Maria", 35, "44444444444",
              "Programacao", "Mestrado"),
    Professor("Carlos", 40, "55555555555",
              "Banco de Dados", "Doutorado")
]


def cadastrar_aluno():
    try:
        nome = input("Nome do aluno: ")

        if not nome.strip():
            print("Erro no cadastro: O nome nao pode ficar vazio.")
            return
        idade = int(input("Idade: "))
        cpf = input("CPF: ")
        matricula = input("Matricula: ")
        curso = input("Curso: ")

        aluno = Aluno(nome, idade, cpf, matricula, curso)
        pessoas.append(aluno)

        print("Aluno cadastrado com sucesso!")

    except ValueError as erro:
        print("Erro no cadastro:", erro)


def cadastrar_professor():
    try:
        nome = input("Nome do professor: ")
        idade = int(input("Idade: "))
        cpf = input("CPF: ")
        disciplina = input("Disciplina: ")
        titulacao = input("Titulacao: ")

        professor = Professor(
            nome, idade, cpf, disciplina, titulacao
        )
        pessoas.append(professor)

        print("Professor cadastrado com sucesso!")

    except ValueError as erro:
        print("Erro no cadastro:", erro)


def listar_pessoas():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return

    print("\n=== LISTA DE PESSOAS ===")

    for pessoa in pessoas:
        pessoa.apresentar()
        pessoa.exibir()
        print("-------------------")


def buscar_pessoa():
    nome_busca = input("Digite o nome para buscar: ").strip().casefold()

    if not nome_busca:
        print("Digite um nome para realizar a busca.")
        return

    encontrados = [
        pessoa for pessoa in pessoas
        if nome_busca in pessoa.get_nome().casefold()
    ]

    if encontrados:
        print("\n=== RESULTADO DA BUSCA ===")
        for pessoa in encontrados:
            pessoa.apresentar()
            pessoa.exibir()
            print("-------------------")
    else:
        print("Pessoa nao encontrada.")

def menu():
    while True:
        print("\n===== SISTEMA DE CADASTRO =====")
        print("1 - Cadastrar aluno")
        print("2 - Cadastrar professor")
        print("3 - Listar pessoas")
        print("4 - Buscar pessoa por nome")
        print("5 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_professor()
        elif opcao == "3":
            listar_pessoas()
        elif opcao == "4":
            buscar_pessoa()
        elif opcao == "5":
            print("Encerrando o sistema. Ate mais!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


menu()