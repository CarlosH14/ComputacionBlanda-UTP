import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

x= np.arange(0,11,1)

bajo=sk.trimf(x, [0,0,5])
medio=sk.trimf(x, [0,5,10])


plt.figure()

plt.plot(x, medio, 'r', linewidth=1.5, label='Medio')
plt.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')

plt.title('Funcion Union Maximo')
plt.ylabel('Membresia')
plt.xlabel('Velocidad Km / h')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)

plt.axvline(x=0, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=1, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=2, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=3, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=4, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=5, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=6, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=7, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=8, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=9, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=10, ymin=0, ymax=10, color="g", linestyle='-.')

plt.plot(0,1,marker='o', markersize=10, color='g')
plt.plot(1,0.8,marker='o', markersize=10, color='g')
plt.plot(2,0.6,marker='o', markersize=10, color='g')
plt.plot(3,0.6,marker='o', markersize=10, color='g')
plt.plot(4,0.8,marker='o', markersize=10, color='g')
plt.plot(5,1,marker='o', markersize=10, color='g')

plt.plot(6,0.8,marker='o', markersize=10, color='g')
plt.plot(7,0.6,marker='o', markersize=10, color='g')
plt.plot(8,0.4,marker='o', markersize=10, color='g')
plt.plot(9,0.2,marker='o', markersize=10, color='g')
plt.plot(10,0,marker='o', markersize=10, color='g')


plt.show()
