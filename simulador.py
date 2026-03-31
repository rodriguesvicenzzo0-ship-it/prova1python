continuar = "sim"

while continuar == "sim":
    continuar = input("Voce deseja continuar? (sim/não): ")

    if continuar == "sim":
        print("voce ainda esta no jogo! ")
    elif continuar == "não":
        print("Game over!")
    else:
        print("Opção invalida. Digite sim ou não. ")
        continuar = "sim"