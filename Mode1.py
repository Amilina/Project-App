import click
from Data import create_outputfile
from Data import return_dict
from Data import return_words_german
from Data import return_words_english

print(" ")
print(10*"-", "DICTIONARY", 10*"-")
print("\nIn this mode we will emulate a dictionary")
print("This means you either type in a german or english word and the app will show you the translation.")
print("Okay, so lets go!")

data_csv = create_outputfile()
all_words_dict = return_dict()
words_german = return_words_german(data_csv)
words_english = return_words_english(data_csv)

while True:
    input_user = input("\nType a word you want to translate: ")
    # comparing the user input with the lists
    if input_user in words_german:
        german_translated = all_words_dict.get(input_user)
        print('\nThe translation of %s is %s' % (input_user, german_translated))
    elif input_user in words_english:
        english_translated = list(all_words_dict.keys())[list(all_words_dict.values()).index(input_user)]
        print('\nThe translation of %s is %s' % (input_user, english_translated))
    else:
        print('\nSorry this word is not in the dictionary')
    if click.confirm('\nDo you want to translate another one?'):
        print('\nOkay, here we go!')
    else:
        input('\nOkay! Hit enter to go back to the main menu')
        click.clear()
        break
