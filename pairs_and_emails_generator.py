#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:49:07 2022

@author: baptistelafoux
"""
import pandas as pd 
from itertools import product, permutations
import random 
from sklearn.utils import shuffle
from urllib.parse import quote
import webbrowser

sheet_url = 'https://docs.google.com/spreadsheets/d/1i5hRWAO--EMEOloPSciI-rpKYIwD85cX-op7cvR2U8c/edit#gid=324996868'
url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

df = pd.read_csv(url)

nfs = df[df[df.columns[-1]] == 'Non-French-speaker']
fs  = df[df[df.columns[-1]] == 'French-speaker']


def gen(email,):
    mailto(email, "[tandem] First tandem", body_template) 
    
for i, pair in enumerate(zip(shuffle(nfs).T, shuffle(fs).T)):
    #print(i, pair)
    
    df_temp = df.loc[list(pair)]
    
    
    body_template = f"""Hello {' & '.join(list(df_temp['First name']))} !

I am happy to announce that you will be together for the first sessions of tandem. 
As we discussed at the coffee meeting last week, you can meet once a week for 20-30min, to discuss a topic of your choice, in the language of your choice. 

I'll let you get in touch and agree on a time that suits you. Have fun!


The main objective is to improve the level of French of non-French speakers. If you wish, it is also the opportunity to learn the language of your interlocutor for French speakers. 

We would like to have a quick feedback on these first experiences in order to know what can be improved, so you can already note the date of Thursday, March 3rd for this meeting (14h30, after coffe meeting). 

Please feel free to get in touch with us if you have any trouble or question in the meantime. 

Best, 
Andrea & Baptiste"""


    gen(','.join(list(df_temp['Mail address '])))
        

def mailto(recipients, subject, body):
    webbrowser.open("mailto:%s?subject=%s&body=%s" %
        (recipients, quote(subject), quote(body)))


