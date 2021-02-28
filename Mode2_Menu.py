import click
import runpy
import os
from os import path

# Choice between test vocab, see or reset statistics
print(" ")
print(10*"-", "VOCABULARY TRAINER", 10*"-")
print("\nYou have three options:")
print("- Type 'test' to train some vocabulary")
print("- Type 'stats' to see some statistics")
print("- Type 'reset' to reset all statistics")
print("\nType 'back' to go back to the main menu")

choice = input("\nWhat do you want to do? ")

if choice == 'test':
    click.clear()
    runpy.run_path("Mode2_Trainer.py")
elif choice == 'stats':
    click.clear()
    runpy.run_path("Mode2_Stats.py")
elif choice == 'reset':
    if path.isfile('output.csv'):
        os.remove('output.csv')
        click.clear()
        print("Okay, all statistics have been reset. You can now start again from the beginning!")
        runpy.run_path("Mode2_Menu.py")
    else:
        click.clear()
        print("There are no statistics that can be reset yet.")
        runpy.run_path("Mode2_Menu.py")
elif choice == 'back':
    input('\nHit enter to go back to the main menu')
    click.clear()
else:
    click.clear()
    print("\nThis function does not exist. And you don't read instructions. Try again.")
    runpy.run_path("Mode2_Menu.py")
    

        
