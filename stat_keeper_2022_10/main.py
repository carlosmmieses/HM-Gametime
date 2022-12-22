from re import A, X
import sqlite3
from stat_keeper.stat_keeper import StatKeeper
from stat_keeper.player import Player
import csv


if __name__ == "__main__":
    # We initiate a connection to setup the database
    # in case it does not exist
    init_stat_keeper = StatKeeper()
    init_stat_keeper.setup()
    # We start the workflow to read all PDFs in the PDF folder and 
    # add the info to the database in case the file was not scanned already
    stat_keeper = StatKeeper()
    stat_keeper.run()


#COMO ORDENAR LAS FILAS
# '''
#     Podemos ordenar las filas por cualquier celda.
#     Si queremos que sea de forma ascendente es el default, si queremos
#     descendente hay que escribir DESC.
# '''
'''
    todo: 
        1.Hacer funciones que generen csv files de promedio de 3, 
         rebotes, tiroslibres, bloqueos,
         promediodepuntos, anotaciones, asistencias, steals.
    

'''

conn = sqlite3.connect('stat_keeper.db')
c = conn.cursor()

def get_promediodetres():
    c.execute("SELECT NAME, TEAM, NUM_GAMES, _3PT FROM PLAYER_STATS ORDER BY _3PT DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items: #item es cada query de la lista de queries.
        tot_ft = item[3].split('/') #tiros libres
        num_ft = float(tot_ft[0])#numerador
        den_ft = float(tot_ft[1])#denominador
        per_ft = num_ft / den_ft #numero decimal
        por_fr = int(per_ft * 100) #porcentaje de tiros libres
        y = list(item)
        y.append(por_fr)
        csv_rows.append(y)

        # field names
    fields = ['Nombre', 'Equipo', 'Juegos Jugados','Anotaciones', 'Promedio']
	
    csv_rows.sort(reverse=True, key = lambda x: x[4])
    # name of csv file
    filename = "promediodetres.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_promediodetres()
def get_teampromediodetres():
    c.execute("SELECT TEAM, NUM_GAMES, _3PT FROM TEAM_STATS ORDER BY _3PT DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items: #item es cada query de la lista de queries.
        tot_ft = item[2].split('/') #tiros libres
        num_ft = float(tot_ft[0])#numerador
        den_ft = float(tot_ft[1])#denominador
        per_ft = num_ft / den_ft #numero decimal
        por_fr = int(per_ft * 100) #porcentaje de tiros libres
        y = list(item)
        y.append(por_fr)
        csv_rows.append(y)

        # field names
    fields = ['Equipo', 'Juegos Jugados','Anotaciones', 'Promedio']
	
    csv_rows.sort(reverse=True, key = lambda x: x[2])
    # name of csv file
    filename = "promediodetres(equipo).csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_teampromediodetres()


def get_rebotes():
    c.execute("SELECT NAME, TEAM, NUM_GAMES, TR, TR_PER_GAME FROM PLAYER_STATS ORDER BY TR DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[4]) 
        y.pop(4)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Nombre', 'Equipo', 'Juegos Jugados','Rebotes', 'Promedio']
	
	
    # name of csv file
    filename = "rebotes.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_rebotes()
def get_teamrebotes():
    c.execute("SELECT TEAM, NUM_GAMES, TR, TR_PER_GAME FROM TEAM_STATS ORDER BY TR DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[3]) 
        y.pop(3)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Equipo', 'Juegos Jugados','Rebotes', 'Promedio']
	
	
    # name of csv file
    filename = "rebotes(equipo).csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_teamrebotes()




def get_tiroslibres():
    c.execute("SELECT NAME, TEAM, NUM_GAMES, FT FROM PLAYER_STATS ORDER BY FT DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items: #item es cada query de la lista de queries.
        tot_ft = item[3].split('/') #tiros libres
        ft = tot_ft[0] #tiros libres
        num_ft = float(tot_ft[0])#numerador
        den_ft = float(tot_ft[1])#denominador
        per_ft = num_ft / den_ft #numero decimal
        por_fr = int(per_ft * 100) #porcentaje de tiros libres
        y = list(item)
        y.append(por_fr)
        csv_rows.append(y)

        # field names
    fields = ['Nombre', 'Equipo', 'Juegos Jugados','Anotaciones', 'Promedio']
    csv_rows.sort(reverse=True, key = lambda x: x[4])
    # name of csv file
    filename = "promediodetiroslibres.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_tiroslibres()

def get_teamtiroslibres():
    c.execute("SELECT TEAM, NUM_GAMES, FT FROM TEAM_STATS ORDER BY FT DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items: #item es cada query de la lista de queries.
        tot_ft = item[2].split('/') #tiros libres
        ft = tot_ft[0] #tiros libres
        num_ft = float(tot_ft[0])#numerador
        den_ft = float(tot_ft[1])#denominador
        per_ft = num_ft / den_ft #numero decimal
        por_fr = int(per_ft * 100) #porcentaje de tiros libres
        y = list(item)
        y.append(por_fr)
        csv_rows.append(y)

        # field names
    fields = ['Equipo', 'Juegos Jugados','Anotaciones', 'Promedio']
    csv_rows.sort(reverse=True, key = lambda x: x[3])
    # name of csv file
    filename = "promediodetiroslibres(equipo).csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_teamtiroslibres()




def get_anotaciones():
    c.execute("SELECT NAME, TEAM, NUM_GAMES, PTS, PTS_PER_GAME FROM PLAYER_STATS ORDER BY PTS DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[4]) 
        y.pop(4)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Nombre', 'Equipo', 'Juegos Jugados','Anotaciones', 'Promedio']
	
	
    # name of csv file
    filename = "anotaciones.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_anotaciones()
def get_teamanotaciones():
    c.execute("SELECT TEAM, NUM_GAMES, PTS, PTS_PER_GAME FROM TEAM_STATS ORDER BY PTS DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[3]) 
        y.pop(3)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Equipo', 'Juegos Jugados','Anotaciones', 'Promedio']
	
	
    # name of csv file
    filename = "anotaciones(equipo).csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_teamanotaciones()



def get_asistencias():
    c.execute("SELECT NAME, TEAM, NUM_GAMES, AST, AST_PER_GAME FROM PLAYER_STATS ORDER BY AST DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[4]) 
        y.pop(4)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Nombre', 'Equipo', 'Juegos Jugados','Asistencias', 'Promedio']
	
	
    # name of csv file
    filename = "asistencias.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_asistencias()
def get_teamasistencias():
    c.execute("SELECT TEAM, NUM_GAMES, AST, AST_PER_GAME FROM TEAM_STATS ORDER BY AST DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[3]) 
        y.pop(3)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Equipo', 'Juegos Jugados','Asistencias', 'Promedio']
	
	
    # name of csv file
    filename = "asistencias(equipo).csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_teamasistencias()



def get_steals():
    c.execute("SELECT NAME, TEAM, NUM_GAMES, ST, ST_PER_GAME FROM PLAYER_STATS ORDER BY ST DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[4]) 
        y.pop(4)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Nombre', 'Equipo', 'Juegos Jugados','Robos de balon', 'Promedio']
	
	
    # name of csv file
    filename = "steals.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_steals()
def get_teamsteals():
    c.execute("SELECT TEAM, NUM_GAMES, ST, ST_PER_GAME FROM TEAM_STATS ORDER BY ST DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[3]) 
        y.pop(3)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Equipo', 'Juegos Jugados','Robos de balon', 'Promedio']
	
	
    # name of csv file
    filename = "steals(equipo).csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_teamsteals()




def get_bloqueos():
    c.execute("SELECT NAME, TEAM, NUM_GAMES, BS, BS_PER_GAME FROM PLAYER_STATS ORDER BY BS DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[4]) 
        y.pop(4)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Nombre', 'Equipo', 'Juegos Jugados','Rebotes', 'Promedio']
	
	
    # name of csv file
    filename = "bloqueos.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_bloqueos()
def get_teambloqueos():
    c.execute("SELECT TEAM, NUM_GAMES, BS, BS_PER_GAME FROM TEAM_STATS ORDER BY BS DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items:
        y = list(item)
        format_float = "{:.2f}".format(item[3]) 
        y.pop(3)
        y.append(format_float)
        csv_rows.append(y)
    
    
    # field names
    fields = ['Equipo', 'Juegos Jugados','Rebotes', 'Promedio']
	
	
    # name of csv file
    filename = "bloqueos(equipo).csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_teambloqueos()




def get_prompuntos():
    c.execute("SELECT NAME, TEAM, NUM_GAMES, TFG FROM PLAYER_STATS ORDER BY TFG DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items: #item es cada query de la lista de queries.
        tot_ft = item[3].split('/') #tiros libres
        num_ft = float(tot_ft[0])#numerador
        den_ft = float(tot_ft[1])#denominador
        per_ft = num_ft / den_ft #numero decimal
        por_fr = int(per_ft * 100) #porcentaje de tiros libres
        y = list(item)
        y.append(por_fr)
        csv_rows.append(y)

        # field names
    fields = ['Nombre', 'Equipo', 'Juegos Jugados','Anotaciones', 'Promedio']
	
    csv_rows.sort(reverse=True, key = lambda x: x[4])
    # name of csv file
    filename = "promediodepuntos2.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_prompuntos()

def get_teamprompuntos():
    c.execute("SELECT TEAM, NUM_GAMES, TFG FROM TEAM_STATS ORDER BY TFG DESC")
    items = c.fetchmany(10) #lista de queries
    csv_rows = []
    for item in items: #item es cada query de la lista de queries.
        tot_ft = item[2].split('/') #tiros libres
        num_ft = float(tot_ft[0])#numerador
        den_ft = float(tot_ft[1])#denominador
        per_ft = num_ft / den_ft #numero decimal
        por_fr = int(per_ft * 100) #porcentaje de tiros libres
        y = list(item)
        y.append(por_fr)
        csv_rows.append(y)

        # field names
    fields = ['Equipo', 'Juegos Jugados','Anotaciones', 'Promedio']
	
    csv_rows.sort(reverse=True, key = lambda x: x[3])
    # name of csv file
    filename = "promediodepuntos(equipo).csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(csv_rows)
get_teamprompuntos()

###### TEST #######################
# c.execute("SELECT NAME, TEAM, NUM_GAMES, TFG FROM PLAYER_STATS ORDER BY TFG DESC")#Tiros Libres / 3 puntos
# #c.execute("SELECT NAME, NUMBER, TEAM, ST, ST_PER_GAME FROM PLAYER_STATS ORDER BY ST DESC")
# items = c.fetchmany(10) #lista de queries

# csv_rows = []
# for item in items: #item es cada query de la lista de queries.
#     # nombre = item[0]
#     # numero = item[1]
#     # equipo = item[2]
#     #print(item[3]) #todos los decimales.
#     #print(type(item[3]))
#     tot_ft = item[3].split('/') #tiros libres
#     ft = tot_ft[0] #tiros libres
#     #print(tot_ft)
#     #print(ft)
#     #format_float = "{:.2f}".format(item[4]) 
#     #print(format_float)
#     num_ft = float(tot_ft[0])#numerador
#     den_ft = float(tot_ft[1])#denominador
#     per_ft = num_ft / den_ft #numero decimal
    #print(per_ft)
#     por_fr = int(per_ft * 100) #porcentaje de tiros libres
#     y = list(item)
#     #y.pop(3) #tiros libres
#     #y.pop(4)
#     #y.append(format_float)
#     y.append(por_fr) #tiros libres
#     #print(y)
#     csv_rows.append(y)
#     #item = tuple(y)
#     #print(item)
# #print(csv_rows)
# # Python program to demonstrate
# # writing to CSV

# # Python code to sort the tuples using second element
# # of sublist Inplace way to sort using sort()
# def Sort(sub_li):

# 	# reverse = None (Sorts in Ascending order)
# 	# key is set to sort using second element of
# 	# sublist lambda has been used
# 	sub_li.sort(reverse=True, key = lambda x: x[4])
# 	return sub_li

# # Driver Code
# sub_li =[['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
# #print(Sort(csv_rows))
# tres_puntos = Sort(csv_rows)

# import csv
	
# # field names
# fields = ['Nombre', 'Numero', 'Equipo', 'Anotaciones', 'Promedio']
	
# # data rows of csv file
# ex_rows = [ ['Nikhil', 'COE', '2', '9.0'],
# 		['Sanchit', 'COE', '2', '9.1'],
# 		['Aditya', 'IT', '2', '9.3'],
# 		['Sagar', 'SE', '1', '9.5'],
# 		['Prateek', 'MCE', '3', '7.8'],
# 		['Sahil', 'EP', '2', '9.1']]
# #rows = [csv_rows]
	
# # name of csv file
# filename = "promediodepuntos.csv"
	
# # writing to csv file
# with open(filename, 'w') as csvfile:
# 	# creating a csv writer object
# 	csvwriter = csv.writer(csvfile)
		
# 	# writing the fields
# 	csvwriter.writerow(fields)
		
# 	# writing the data rows
# 	csvwriter.writerows(csv_rows)
