#region Imports
import os
import datetime

from get_dict import get_dict
from find_solution import find_solution
#endregion


if __name__ == "__main__":
    #region Setup
    os.system("cls" if os.name == "nt" else "clear")
    start_time = datetime.datetime.now()

    print("\n\n\nWordle process started at: " + str(start_time))
    print("####################################################")
    #endregion

    #region Load words and setup word_dict
    words_dict = get_dict(True)
    words_set = set(words_dict.keys())
    #endregion

    #region Add possible word-combinations to word_dict
    find_solution(words_dict, words_set, False)
    #endregion

    end_time = datetime.datetime.now()
    print("\n####################################################")
    print("Wordle process completed in " + str(end_time - start_time))