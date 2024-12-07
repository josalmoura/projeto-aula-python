print("-"*6, "Bem-vindo a madereira do Jonathan Silva Moura","-"*5)

def escolha_tipo():#Menu entrada so site
  while True:
     print("="*58)
     print("-"*10, "Entre com o tipo de madeira desejado", "-"*10)
     print(" "*18, "PIN - Tora de Pinho ", " "*18)
     print(" "*18, "PER - Tora de Peroba", " "*18)
     print(" "*18, "MOG - Tora de Mogno ", " "*18)
     print(" "*18, "IPE - Tora de Ipê   ", " "*18)
     print(" "*18, "IMB - Tora de Imbuia", " "*18)
     print("="*58)
     valorMadeira = input(">> ").upper()#Entrada de qual madeira deseja.
     match valorMadeira:   #Podendo ser escrita em letras maiúsculas ou minúsculas.
        case "PIN":
         return 150.40
        case "PER":
         return 170.20
        case "MOG":
         return 190.90
        case "IPE":
         return 210.10
        case "IMB":
         return 220.70
        case _:
         print("Escolha inválida, entre com o modelo novamente.")
         continue

def qtd_toras():#Entrada dos pedido de tora.
  while True:
    try:
      qtdToras = int(input("Informe quantas toras deseja: "))
      if qtdToras > 2000:
        print("Não aceitamos pedidos acima de 2000 toras.")
      else:
        if qtdToras < 100:
          desconto = 0
        elif qtdToras >= 100 and qtdToras < 500:
          desconto = 4/100
        elif qtdToras >= 500 and qtdToras < 1000:
          desconto = 9/100
        elif qtdToras >= 1000 and qtdToras <= 2000:
          desconto = 16/100
        return qtdToras*(1-desconto)
    except ValueError:
      print("Por favor, entre com a quantidade novamente")

def transporte():#Escolha tipo trasporte
  while True:
    print("Escolha o tipo de transporte: ")
    print(" 1 - Transporte Rodoviário  - R$ 1000.00\n 2 - Transporte Ferroviário - R$ 2000.00\n 3 - Transporte Hidroviário - R$ 2500.00")
    frete = int(input(">> "))
    match frete:
      case 1:
        return 1000
      case 2:
        return 2000
      case 3:
        return 2500
      case _:
        print("Opção inválida, tente novamente!")
        continue

valorMadeira = escolha_tipo()
qtdToras = qtd_toras()
frete = transporte()
total = (valorMadeira * qtdToras)+ frete
def main():#Valor total no main principal.
  print(f"Total: {total:.2f}")

if __name__ == "__main__":
 main()