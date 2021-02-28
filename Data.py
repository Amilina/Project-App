import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas
import click
import random
import runpy
from os import path

def create_outputfile():
    # Check if output file already exist
    if path.isfile('output.csv'):
        # If yes, read output file
        data_csv = pandas.read_csv('output.csv', sep=';')
    else:
        # If not, create a new (csv) file from the txt file to save progress
        input_file = pandas.read_csv('words.txt', header = None, sep=r'\s*,\s*', engine='python')
        input_file.columns = ['German', 'Type of speech', 'English']
        input_file['correct_count'] = 0
        input_file['wrong_count'] = 0
        input_file['total_count'] = 0
        input_file['Type of speech'] = input_file['Type of speech'].str.replace("[(),]", "")
        input_file.to_csv('output.csv', index=None, sep=r';')
        data_csv = pandas.read_csv('output.csv', sep=';')
    return data_csv

# Create list with german words
def return_words_german(data_csv):
    words_german = data_csv.German.to_list()
    return words_german

# Create list with english words
def return_words_english(data_csv):
    words_english = data_csv.English.to_list()
    words_english = [x.strip(' ') for x in words_english]
    return words_english

# Create dictionary with german and english words
def return_dict():
    data_csv = create_outputfile()
    words_german = return_words_german(data_csv)
    words_english = return_words_english(data_csv)
    all_words_dict = dict(zip(words_german, words_english))
    return all_words_dict

# Check user process for vocab trainer
def return_vocab():
    data_csv = create_outputfile()
    all_words_dict = return_dict()
    all_words = []
    if data_csv.at[0, 'total_count'] <= 10:
        # If vocab trainer was used less than 10 times, probability that words will be used is the same for every word
        for key, value in all_words_dict.items():
            all_words.append(key)
            all_words.append(value)
    else:
        # If vocab trainer was used more than 10 times, probability that words will be used is higher for wrong words
        correct_df = data_csv[data_csv['correct_count'] > data_csv['wrong_count']]
        c_words_german = correct_df.German.to_list()
        c_words_english = correct_df.English.to_list()
        c_words_english = [x.strip(' ') for x in c_words_english]
        c_all_words = c_words_german + c_words_english

        wrong_df = data_csv[data_csv['wrong_count'] >= data_csv['correct_count']]
        w_words_german = wrong_df.German.to_list()
        w_words_english = wrong_df.English.to_list()
        w_words_english = [x.strip(' ') for x in w_words_english]
        w_all_words = w_words_german * 2 + w_words_english * 2

        all_words = c_all_words + w_all_words
    return all_words