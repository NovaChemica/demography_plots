import os
from module_dem_plots import ConvertData as CD
from module_dem_plots import LinePlot as LP
from    plot_pop_functions import clean_population_file
from    plot_pop_functions import plot_population

folder = os.getcwd() #use current working directory
converted_files = CD(folder).to_txt()

population_data = clean_population_file(converted_files)
plot_graph = plot_population(population_data)
