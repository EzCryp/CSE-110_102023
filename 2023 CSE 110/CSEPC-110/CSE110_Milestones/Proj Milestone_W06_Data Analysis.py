""""
Author: Ezra Zacarias
Milestone: W06_Data Analysis
"""
import csv


# A sample run could look as follows:
# Enter the year of interest: {1959}

# The overall max life expectancy is: {86.751} from {Monaco} in {2019}
# The overall min life expectancy is: {17.76} from {Iceland} in {1882}

# For the year 1959:
# The average life expectancy across all countries was 54.95
# The max life expectancy was in Norway with 73.49
# The min life expectancy was in Mali with 28.077

# use the with function to make sure that it will not have a problem that the file is not closed properly
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

        # test if file will open
        # print(line)

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

#
print(f"\nThe overall max life expectancy is: {max(expectancies)} from {countries[expectancies.index(max(expectancies))]} in the year {years[expectancies.index(max(expectancies))]}.")

# 
print(f"The overall min life expectancy is: {min(expectancies)} from {countries[expectancies.index(min(expectancies))]} in the year {years[expectancies.index(min(expectancies))]}.\n")

#
print(f"From the year {year_of_interest}:")

#
year_of_interest_list = []
total = 0

#
for yr in range(len(years)):
    if year_of_interest == float(years[yr]):
        year_of_interest_list.append(expectancies[yr])

# 
for num in year_of_interest_list:
    total += float(num)


#
print(f"\nThe average life expectancy accross all countries was {round(total/len(year_of_interest_list),2)}")

#
print(f"The maximum life expectancy was in {countries[expectancies.index(max(year_of_interest_list))]} in the year {max(year_of_interest_list)}")

#
print(f"The minimum life expectancy was in {countries[expectancies.index(min(year_of_interest_list))]} in the year {min(year_of_interest_list)} \n")

