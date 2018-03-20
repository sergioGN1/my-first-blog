def hola(name):
    if name != "":
        print("Hola " + name)
    else:
        print("No tienes nombre??????")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hola(name)


for i in range(1, 6):
    hola(girls[i])
