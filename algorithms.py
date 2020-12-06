# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 15:02:43 2020

@author: AKINTOLA
"""
import numpy as np
import pandas as pd


''' Generating 10 random integer numbers between 0 - 20 
 to populate the price and unit field
 '''
 
price = np.random.randint(20, size = 10 )
unit = np.random.randint(5, size = 10 )
product = []


count = 0
while count < len(price):
    name = input('Enter products name: ')
    product.append(name)
    count = count + 1

dictionary = {
            'product name': product,
            'price': price,
            'unit': unit,
        }

df = pd.DataFrame(dictionary)
df

# where 20 happens to be the threshold  
df['prediction'] = df['price'].apply(lambda x: 1 if x > len(price) else 0 )


