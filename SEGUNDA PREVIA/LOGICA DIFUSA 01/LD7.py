import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

x= np.arange(0, 11, 1)
vd_trapezoidal = sk.trapmf (x, [0,3,5,8])

plt.figure()
plt.plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresia')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)
plt.show()
