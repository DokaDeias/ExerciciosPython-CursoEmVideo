l = (float(input("Qual a largura da parede? ")))
a = (float(input("Qual a altura da parede? ")))

d = l * a

print("Sua parede tem a dimensão de", l,"x",a,"e sua area é de {}m²".format(d))
print("Para pintar sua parede, você precisará de {}l de tinta".format(d/2))