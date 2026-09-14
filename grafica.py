import matplotlib.pyplot as plt


def graficar_tiempos(
    ejeX,
    ejeY_bubble,
    ejeY_selection,
    ejeY_insertion,
    ejeY_gnome,
    ejeY_stooge,
    ejeY_exchange,
):
  plt.plot(ejeX, ejeY_bubble, label='Bubble Sort', marker='o')
  plt.plot(ejeX, ejeY_selection, label='Selection Sort', marker='o')
  plt.plot(ejeX, ejeY_insertion, label='Insertion Sort', marker='o')
  plt.plot(ejeX, ejeY_gnome, label='Gnome Sort', marker='o')
  #plt.plot(ejeX, ejeY_stooge, label='Stooge Sort', marker='o')
  plt.plot(ejeX, ejeY_exchange, label='Exchange Sort', marker='o')

  plt.xlabel('Cantidad de numeros N')
  plt.ylabel('Tiempo (S)')

  plt.legend()
  plt.show()