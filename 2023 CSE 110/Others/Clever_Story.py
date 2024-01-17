# Create inputs for the following ramdom thoughts to create the assignment Clever Story

print("Please enter the following: ")
print()
adjective = input("Adjective: ")
verb0 = input("First Verb: ")
animal = input("Animal: ")
exclamation = input("Exclamation: ")
verb1 = input("Second Verb: ")
verb2 = input("Third Verb: ")

# Your story should look like:
#
# The other day, I was really in trouble. It all started when I saw a very
# tired snail yell down the hallway. "Oh no!" I yelled. But all
# I could think to do was to sing over and over. Miraculously,
# that caused it to stop, but not before it tried to skip
# right in front of my family.

print("\nYour story is:")
print()
print("The other day, I was really in trouble. It all started when I saw a very")
print(adjective.capitalize() + " " + animal.upper() + " "+ verb0.lower() + " down the hallway. " + exclamation.capitalize() +"!" + " " + "I yelled. But all")
print(f"I could think to do was to {verb1} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb2}")
print("right in front of my family.")
print()