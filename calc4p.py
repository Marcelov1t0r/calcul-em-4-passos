x=int(input("Digite um número: "))
y=int(input("Digite outro número: "))

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print("O resultado é:",x+y)
elif opcao == 2:
    print("O resultado é:",x-y)
elif opcao == 3:
    print("O resultado é:",x*y)
elif opcao == 4:
    if y!=0 :
        print("O resultado é:",x/y)
    else:
        print("Impossível divisão por 0!")