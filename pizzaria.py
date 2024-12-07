print('-' * 6,'bem-vindo a pizzaria do Jonathan Silva Moura', '-' * 6)
print('-' * 21, 'Cardápio', '-' * 27)
print('='* 58)  #Menu inicial
print(' ' * 4, '| Tamanho | Pizza Salgada(Ps) | Pizza doce(Pd) |', ' ' * 4)
print(' ' * 4, '|    P    |     R$ 30.00      |    R$ 34.00    |', ' ' * 4)
print(' ' * 4, '|    M    |     R$ 45.00      |    R$ 48.00    |', ' ' * 4)
print(' ' * 4, '|    G    |     R$ 60.00      |    R$ 66.00    |', ' ' * 4)
print('='* 58)
desejo = str
valorTotal: float = 0

pizza = str(input("Entre com o sabor desejado (PS/PD): ")).upper()

while pizza != "PS" and pizza != "PD":
  print("Sabor inválido. tente novamente!")
  pizza = str(input("Entre com o sabor desejado (PS/PD): ")).upper()
  continue
#Area do site para pedidos, podendo ser letras maiúsculas e minúsculas, sem dar erro.
while pizza == "PS" or desejo == "S":
  tamanho = str(input("Qual o tamanho da pizza deseja: P/M/G  ")).upper()
  if tamanho == "P":
    print("Você pediu uma pizza salgada tamanho pequena R$ 30.00")
    valorTotal = valorTotal + 30.00
    break
  elif tamanho == "M":
    print("Você pediu uma pizza salgada tamanho média R$ 45.00")
    valorTotal = valorTotal + 45.00
    break
  elif tamanho == "G":
    print("Você pediu uma pizza salgada tamanho grande R$ 60.00")
    valorTotal = valorTotal + 60.00
    break
  else:
    print("Tamanho inválido. Tente novamnete!")
    print()
    continue
desejo = str(input("Deseja adicionar mais um pedido? (S/N)  ")).upper()
print()
while desejo == "S":
 pizza = str(input("Entre com o sabor desejado (PS/PD): ")).upper()
 break
while pizza == "PD":
  tamanho = str(input("Qual o tamanho da pizza deseja: P/M/G  ")).upper()
  if tamanho == "P":
    print("Você pediu uma pizza doce tamanho pequena R$ 34.00")
    valorTotal = valorTotal + 34.00
    break
  elif tamanho == "M":
    print("Você pediu uma pizza doce tamanho média R$ 48.00")
    valorTotal = valorTotal + 48.00
    break
  elif tamanho == "G":
    print("Você pediu uma pizza doce tamanho grande R$ 66.00")
    valorTotal = valorTotal + 66.00
    break
  else:
    print("Tamanho inválido. Tente novamente!")
    print()
    continue
print() 
desejo = str(input("Deseja mais alguma coisa? (S/N)  ")).upper()
print('='* 58)
while desejo == "N" :#pedido só será finalizado quando responder não(N/n)
   print(f"O valor total a ser pago: R$ {valorTotal:.2f}")
   break 

#Programa neccessita de melhorar
#principalmente no segundo pedido da pizza
# tendo continuidade somente se for PD
#não podendo ser PS ou erros.