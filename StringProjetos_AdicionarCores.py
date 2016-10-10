def AdicionarCores(cores):
    cor = input("Qual é a cor que deseja adicionar :")
    cores.append(cor)

def ListarCores(cor):
    for cor in cores:
        print(cor)
