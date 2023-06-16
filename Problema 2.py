
def main():
    codigo_del_partido = []
    nombre_del_partido = []
    siglas_del_partido = []
    votos_de_partido = []


    while True:
        codigo = int(input('Ingrese el codigo del partido: '))
        codigo_del_partido.append(codigo)
        nombre = str(input('Ingrese el nombre del partido politico: '))
        nombre_del_partido.append(nombre_del_partido)
        siglas = str(input('Ingrese las siglas del partido politico'))
        print('')
        desicion = str(input('Dese ingresar otro partido politico? S/N: '))
        if desicion == "N":
            break

    while True:
        mesa = int(input('Ingrese el numero de mesa: '))
        deapartamento = str(input('Ingrese el departamento: '))
        municipio = str(input('Ingrese el municipio: '))
        codigo = int(input('Ingrese el codigo del partido politico '))
        votos = int(input('Ingrese la cantidad exacta de votos del paritod politico'))

        for i in range(len(codigo_del_partido)):
            if votos_de_partido[i] == 0:
                votos_de_partido.append(0)
                
            if codigo == codigo_del_partido[i]:
                votost = votos + votos_de_partido[i]
                votos_de_partido.append(votost)



        print(codigo_del_partido)
        print(votos_de_partido)
        print('')
        desicion = str(input('Dese ingresar más votos? S/N: '))
        if desicion == "N":
            break

    votos_de_partido.sort()
    print(votos_de_partido)





    return

main()