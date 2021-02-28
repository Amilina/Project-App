import click
import time
import runpy

stop = False

# Start
click.clear()
print(" ")
click.secho("Welcome to the German learning app!\n", bold=True)

# Asking for motivation, user can choose between yes and no
if click.confirm('\nAre you motivated to learn some German?'):
    print('\nOkay! Lets start!')
    time.sleep(1)
    click.clear()
else:
    click.clear()
    print("\nOk then let's call it a day. Bye!")
    time.sleep(3)
    click.clear()
    stop = True

# Menu
while not stop: 
    print(" ")
    print(19*"-", "MENU", 19*"-")
    print("\nThis app has four basic functions.")
    print("- Type 'mode1' to enter the dictionary")
    print("- Type 'mode2' to train your vocabulary")
    print("- Type 'mode3' to train some german grammar")
    print("- Type 'mode4' to play a fun mad libs game")
    print("\nType 'exit' to exit the app\n")
    print(44*"-")


    choice = input("\nWhich mode do you want to do? ")

    if choice == "mode1":
        click.clear()
        runpy.run_path("Mode1.py")
    elif choice == "mode2":
        click.clear()
        runpy.run_path("Mode2_Menu.py")
    elif choice == "mode3":
        click.clear()
        runpy.run_path("Mode3.py")
    elif choice == "mode4":
        click.clear()
        runpy.run_path("Mode4.py")
    elif choice == "exit":
        click.clear()
        print("\nOk then let's call it a day. Bye!")
        time.sleep(3)
        click.clear()
        stop = True
    else:
        click.clear()
        print("\nThis function does not exist. And you don't read instructions. Try again.")


