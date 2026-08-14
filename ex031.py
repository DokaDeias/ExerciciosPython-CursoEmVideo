viagem = float(input("Quantos Kms voce viajou?: "))

if viagem <= 200:
    calc1 = viagem * 0.50
    print("Você ira pagar R${:.2f}".format(calc1))
else:
    print("Você ira pagar R${:.2f}".format(viagem * 0.45))