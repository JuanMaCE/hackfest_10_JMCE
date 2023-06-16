
def generador_de_espacios():
    for x in range(0, 10):
        print(' ')
    return


def comprobar_mayoria_de_edad(edad):
    mayor_de_edad = 0

    if int(edad[4]) < 2:
        mayor_de_edad = 1
        return mayor_de_edad

    elif int(edad[4]) >= 2:
        if int(edad[7]) < 5:
            mayor_de_edad = 1
            return mayor_de_edad
        elif int(edad[7]) == 5:

            if int(edad[3]) <= 6:
                if int(edad[1]) <= 6:
                    mayor_de_edad = 1
                    return mayor_de_edad
                else:
                    mayor_de_edad = 0
                    return mayor_de_edad
            else:
                mayor_de_edad = 0
                return mayor_de_edad
        else:
            mayor_de_edad = 0
            return mayor_de_edad
    else:
        mayor_de_edad = 0
        return mayor_de_edad


def main():
    print('¿Donde votar las siguientes elecciones generales? ')
    print('Ingrese su fecha de nacimiento de la siguiente forma: ')
    fecha_de_nacimiento = str(input('DDMMAAAA: '))
    mayor_de_edad = comprobar_mayoria_de_edad(fecha_de_nacimiento)
    if  mayor_de_edad == 0:
        print('Aún no puede votar :) ')
    elif mayor_de_edad == 1:
        generador_de_espacios()
        dpi = str(input('Ingrese su numero de CUI del documento personal de identificacion DPI: '))
        # mesa de trabajo
        mesa = " "
        centro_de_votacion = ' '

        for i in range(len(dpi)):
            if i <= 3:
                mesa += dpi[i]
            if (i > 3) and (i <= 8):
                centro_de_votacion += dpi[i]
        print('Usted debe votar en la mesa: ', mesa)
        print('Su centro de votacion es : ', centro_de_votacion)
    # departamentos:
        codigo_departamentos = dpi[9] + dpi[10]
        codigo_municipio = dpi[11] + dpi[12]
        departamento = ""
        municipio = " "



        if codigo_departamentos == '01':
            departamento = "Guatemala"
            if codigo_municipio == "01":
                municipio = "Municipio de Guatemala"
            if codigo_municipio == "02":
                municipio = "Santa Catarina Pinula "
            if codigo_municipio == "03":
                municipio = "San José Pinula "
            if codigo_municipio == "04":
                municipio = "San José del Golfo"
            if codigo_municipio == "05":
                municipio = "Palencia"

        if codigo_departamentos == '02':
            departamento = "El Progreso"
            if codigo_municipio == "01":
                municipio = "Guastatoya"
            if codigo_municipio == "02":
                municipio = "Morazán "
            if codigo_municipio == "03":
                municipio = "San Agustín Acasaguastlán "
            if codigo_municipio == "04":
                municipio = "San Cristobal Acasaguastlán "
            if codigo_municipio == "05":
                municipio = "El Jícaro "

        if codigo_departamentos == '03':
            departamento = "sacatepequez"

            if codigo_municipio == "01":
                municipio = "Antigua Guatemala"
            if codigo_municipio == "02":
                municipio = "Jocotenango  "
            if codigo_municipio == "03":
                municipio = "Pastores "
            if codigo_municipio == "04":
                municipio = "Sumpango "
            if codigo_municipio == "05":
                municipio = "Santo Domingo Xenacoj"

        if codigo_departamentos == '04':
            departamento = " CHIMALTENANGO "

            if codigo_municipio == "01":
                municipio = "Chimaltenango"
            if codigo_municipio == "02":
                municipio = "San José Poaquil  "
            if codigo_municipio == "03":
                municipio = "San MartÍn Jilotepeque "
            if codigo_municipio == "04":
                municipio = "Comalapa "
            if codigo_municipio == "05":
                municipio = "Santa Apolonia"

        if codigo_departamentos == '05':
            departamento = " ESCUINTLA  "

            if codigo_municipio == "01":
                municipio = "Escuintla"
            if codigo_municipio == "02":
                municipio = "Santa Lucía Cotzumalguapa   "
            if codigo_municipio == "03":
                municipio = "La Democracia  "
            if codigo_municipio == "04":
                municipio = "Siquinala "
            if codigo_municipio == "05":
                municipio = "Masagua"

        if codigo_departamentos == '06':
            departamento = "  SANTA ROSA  "

            if codigo_municipio == "01":
                municipio = "Cuilapa"
            if codigo_municipio == "02":
                municipio = "Barberena "
            if codigo_municipio == "03":
                municipio = "Santa Rosa De Lima  "
            if codigo_municipio == "04":
                municipio = "Casillas "
            if codigo_municipio == "05":
                municipio = "San Rafael Las Flores"

        if codigo_departamentos == '07':
            departamento = " SOLOLÁ  "

            if codigo_municipio == "01":
                municipio = "SOLOLÁ "
            if codigo_municipio == "02":
                municipio = "San José Chacayá "
            if codigo_municipio == "03":
                municipio = "Santa María Visitación"
            if codigo_municipio == "04":
                municipio = "Santa Lucía Utatlan "
            if codigo_municipio == "05":
                municipio = "Nahuala"

        if codigo_departamentos == '08':
            departamento = " TOTONICAPAN  "

            if codigo_municipio == "01":
                municipio = "TOTONICAPAN "
            if codigo_municipio == "02":
                municipio = "San Cristóbal Totonicapan "
            if codigo_municipio == "03":
                municipio = "San Francisco El Alto "
            if codigo_municipio == "04":
                municipio = "San Andrés Xecul "
            if codigo_municipio == "05":
                municipio = "Momostenango"

        if codigo_departamentos == '09':
            departamento = " QUETZALTENANGO  "

            if codigo_municipio == "01":
                municipio = "QUETZALTENANGO "
            if codigo_municipio == "02":
                municipio = "Salcajá"
            if codigo_municipio == "03":
                municipio = "Olintepeque "
            if codigo_municipio == "04":
                municipio = "San Carlos Sija  "
            if codigo_municipio == "05":
                municipio = "Sibilia"

        if codigo_departamentos == '10':
            departamento = " SUCHITEPÉQUEZ  "

            if codigo_municipio == "01":
                municipio = "Mazatenango "
            if codigo_municipio == "02":
                municipio = "Cuyotenango"
            if codigo_municipio == "03":
                municipio = "San Francisco Zapotitlán "
            if codigo_municipio == "04":
                municipio = "San Bernardino"
            if codigo_municipio == "05":
                municipio = "San José El Idolo"

        if codigo_departamentos == '11':
            departamento = " RETALHULEU   "

            if codigo_municipio == "01":
                municipio = "RETALHULEU  "
            if codigo_municipio == "02":
                municipio = "San Sebastián"
            if codigo_municipio == "03":
                municipio = "Santa Cruz Mulu "
            if codigo_municipio == "04":
                municipio = "San Martín Zapotitlán"
            if codigo_municipio == "05":
                municipio = "San Felipe "

        if codigo_departamentos == '12':
            departamento = " SAN MARCOS    "

            if codigo_municipio == "01":
                municipio = "SAN MARCOS   "
            if codigo_municipio == "02":
                municipio = "San Pedro"
            if codigo_municipio == "03":
                municipio = "Santa antonio"
            if codigo_municipio == "04":
                municipio = "Comitancillo"
            if codigo_municipio == "05":
                municipio = "San Miguel Ixtahuacán  "

        if codigo_departamentos == '13':
            departamento = " HUEHUETENANGO    "

            if codigo_municipio == "01":
                municipio = "HUEHUETENANGO  "
            if codigo_municipio == "02":
                municipio = "Chiantla"
            if codigo_municipio == "03":
                municipio = "Malacatancito  "
            if codigo_municipio == "04":
                municipio = "Cuilco"
            if codigo_municipio == "05":
                municipio = "Nentón  "

        if codigo_departamentos == '15':
            departamento = "  BAJA VERAPAZ     "

            if codigo_municipio == "01":
                municipio = "Salamá  "
            if codigo_municipio == "02":
                municipio = "San Miguel Chicaj"
            if codigo_municipio == "03":
                municipio = "Rabinal  "
            if codigo_municipio == "04":
                municipio = "Cubulco"
            if codigo_municipio == "05":
                municipio = "Granados  "
        
        if codigo_departamentos == '14':
            departamento = "  BAJA VERAPAZ     "

            if codigo_municipio == "01":
                municipio = "Salamá  "
            if codigo_municipio == "02":
                municipio = "San Miguel Chicaj"
            if codigo_municipio == "03":
                municipio = "Rabinal  "
            if codigo_municipio == "04":
                municipio = "Cubulco"
            if codigo_municipio == "05":
                municipio = "Granados  "


        print('Departamento: ', departamento)
        print('Municipio: ', municipio)




    return 0





main()

