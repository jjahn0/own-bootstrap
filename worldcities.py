import csv
import pandas as pd
import numpy as np
import os
import random as rd

file = os.path.join('Resources','worldcities.csv')
data = pd.read_csv(file)

def ran_select(number):
    range_num = int(number/7)
    city_list = []
    lat = np.arange(-60,100,20)
    for deg in range(1,len(lat)):
        range_ls = list(data.loc[(data['Latitude'] > lat[deg-1]) & (data['Latitude'] <= lat[deg]),:]['City'])
        selections = rd.sample(range_ls, range_num)
        city_list = city_list + selections
    return city_list