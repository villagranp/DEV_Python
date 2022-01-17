import numpy as np
import matplotlib.pyplot as plt


indice = np.arange(23) 
xlabels = np.arange(1983,2006,1)
time = np.array([360, None, None, None, None, None, None, None, None, None, 320, None, None, None, None, None, None, None, None, None, 305, 290, 265]).astype(np.double)
timeMask = np.isfinite(time)
newsweek = np.array([350, None, None, None, None, None, None, None, None, None, 250, None, None, None, None, None, None, None, None, None, 175, 180, 185]).astype(np.double)
newsweekMask = np.isfinite(newsweek)

plt.grid(True)  
plt.xlabel("Año")  
plt.ylabel("Empleados") 
plt.xticks(indice,xlabels)
plt.plot(time, marker='o', linestyle='-', color='b', label = "Time")
plt.plot(newsweek, marker='o', linestyle='-', color='g', label = "Newsweek")
plt.title(label = "Comparación de Empleados a travéz del tiempo Time vs Newsweek", loc="left", fontstyle='italic', fontsize='20' )
plt.legend(loc="lower left")
plt.plot(indice[timeMask],time[timeMask], marker='o', color='b')
plt.plot(indice[newsweekMask],newsweek[newsweekMask], marker='o', color='g')
plt.ylim(ymin=0)  
plt.show() 