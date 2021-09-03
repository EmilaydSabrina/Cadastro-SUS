import random

def exibir_menu():
    print("...MENU...")
    print("1. Listar pessoas cadastradas")
    print("2. Procurar dados de uma pessoa")
    print("3. Procurar pelo numero do sus")
    print("4. Remover pessoa")
    print("5. Cadastrar uma pessoa")
    print("6. Grava dados em arquivo") 
    print("7. Sair")
    opt = int(input("Escolha uma opção:"))
    return opt

def le_pessoas_cadastradas(nomeArquivo):
  arquivo = open(nomeArquivo, 'r')
  linhas = []
  for linha in arquivo:
      linhaLida = linha.strip().split("#")
      linhas.append(linhaLida)
  arquivo.close()
  return linhas

def gravaDadosEmArquivo(pessoas_cadastradas, nomeArquivo):
  arquivo = open(nomeArquivo,"w")
  for nome, idade, identificador, cpf, nome_pai, nome_mae, numerosus in pessoas_cadastradas:
      linha = nome+"#"+idade+"#"+identificador+"#"+cpf+"#"+nome_pai+"#"+nome_mae+"#"+numerosus +"\n"
      arquivo.write(linha)
  arquivo.close()

def listaPessoas(pessoas_cadastradas):
    for linha in pessoas_cadastradas:
      print("NOME: " ,linha[0], "/IDADE: ",linha[1], "/ID: ",linha[2], "/CPF: ",linha[3], "/NOME DA MÃE: ",linha[4], "/NOME DO PAI: ",linha[5], "/NUMERO DO SUS: ",linha[6])
      print("="*110)

def buscar(quem_procurar, pessoas_cadastradas):
  existe_pessoa = False
  for nome, idade, identificador, cpf, nome_pai, nome_mae, numerosus in pessoas_cadastradas:
    if (nome.upper() == quem_procurar.upper() or identificador.upper() == quem_procurar.upper() or idade.upper() == quem_procurar.upper() or cpf.upper() == quem_procurar.upper() or nome_pai.upper() == quem_procurar.upper() or nome_mae.upper() == quem_procurar.upper() or numerosus.upper() == quem_procurar.upper()):
      print("NOME:",nome,"/","IDADE:", idade,"/","IDENTIDADE:", identificador,"/","CPF:", cpf,"/","NOME DO PAI:", nome_pai,"/","NOME DA MÃE:", nome_mae,"/","NUMERO DO SUS:" ,numerosus)
      existe_pessoa = True
    elif (not existe_pessoa):
      print("Essa pessoa nao esta cadastrada")

                
def procura_pelo_SUS(numero_do_sus, pessoas_cadastradas):
    for nome, idade, identificador, cpf, nome_pai, nome_mae, numerosus in pessoas_cadastradas:
        if (numerosus == numero_do_sus):
            print("NOME:",nome,"/","IDADE:", idade,"/","IDENTIDADE:", identificador,"/","CPF:", cpf,"/","NOME DO PAI:", nome_pai,"/","NOME DA MÃE:", nome_mae,"/","NUMERO DO SUS:" ,numerosus)

def produz_numero_sus(random):
  for n in range(1):
    numero_aleatorio = random.randint(1,1000)
    print("SEU NOVO NUMERO DO SUS É: ",numero_aleatorio)

def remove_dados (pessoas_cadastradas):
    quem_remover = input("Digite o nome de quem você quer remover: ")
    for nome, idade, identificador, cpf, nome_pai, nome_mae, numerosus in pessoas_cadastradas:
        if (nome.upper()==quem_remover.upper()):
            pessoa_removida = [nome, idade, identificador, cpf, nome_pai, nome_mae, numerosus]
            pessoas_cadastradas.remove(pessoa_removida)


#PROGRAMA PRINCIPAL
pessoas_cadastradas = le_pessoas_cadastradas("PessoasCadastradas.txt")

acabou = False
while (not acabou):
    opcao = exibir_menu()
    if (opcao == 1):
      listaPessoas(pessoas_cadastradas)
    elif (opcao == 2):
      quem_procurar = input("Identidade ou nome a pesquisar:")
      buscar(quem_procurar, pessoas_cadastradas)
    elif(opcao == 3):
      numero_do_sus = input("Qual o numero do SUS?")
      procura_pelo_SUS(numero_do_sus, pessoas_cadastradas)
    elif(opcao == 4):
      remove_dados (pessoas_cadastradas)
    elif (opcao == 5):
        nome = input("Digite o nome da pessoa:\n")
        idade = input("Digite a idade:\n")
        identificador = input("Digite o numero da identidade:\n")
        cpf = input("Digite o número do CPF:\n")
        nome_mae = input("Digite o nome da mãe:\n")
        nome_pai = input("Digite o nome do pai:\n")
        print("Gerando número do SUS...")
        produz_numero_sus(random)
        numerosus = input("Digite o número gerado:\n")
        pessoa = [nome, idade, identificador,cpf, nome_mae, nome_pai, numerosus]
        pessoas_cadastradas.append(pessoa)
    elif (opcao ==6):
        gravaDadosEmArquivo(pessoas_cadastradas, "PessoasCadastradas.txt")
    elif (opcao ==7):
        acabou = True
print("FIM DO PROGRAMA!")






