def clean_population_file(converted_files):
    """Function to normalize population TXT data files"""
    population_data = []

    for txt_file in converted_files:
        with open(txt_file, 'r') as f:
            # Read the header and clean it
            header = f.readline().rstrip().split('\t')
            for i in range(len(header)):
                header[i] = header[i].strip().lower()

            # Replace 'all years' by 'population'
            for i in range(len(header)):
                if header[i] == 'all years':
                    header[i] = 'population'
            print(f'\nRename : {header}')
            
            # Get the index of each useful column (ignore 'code')
            idx_entity = header.index('entity')
            idx_year = header.index('year')
            idx_population = header.index('population')

            # Loop over data lines
            for line in f: 
                columns = line.rstrip().split('\t')

                # Skip lines that are too short (errors)
                if len(columns) <= max(idx_entity, idx_year, idx_population):
                    continue

                # Append only the useful columns, ignore 'code'
                try:
                    population_data.append({
                        'entity': columns[idx_entity],
                        'year': int(columns[idx_year]),
                        'population': int(columns[idx_population])
                    })
                except ValueError:
                    # Skip lines where year or population is not a number
                    continue

    return population_data

import matplotlib.pyplot as plt

def plot_population(population_data):
    """Plot demographic curves from population_data (list of dicts)"""
    
    # Group data by country
    data_by_country = {}
    for pop_entry in population_data:
        country = pop_entry['entity']
        year = pop_entry['year']
        pop = pop_entry['population']


        if country not in data_by_country:

            # Creation of empty list in the dictionnary 'country' which is the key inside the DICTIONNARY 'data_by_country
            data_by_country[country] = {'year': [], 'population': []}
        # Append the current year and population to the corresponding lists for this country
        data_by_country[country]['year'].append(year)
        data_by_country[country]['population'].append(pop)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    for country, values in data_by_country.items():
        plt.plot(values['year'], values['population'], marker='o', label=country)

     # Set axis labels and title
    plt.xlabel('Year')
    plt.ylabel('Population (millions)')
    plt.title('Demographic Evolution by Country')

    # x-axis is from 1950 to 2023 with ticks every 10 years
    plt.xlim(1950, 2023)
    plt.xticks(range(1950, 2024, 10))

    # y-axis is from 0 to 350 million with ticks every 10 million
    plt.ylim(0, 80_000_000)
    plt.yticks(range(0, 80_000_001, 10_000_000))

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
