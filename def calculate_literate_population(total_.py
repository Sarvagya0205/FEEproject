def calculate_literate_population(total_population, percent_men, percent_literacy, percent_literate_men):
    # Calculate the total number of men and women in the town
    total_men = (percent_men / 100) * total_population
    total_women = total_population - total_men

    # Calculate the total number of literate people in the town
    total_literate = (percent_literacy / 100) * total_population

    # Calculate the total number of literate men
    literate_men = (percent_literate_men / 100) * total_population

    # Calculate the total number of literate women
    literate_women = total_literate - literate_men

    return int(literate_men), int(literate_women)

# Given data
total_population = 80000
percent_men = 52
percent_literacy = 48
percent_literate_men = 35

# Calculate the total number of literate men and women
literate_men, literate_women = calculate_literate_population(total_population, percent_men, percent_literacy, percent_literate_men)

# Display the results
print(f"Total number of literate men: {literate_men}")
print(f"Total number of literate women: {literate_women}")
