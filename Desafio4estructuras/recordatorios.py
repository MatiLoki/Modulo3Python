recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                ['2021-05-01', "15:00", "No trabajar"],
                ['2021-07-15', "13:00", "No hacer nada es feriado"],
                ['2021-09-18', "16:00", "Ramadas"],
                ['2021-12-25', "00:00", "Navidad"]]

#Agregar un evento 
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

#Modificar el evento del 15 de Julio
for recordatorio in recordatorios:
    if recordatorio[0] == '2021-07-15':
        recordatorio[0] = '2021-07-16'
        break

#Eliminar el evento del día del trabajo
for recordatorio in recordatorios:
    if recordatorio[0] == '2021-05-01':
        recordatorios.remove(recordatorio)
        break

#Agregar una cena de Navidad y de Año Nuevo a las 22 hrs
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

recordatorios.sort()
print(recordatorios)