
countries = ['Argentina', 'Colombia', 0]
capitals = ['Buenos Aires', 'Bogota', 0]
areas = [1908, 1000, 0]
populations = [50, 45]
populations.append(100)
cont = 3
list_dict = []
for i in range(0, cont):
    dict1 = {}
    dict1['pais'] = countries[i]
    dict1['capital'] = capitals[i]
    dict1['areas'] = str(areas[i])
    dict1['poblacion'] = str(populations[i]) 
    list_dict.append(dict1)

for jugar in list_dict:
    print(jugar)