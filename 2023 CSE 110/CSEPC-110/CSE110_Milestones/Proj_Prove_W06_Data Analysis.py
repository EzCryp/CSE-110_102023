""""
Author: Ezra Zacarias
Prove: W06_Data Analysis
"""
import csv

# This project for Week 06 is regarding on how to work with files such as .txt or .csv
# This project will be working with dataset that comes from OurWorldInData.org from an article on the Spanish Flu.
# the csv files contains roughly 19,000 rows of dataset

# First is to open the .csv file usith the with function
# We use the with function to make sure that it will not have a problem that the file is not closed properly
with open("life-expectancy.csv", "r") as csv_file:
    csv_file.readline()

    # creating a empty list for the following category
    years = []
    countries = []
    expectancies = []

    # clean_file = csv_reader.split(",")
    for line in csv_file:

        # make sure the file is clean by using the strip function to remove any unecessary white space
        line = line.strip()

        # Split the current line into its parts based on a space "," as the separator
        line = line.split(",")

        # use a variable for each line to identify each category
        country = line[0]
        year = line[2]
        life_expectancy = line[3]

        # place the data to the empty list storage
        countries.append(country)
        years.append(year)
        expectancies.append(life_expectancy)


# ask user to select a year of interest
year_of_interest = int(input("\nEnter the year of interest: "))

# show overall maximum life expectancy from a country with the  maximum life expectancy along with the year
print(f"\nThe overall max life expectancy is: {max(expectancies)} from {countries[expectancies.index(max(expectancies))]} in the year {years[expectancies.index(max(expectancies))]}.")

# show overall minimum life expectancy from a country with the  minimum life expectancy along with the year
print(f"The overall min life expectancy is: {min(expectancies)} from {countries[expectancies.index(min(expectancies))]} in the year {years[expectancies.index(min(expectancies))]}.\n")

# Once again show the year of interest the user inputs
print(f"From the year {year_of_interest}:")

# create a empty list for the year of interest and total
year_of_interest_list = []
total = 0

#
for yr in range(len(years)):
    if year_of_interest == float(years[yr]):
        year_of_interest_list.append(expectancies[yr])

# 
for num in year_of_interest_list:
    total += float(num)


# Show data for the average life expectancy accross various countries
print(f"\nThe average life expectancy accross all countries was {round(total/len(year_of_interest_list),2)}")

# Show data from a country with the maximum life expectancy 
print(f"The maximum life expectancy was in {countries[expectancies.index(max(year_of_interest_list))]} in the year {max(year_of_interest_list)}")

# Show data from a country with the minimum life expectancy 
print(f"The minimum life expectancy was in {countries[expectancies.index(min(year_of_interest_list))]} in the year {min(year_of_interest_list)} \n")

