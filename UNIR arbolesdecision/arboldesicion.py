import pandas
import os
import numpy


if __name__ == "__main__":
    file = "Laboratorio_dataset_car.csv"
    if (os.path.exists(file)):
        dataFrame = pandas.read_csv(file ,sep=";")
        print(dataFrame)
    else:
        print('El archivo {} no se ha encontrado.'.format(file))