import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('emigracionCSV.csv')
dic= {'Enero': 1 ,
      'Febrero': 2 ,
      'Marzo': 3 ,
      'Abril': 4 ,
      'Mayo': 5 ,
      'Junio': 6 ,
      'Julio': 7 ,
      'Agosto': 8 ,
      'Septiembre': 9 ,
      'Octubre': 10 ,
      'Noviembre': 11 ,
      'Diciembre': 12 }
df["Mes"] = df["Mes"].replace(dic)
dftotal = df.groupby(['Mes','Año'],as_index = False).sum().pivot('Mes','Año').fillna(0)
x_axis_labels = ['2009','2010','2011','2012']
y_axis_labels = ['Enero','Febrero','Marzo','Abril',
                 'Mayo','Junio','Julio','Agosto',
                 'Septiembre','Octubre','Noviembre','Diciembre']


plt.figure(figsize = (10,7))
plt.title('Emigración Anual 2009 - 2012')
sns.heatmap(dftotal, cmap = "coolwarm", xticklabels=x_axis_labels, yticklabels=y_axis_labels )
plt.xlabel('Año')
plt.ylabel('Mes')
plt.show()