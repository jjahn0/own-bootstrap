import csv
import pandas as pd
import numpy as np
import os
import random as rd

file = os.path.join('Resources','owm_citylist.txt')
owm_df = pd.read_csv(file, delimiter='\t')

def lat_random_select(number):
    range_num = int(number+7/7)
    id_list = []
    lat_list = []
    nm_list = []
    column_names = ['City', 'ID', 'Latitude']
    id_df = pd.DataFrame(columns=column_names)
    lat = np.arange(-60,100,20)
    for deg in range(1,len(lat)):
        range_ls = list(owm_df.loc[(owm_df['lat'] > lat[deg-1]) & (owm_df['lat'] <= lat[deg]),:]['id'])
        selections = rd.sample(range_ls, range_num)
        id_list = id_list + selections
    for city_id in ls:
        selection = owm_df.loc[owm_df['id'] == city_id]
        name = list(selection['nm'])[0]
        lat = float(selection['lat'])
        lat_list.append(lat)
        nm_list.append(name)
    id_df['City'] = nm_list
    id_df['ID'] = ls
    id_df['Latitude'] = lat_list
    return id_df