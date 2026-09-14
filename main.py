import random
import time

from grafica import graficar_tiempos
from ordenamientos import (
    bubble_sort_brute_force,
    exchange_sort,
    gnome_sort,
    insertion_sort,
    selection_sort,
    stooge_sort,
)

inicio = 20
incremento = 20
fin = 100
a = 0
lista_de_listas = []
tempo = 0
tempo2 = 0
tempo3 = 0
tempo4 = 0
tempo5 = 0
tempo6 = 0

ejeX = []
ejeY_bubble = []
ejeY_selection = []
ejeY_insertion = []
ejeY_gnome_sort = []
ejeY_stooge_sort_rec = []
ejeY_exchange_sort = []

for i in range(inicio, fin + 1, incremento):
  a += 1
  arreglo_num = []

  for j in range(i):
    numero_random = random.randint(0, 10000)
    arreglo_num.append(numero_random)

  lista_de_listas.append(arreglo_num)
  ejeX.append(i)
  print(f'Lista de #{i}, {arreglo_num}')


print('Ordenamiento de Bubble Sort')

for f in range(len(lista_de_listas)):
  lista_actual = lista_de_listas[f].copy()
  tiempo_inicio = time.time()

  lista_actual_ordenada = bubble_sort_brute_force(lista_actual)
  tiempo_fin = time.time()

  tiempo_total = tiempo_fin - tiempo_inicio
  tempo += tiempo_total
  ejeY_bubble.append(tiempo_total)
  print(f'Lista de #{inicio+f*incremento}')
  print(lista_actual_ordenada)
  print(f'Tardo {tiempo_total}s')

print(f'El bubble sort tardo un total de {tempo} s')

print('Ordenamiento por Selection Sort')
for k in range(len(lista_de_listas)):
  lista_actual2 = lista_de_listas[k].copy()

  tiempo_inicio2 = time.time()

  lista_actual_ordenada_2 = selection_sort(lista_actual2)
  tiempo_fin2 = time.time()
  tiempo_total2 = tiempo_fin2 - tiempo_inicio2
  tempo2 += tiempo_total2
  ejeY_selection.append(tiempo_total2)
  print(f'Lista de #{inicio+k*incremento}')
  print(lista_actual_ordenada_2)
  print(f'Tardo {tiempo_total2}s')

print(f'El selection sort tardo un total de {tempo2} s')

print('El ordenamietno de insertion')
for l in range(len(lista_de_listas)):
  lista_actual3 = lista_de_listas[l].copy()
  tiempo_inicio3 = time.time()

  lista_actual_ordenada3 = insertion_sort(lista_actual3)
  tiempo_fin3 = time.time()

  tiempo_total3 = tiempo_fin3 - tiempo_inicio3
  tempo3 += tiempo_total3
  ejeY_insertion.append(tiempo_total3)
  print(f'Lista de #{inicio+l*incremento}')
  print(lista_actual_ordenada3)
  print(f'Tardo {tiempo_total3}s')

print(f'El insertion sort tardo un total de {tempo3} s')


print('El gnome_sort')
for c in range(len(lista_de_listas)):
  lista_actual4 = lista_de_listas[c].copy()
  tiempo_inicio4 = time.time()

  lista_actual_ordenada4 = gnome_sort(lista_actual4)
  tiempo_fin4 = time.time()

  tiempo_total4 = tiempo_fin4 - tiempo_inicio4
  tempo4 += tiempo_total4
  ejeY_gnome_sort.append(tiempo_total4)
  print(f'Lista de #{inicio+c*incremento}')
  print(lista_actual_ordenada4)
  print(f'Tardo {tiempo_total4}s')

print(f'El gnome sort tardo un total de {tempo4} s')

print('El stooge sort rec')
for e in range(len(lista_de_listas)):
  lista_actual5 = lista_de_listas[e].copy()
  tiempo_inicio5 = time.time()

  lista_actual_ordenada5 = stooge_sort(lista_actual5)
  tiempo_fin5 = time.time()

  tiempo_total5 = tiempo_fin5 - tiempo_inicio5
  tempo5 += tiempo_total5
  ejeY_stooge_sort_rec.append(tiempo_total5)
  print(f'Lista de #{inicio+e*incremento}')
  print(lista_actual_ordenada5)
  print(f'Tardo {tiempo_total5}s')

print(f'El stooge_sort_rec tardo un total de {tempo5} s')


print('El  exchange_sort')
for z in range(len(lista_de_listas)):
  lista_actual6 = lista_de_listas[z].copy()
  tiempo_inicio6 = time.time()

  lista_actual_ordenada6 = exchange_sort(lista_actual6)
  tiempo_fin6 = time.time()

  tiempo_total6 = tiempo_fin6 - tiempo_inicio6
  tempo6 += tiempo_total6
  ejeY_exchange_sort.append(tiempo_total6)
  print(f'Lista de #{inicio+z*incremento}')
  print(lista_actual_ordenada6)
  print(f'Tardo {tiempo_total6}s')

print(f'El  exchange_sort tardo un total de {tempo6} s')

graficar_tiempos(
    ejeX,
    ejeY_bubble,
    ejeY_selection,
    ejeY_insertion,
    ejeY_gnome_sort,
    ejeY_stooge_sort_rec,
    ejeY_exchange_sort,
)