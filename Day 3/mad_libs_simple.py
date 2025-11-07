# This file contains a simple construction of Mad Libs game in python.

# Variables (Inputs)

proper_noun_1 : str = input("Enter a Proper Noun (Person's Name): ")
noun_1 : str = input("Enter a Noun: ")
adjective_1 : str = input("Enter an Adjective (Feeling): ")
verb_1 : str = input("Enter a Verb: ")
adjective_2 : str = input("Enter another Adjective (Feeling): ")
animal_1 : str = input("Enter an Animal Name: ")
verb_2 : str = input("Enter another Verb: ")
color_1 : str = input("Enter a Color: ")
verb_3 : str = input("Enter another Verb (ending in ing): ")
adverb_1 : str = input("Enter an Adverb (ending in ly): ")
number_1 : str = input("Enter a Number: ")
measure_of_time_1 : str = input("Enter a Measure of Time: ")
color_2 : str = input("Enter another Color: ")
animal_2 : str = input("Enter another Animal Name: ")
number_2 : str = input("Enter another Number: ")
silly_word : str = input("Enter a Silly Word: ")
noun_2 : str = input("Enter another Noun: ")

story : str = f"""
This weekend I am going camping with {proper_noun_1}. I packed my lantern, sleeping bag, and
{noun_1}. I am so {adjective_1} to {verb_1} in a tent. I am {adjective_2} we
might see a {animal_1}, they are kind of dangerous. We are going to hike, fish, and {verb_2}.
I have heard that the {color_1} lake is great for {verb_3}. Then we will
{adverb_1} hike through the forest for {number_1} {measure_of_time_1}. If I see a
{color_2} {animal_2} while hiking, I am going to bring it home as a pet! At night we will tell
{number_2} {silly_word} stories and roast {noun_2} around the campfire!! 
"""

print("\nYour Mad-Libs Story:")
print(story)