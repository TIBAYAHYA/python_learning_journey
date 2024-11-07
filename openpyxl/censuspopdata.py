import openpyxl,pprint
wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb["Population by Census Tract"]
countrys_population_dict = {}
max_country_lengh = 0
max_population_lengh = 0
for x in range(2,sheet.max_row+1):
    country = sheet["C%s"%x].value
    if country not in countrys_population_dict:
        countrys_population_dict[country] = sheet["D%s"%x].value
    else: countrys_population_dict[country] += sheet["D%s"%x].value
for country,population in countrys_population_dict.items():
    if len(country)> max_country_lengh:
        max_country_lengh = len(country)
    if len(str(population))> max_population_lengh:
        max_population_lengh = len(str(population))
for country,population in countrys_population_dict.items():
    country = str(country).center(max_country_lengh," ")
    population = str(population).rjust(max_population_lengh," ")
    print(f"The 2010 population of {country} is {population}")