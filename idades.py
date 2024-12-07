print("Seja bem vinso ao sistema do Jonathan Silva Moura")

valorBase = float(input("Informe o valor base do plano: "))
idade = int(input("Informe a idade do cliente: "))

#Com a idade e o valor base  cedido pelo cliente terá o acréscimo do valor mensal#
valorMnesal = 0
if idade >= 0 and idade < 19:
    valorMensal = valorBase * 100/100
    #sem acréscimo#

elif idade >= 19 and idade < 29:
    valorMensal = valorBase * 150/100
    #acréscimo de 1.5 #

elif idade >= 29 and idade < 39:
    valorMensal = valorBase * 225/100
    # acréscimo de 2.25 #

elif idade >= 39 and idade < 49:
    valorMensal = valorBase * 240/100
    # acréscimo de 2.4 #

elif idade >= 49 and idade < 59:
    valorMensal = valorBase + 350/100
    # acréscimo de 3.5 #
else:
    valorMensal = valorBase * 600/100
    # acréscimo de 6 #
print()
print(f" Clinete com a idade maior ou igual a {idade} anos pagara {valorMensal:.2f}R$")
print()
print("Jonathan Silva Moura agradece pela preferência!")