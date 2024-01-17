# Meet with group and create a code for HR System

with open(hr_system.txt) as f:
    # The file has now been opened and stored in a variable "f"

    # Read each line, one by one, into a variable: current_line
    for line in f:
        # Split the current line into its parts based on a space " " as the separator
        parts = line.split(" ")

        # Save the parts we need into variables
        name = parts[0]
        title = parts[2]

        # Output the name and title as desired
        print(f"Name: {name}, Title: {title}")