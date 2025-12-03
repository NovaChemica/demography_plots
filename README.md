# The objective is to demonstrate through this project an application of my python programming language study. 

I used : 
- Python 3.x
- matplotlib
- os (standard library)

data collected from [Our World in Data](https://ourworldindata.org/population-growth#explore-data-on-population-growth)

Saved as: 
        - population_france.csv
        - population_greece.csv
        - population_spain.csv

## Example of usage (in the file main_dem_plots.py)
 
            import os
        from module_dem_plots import ConvertData as CD
        from module_dem_plots import LinePlot as LP
        from plot_pop_functions import clean_population_file
        from plot_pop_functions import plot_population

        folder = os.getcwd() #use current working directory
        converted_files = CD(folder).to_txt()

population_data = clean_population_file(converted_files)
plot_graph = plot_population(population_data)

## Structure of the project (2 main parts and 2 subparts)

A. Generic classes are grouped in the module: module_dem_plots.py 
        - class Mother : base class for folder processing
        - class Daugther(Mother) : class related to the mother for file processing

    This folder is used in the first part of the main program : main_dem_plots.py
        - It allows a first treat of the file available in the repository demography_plots
        - Convert CSV or DAT files in a tabular TXT file

B. Two functions linked to the project are grouped in the module: plot_pop_functions.py 
        - the first function is for collecting the data of interest from the TXT file into a dictionnary
        - the second to plot the "scatter-line" curves with the matplotlib library 


The output in the terminal is captured in the picture: **program_execution.png**

The final graph is saved as: **PLOT_demographic_evolution_by_count.png**

The program demonstrates :
- Object-oriented programming: classes, methods, functions
- Data treatment automation
- Uses try-except blocks to handle variations in CSV/DAT files.
- Easy to extend to handle more countries or larger datasets.
