import click

print(" ")
print(10*"-", "GRAMMAR", 10*"-")
print("\nIn this mode we will train some basic german grammar.")
print("This means you type in some german text that consists of several sentences.")
print("The sentences should only contain a pronoun, the verb 'to be' and an adjective.")
print("Okay, so lets go!\n")

while True:
    user_text = input("Type some German sentences: ")

    #slice user input into sentences
    sliced_text = user_text.split('. ')
    

    word_list = ['Ich', 'Du', 'Er', 'Sie', 'Es', 'Wir', 'Ihr', 'Sie']
    word_list_2 = ['Ich bin', 'Du bist', 'Er ist', 'Sie ist', 'Es ist', 'Wir sind', 'Ihr seid', 'Sie sind']

    new_string = ''
    
    for sentence in sliced_text:
        sentence = sentence.replace(".", "")
        first_word = sentence.split()
        first_word = first_word[0]
        if first_word in word_list:
            new_string = sentence.split()
            first_two_words = new_string[0] + ' ' + new_string[1]
            if first_two_words in word_list_2:
                print('\n%s: correct' % sentence)
            else:
                print('\n%s: wrong' % sentence)
                if new_string[0] in word_list:
                    pos = word_list.index(new_string[0])
                    correct_type = word_list_2[pos]
                    last_word = new_string[-1]
                    print('Correct would be:', correct_type, last_word)
        else:
            print("\n%s: This is not a valid input." % sentence)
            
    if click.confirm('\nDo you want to do another test?'):
        print('\nOkay, here we go!')
    else:
        input('\nOkay! Hit enter to go back to the main menu')
        click.clear()
        break