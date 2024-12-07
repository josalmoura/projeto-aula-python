print('Bem vindo a lista de contatos do Jonathan Silva Moura')
#Lista de armanezamento de contatos e ig global
lista_contatos = []
id_global = 5031376

def cadastrar_contato(id): #Aqui atribui as informações do contato
  print('='*58)
  print('*'*16, 'MENU CADASTROR CONTATOS', '*'*17)
  print('='*58)
  print(f'Por favor preencha o cadastro do novo contato: ')
  print(f"ID:  {id}")
  nome= input('Nome: ')
  setor = input('Profissão/Função/setor: ')
  telefone = input('Telefone: ')
  contato = {'id': id, 'nome': nome, 'setor': setor, 'Telefone': telefone}      
  lista_contatos.append(contato.copy())

def consultar_contatos(): # aquiserá solicitadon as informações atribiudas acima
    while True:
      print('='*58)
      print('*'*16, 'MENU CONSULTAR CONTATOS', '*'*17)
      print('='*58)
      print('1 - Consultar todos: ')
      print('2 - Consultar por id: ')
      print('3 - Consultar por setor: ')
      print('4 - Retornar ao menu: ')
      print('-'*58)
      opcao = int(input("Escolha uma opção: "))
      if opcao == 1:
        for LC in lista_contatos:
          print(f'\n{LC}') 
      elif opcao == 2:
        id_consulta = int(input('Entre com o Id do contato:'))
        identificado = False
        for LC in lista_contatos:
          if LC['id'] == id_consulta:
            print(LC)
            identificado = True
            break
        if not identificado:
            print('id inválido')
      elif opcao == 3:
        setor_consulta = input("Digite o setor dos contatos: ")
        identificados = [LC for LC in lista_contatos if LC['setor'] == setor_consulta]
        if identificados:
          for LC in identificados:
            print(LC)
            break
        else:
            print('Contato não encontrado! ')
      elif opcao == 4:
        return
      else:
        print('Opção invalida!')

def remover_contato(): #contatp será deletado/excluído da lista
  while True:
    id_remover = int(input('Entre com o id do contato que deseja remover: '))
    identificado = False
    for LC in lista_contatos:
      if LC['id'] == id_remover:
        lista_contatos.remove(LC)
        print('Contato removido com sucesso!')
        identificado = True
        break
    if not identificado:
      print('id iválido!')
    else:
      break

while True: #menu inicial para atribuir/ extrair/ excluir contatos
  print('='*58)
  print('*'*21, 'MENU PRINCIPAL', '*'*21)
  print('='*58)
  print('1 - Cadastrar contato')
  print('2 - Consultar contato')
  print('3 - Remover contato')
  print('4 - Finalizar')
  print('-'*58)
  opcao = int(input('Escolha uma opção: '))
  match opcao:
    case 1:
      id_global += 1
      cadastrar_contato(id_global)
    case 2:
      consultar_contatos()
    case 3:
       remover_contato()
    case 4:
      print('PROGRAMA FINALIZADO! ')
      break
    case _:
      print('Opção inválida!')
      continue


