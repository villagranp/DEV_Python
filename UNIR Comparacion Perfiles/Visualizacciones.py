import numpy as np
import matplotlib.pyplot as plt

labels =  ['Experiencia','Comunicación','Amabilidad',
            'Dominio del Tema','Presentación','Educación']
indice = [1,2,3,4,5,6]
dataKaren  = [4,   3.5, 4,   4,   3,    3.5]
dataMike  =[4.5,   2, 2,   5,   1.5,  4.5]
dataJack  =  [2.5,   5, 4.5, 2.5, 2.75,   2]
nAttr = 6
data = np.array([   dataKaren,
                    dataMike,
                    dataJack,])
data = np.transpose(data)
data_labels = ('Karen Fortou', 'Mike Rafun', 'Jack Nymbul')
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles,data,'o-', linewidth=1, alpha=0.4)
plt.fill(angles,data, alpha=0.4)
plt.thetagrids(angles*180/np.pi, labels)
plt.figtext(0.52, 0.95, 'Comparación Entre Perfiles', ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='small')
plt.grid(True)
plt.show()

plt.grid(True)  
plt.xlabel("Habilidades")  
plt.ylabel("Puntuación") 
plt.xticks(indice,labels)
plt.plot(dataKaren, marker='o', linestyle='-', color='b', label = "Karen Fortou")
plt.plot(dataMike, marker='o', linestyle='-', color='orange', label = "Mike Rafun")
plt.plot(dataJack, marker='o', linestyle='-', color='g', label = "Jack Nymbul")
plt.title(label = "Comparacion de Perfiles", loc="left", fontstyle='italic', fontsize='20' )
plt.legend(loc="lower right")
plt.plot(labels,dataKaren, marker='o', color='b')
plt.plot(labels,dataMike, marker='o', color='orange')
plt.plot(labels,dataJack, marker='o', color='g')
plt.ylim(ymin=0)
plt.show()