while True:
    numero = int(input("Digite um número PAR: "))
    if numero % 2 == 0 and numero >= 0:
        print('""P-A-R!!""')
        break
    else:
        print("tente novamente")