import random as rd
import numpy as np

lat_lng_ranges = [[(-60,-40),(-80,-60),(160,180)],
                   [(-40,-20),(-80,-40),(10,50),(110,180)],
                   [(-20,0),(-80,-30),(10,50),(110,170)],
                   [(0,20),(-80,-30),(-20,60),(70,130)],
                   [(20,40),(-130,-70),(-20,70),(70,150)],
                   [(40,60),(-180,-150),(-140,-50),(-10,170)],
                   [(60,80),(-180,0),(0,180)]]

lat_long_list = []

def random_cords (sample_number):
    while len(lat_long_list) < 1000:
        for ln in lat_lng_ranges:
            for i in range(1,len(ln)):
                lat_long_list.append( [rd.randint(ln[0][0],ln[0][1]), rd.randint(ln[i][0],ln[i][1])] )
    cords = rd.sample(lat_long_list,sample_number)
    return cords