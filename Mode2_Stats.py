import click
import runpy
import pandas
import emoji
from os import path

min_correct = 5
frog_upperlimit = 20
rabbit_upperlimit = 35
monkey_upperlimit = 60
dolphin_upperlimit = 75

# Explanation
print(" ")
print(10*"-", "TEST STATISTICS", 10*"-")
print("\nHere are some analytics regarding your process in the vocabulary trainer.")

# Check if output file already exist
if path.exists("output.csv") == False:
    print("\nThere are no statistics available yet. You must first use the vocab trainer")
else:
    data_csv = pandas.read_csv('output.csv', sep=';')

    wordpair_count = len(data_csv.index)
    total_runs = data_csv.at[0, 'total_count']
    correct_counter = 0
    wrong_counter = 0
    for num in data_csv['correct_count']:
        if num >= 3:
            correct_counter += 1
    for num in data_csv['wrong_count']:
        if num >= 3:
            wrong_counter += 1

    print("\n- Possible word pairs: %d" % wordpair_count)
    print("- How often you have used the vocab trainer: %d" % total_runs)
    print("- How many words you've gotten right more than two times: %d" % correct_counter )
    print("- How many words you've keep getting wrong more than two times: %d " % wrong_counter)

    beetle_rank = total_runs >= 1
    frog_rank = min_correct <= correct_counter < frog_upperlimit
    rabbit_rank = frog_upperlimit <= correct_counter < rabbit_upperlimit
    monkey_rank = rabbit_upperlimit <= correct_counter < monkey_upperlimit
    dolphin_rank = monkey_upperlimit <= correct_counter < dolphin_upperlimit
    elephant_rank = correct_counter >= dolphin_upperlimit

    if beetle_rank and frog_rank:
        print(emoji.emojize("\nCurrent rank: :frog:"))
        print("Your current rank is frog")
    elif beetle_rank and rabbit_rank:
        print(emoji.emojize("\nCurrent rank: :rabbit:"))
        print("Your current rank is bunny")
    elif beetle_rank and monkey_rank:
        print(emoji.emojize("\nCurrent rank: :monkey:"))
        print("Your current rank is monkey")
    elif beetle_rank and dolphin_rank:
        print(emoji.emojize("\nCurrent rank: :dolphin:"))
        print("Your current rank is dolphin")
    elif beetle_rank and elephant_rank:
        print(emoji.emojize("\nCurrent rank: :elephant:"))
        print("Your current rank is elephant")
    elif beetle_rank:
        print(emoji.emojize("\nCurrent rank: :beetle:"))
        print("Your current rank is beetle")
    
input('\nHit enter to go back to the mode 2 menu')
click.clear()
runpy.run_path("Mode2_Menu.py")
