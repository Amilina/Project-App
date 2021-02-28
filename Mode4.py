import click
import random
from Data import create_outputfile

print(" ")
print(10*"-", "MAD LIBS GAME", 10*"-")

data_csv = create_outputfile()

# If vocab trainer was used less than 10 times, words are picked randomly
if data_csv.at[0, 'total_count'] <= 10:
    adj_df = data_csv[data_csv['Type of speech'] == "adj."]
    adj_list = adj_df.English.to_list()
    noun_df = data_csv[data_csv['Type of speech'] == "noun"]
    noun_list = noun_df.English.to_list()
    verb_df = data_csv[data_csv['Type of speech'] == "verb"]
    verb_list = verb_df.English.to_list()

# If vocab trainer was used more than 10 times, only words are used that the user already knows
else:
    adj_df = data_csv[data_csv['correct_count'] > data_csv['wrong_count']]
    adj_list = adj_df.English.to_list()
    noun_df = data_csv[data_csv['correct_count'] > data_csv['wrong_count']]
    noun_list = noun_df.English.to_list()
    verb_df = data_csv[data_csv['correct_count'] > data_csv['wrong_count']]
    verb_list = verb_df.English.to_list()

while True:
    print(" ")
    print("A unicorn is nothing like a %s."  % random.choice(noun_list)) 
    print("They are %s creatures." % random.choice(adj_list)) 
    print("Some have a %s mane of hair and others have a %s %s on their head." % (random.choice(adj_list), random.choice(adj_list), random.choice(noun_list))) 
    print("I would love %s a unicorn one day." % random.choice(verb_list))

    if click.confirm("\nDo you want to have it filled out again?"):
        print("\nOkay, here we go!")
    else:
        input('\nOkay! Hit enter to go back to the main menu')
        click.clear()
        break