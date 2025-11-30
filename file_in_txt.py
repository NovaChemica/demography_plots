from export_txt import Data as D

with open('population_france.csv') as file_object:
    data_france = D.__format__(file_object)
    print(data_france.__format__())