#region Imports
import os
import sys
import pickle
#endregion

#region Helper functions

# Loads the words from a file into a set and returns it
def load_words_file(file_path, print_info=False):
    word_dict = dict()
    with open(file_path) as word_file:
        words = set(word_file.read().split())
        for word in words:
            word_dict[word.lower()] = dict()

    if(print_info):
        print(file_path + " loaded")
        print("Words in file: " + str(len(word_dict)))

    return word_dict

# Loads the dictionary from a file via pickle serialization
def load_dic(print_info=False):
    with open("savestate\\words_dict.pickle", "rb") as word_file:
            words_dict = pickle.load(word_file)

    if(print_info):
        print("Existing dictionary loaded")
        print("Words in dictionary: " + str(len(words_dict)))

    return words_dict

# Creates the dictionary removes unnecessary files 
# and saves it to a file via pickle serialization
def create_dic(print_info=False):
    # Get all valid wordle guesses from the file
    word_file_url = "words_wordle_small.txt"
    words_dict = load_words_file("word_lists\\" + word_file_url)

    if(print_info):
        print("Wordle words: " + str(len(words_dict)))

    # Remove words from the dictionary that have the same letter at least twice
    words_dict_filtered = dict()
    for word in words_dict:
        if(len(word) is len(set(word))):
            words_dict_filtered[word] = words_dict[word]
    if(print_info):
        print("Wordle words (without multi-letter): " + str(len(words_dict_filtered)))

    # Remove words from the dictionary that are anagrams of other words
    words_dict_uniq = dict()
    for word in words_dict_filtered:
        word_sorted = "".join(sorted(word))
        if word not in words_dict_uniq:
            words_dict_uniq[word_sorted] = {"anagrams": [word], "comb_set": set()}
        else:
            words_dict_uniq[word_sorted]["anagrams"].append(word)
    if(print_info):
        print("Wordle words (without anagrams): " + str(len(words_dict_uniq)))

    # Save the dictionary to a file
    with open("savestate\\words_dict.pickle", "wb") as dic_file:
        pickle.dump(words_dict_uniq, dic_file)

    return words_dict_uniq
#endregion

#region MAIN: Find the solution
def get_dict(print_info):
    if(print_info):
        print("\nDictionary")
        print("-----------------------------------------------------")

    if os.path.isfile("savestate\\words_dict.pickle"):
        return load_dic(print_info)
    else:
        return create_dic(print_info)
#endregion