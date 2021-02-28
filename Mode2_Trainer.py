import click
import runpy
import random
from Data import create_outputfile
from Data import return_dict
from Data import return_vocab
from Data import return_words_german
from Data import return_words_english

# Explanation vocabulary trainer
print(" ")
print(10*"-", "VOCABULARY TRAINER", 10*"-")
print("\nIn this mode we will test some vocabulary")
print("This means the app will provide a german word and you have to type in the english translation or the other way around.")
print("The app will continue to run, until you enter 'stop'")
if click.confirm("\nAre you ready?"):
    print("Okay, here we go!")
else:
    input('\nOkay! Hit enter to go back to the mode 2 menu')
    click.clear()
    runpy.run_path("Mode2_Menu.py")

data_csv = create_outputfile()
all_words_dict = return_dict()
all_words = return_vocab()
words_german = return_words_german(data_csv)
words_english = return_words_english(data_csv)
            
# Set counters for evaluation of this run
wrong = 0
correct = 0
word_counter = 0

# Here starts vocab trainer with a randomly chosen word to translate 
while True:
    i = random.randint(0, len(all_words)-1)
    user_answer = click.prompt("\nTranslation of " + all_words[i])

    # from german to english
    if all_words[i] in words_german:
        if user_answer == all_words_dict.get(all_words[i]):
            click.secho('\nRight!', fg="green")
            correct += 1
            # 
            pos = data_csv[data_csv['German'] == all_words[i]].index.tolist()[0]
            data_csv.at[pos, 'correct_count'] = int(data_csv.at[pos, 'correct_count']) +1
        elif user_answer == 'stop':
            break
        else:
            click.secho('\nSorry, this is wrong.', fg="red")
            wrong += 1
            pos = data_csv[data_csv['German'] == all_words[i]].index.tolist()[0]
            data_csv.at[pos, 'wrong_count'] = int(data_csv.at[pos, 'wrong_count']) +1
            print('\nThe correct answer is %s.' % all_words_dict.get(all_words[i]))

    # from english to german              
    elif all_words[i] in words_english:
        correct_answer = list(all_words_dict.keys())[list(all_words_dict.values()).index(all_words[i])]
        if user_answer == correct_answer:
            click.secho('\nRight!', fg="green")
            correct += 1
            pos = data_csv.index[data_csv['English'] == all_words[i]].tolist()[0]
            data_csv.at[pos, 'correct_count'] +1 
        elif user_answer == 'stop':
            break
        else:
            click.secho('\nSorry, this is wrong', fg="red")
            wrong += 1
            pos = data_csv.index[data_csv['English'] == all_words[i]].tolist()[0]
            data_csv.at[pos, 'wrong_count'] = data_csv.at[pos, 'wrong_count'] + 1
            print('\nThe correct answer is %s.' % correct_answer)
                
    word_counter += 1

data_csv.at[0,'total_count'] = int(data_csv.at[0,'total_count']) + 1
data_csv.to_csv('output.csv', index=None, sep=r';')

# Evaluation of last test round
print(" ")
print("-" * 5)
print("Here is your evaluation for the last run:")
print("Correct words: %d of %d" % (correct, word_counter))
print("Wrong words: %d of %d" % (wrong, word_counter))

input('\nHit enter to go back to the mode 2 menu')
click.clear()
runpy.run_path("Mode2_Menu.py")