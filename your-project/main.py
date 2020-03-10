import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import hashlib
import json
import random
from cleaning import *

if __name__ == '__main__':
    print('It’s good to meet you')
    # Acquisition // The path is always ../data
    tkd_data = pd.read_csv('Taekwondo_Technique_Classification_Stats.csv')
    original_data = pd.read_csv('Taekwondo_Technique_Classification_Stats.csv')
    tkd_data.head()

    # Wrangling
    lower = -10
    upper = 20
    roll = 2
    final_df = cleaner(tkd_data, lower, upper, roll)
    
#    final_df.to_csv('CSVs/marvel_cleaned.csv', sep = ';', index = False)

    # Analysis
#    final_df.describe().to_csv('CSVs/marvel_describe.csv')
    
    # Doing a multi-graph figure
    graphing(final_df, lower, upper, roll)

    # keep_on = True
    # while keep_on:
    #     dict_test = {"good": 0 , "bad": 1, "neutral" : 0 , "male": 0 , "female": 1, 'all': 2 }
    #     gender, alignment = ask_input(dict_test)
    #     selected_df = df_selection(final_df, dict_test[gender], dict_test[alignment])        
    #     graphing(selected_df, 'marvel_'+alignment+'_'+gender)

    #     print(selected_df.describe())
    # Reporting