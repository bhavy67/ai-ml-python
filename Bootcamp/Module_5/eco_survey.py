from ast import literal_eval

# Taking the input 
site_records = literal_eval(input())

def analyse_bird_data(site_records):
    species_count = {}
    for site, birds in site_records.items():
        for bird in birds:
            species_count[bird] = species_count.get(bird, 0) + 1

    migratory = sorted([species for species, count in species_count.items() if count >= 3])

    exclusive = {}
    for site, birds in site_records.items():
        exclusive[site] = sorted([bird for bird in birds if species_count[bird] == 1])

    return [migratory, exclusive]

# Print the output
print(analyse_bird_data(site_records))
