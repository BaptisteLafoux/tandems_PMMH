#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:49:07 2022

@author: baptistelafoux
"""
import pandas as pd 

from sklearn.utils import shuffle
from urllib.parse import quote
import webbrowser

gen_email = False

sheet_url = 'https://docs.google.com/spreadsheets/d/1i5hRWAO--EMEOloPSciI-rpKYIwD85cX-op7cvR2U8c/edit#gid=324996868'
url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

df = pd.read_csv(url)

nfs = df[df[df.columns[-1]] == 'Non-French-speaker']
fs  = df[df[df.columns[-1]] == 'French-speaker']

def mailto(recipients, subject, body):
    webbrowser.open("mailto:%s?subject=%s&body=%s" %
        (recipients, quote(subject), quote(body)))

def gen(email, body):
    mailto(email, "[tandem] First tandem", body) 
    
def body(names):
    return f"""
Hello {' & '.join(names)} !

I am happy to announce that you will be together for the first sessions of tandem. 
As we discussed at the coffee meeting last week, you can meet once a week for 20-30min, to discuss a topic of your choice, in the language of your choice. 

I'll let you get in touch and agree on a time that suits you. Have fun!


The main objective is to improve the level of French of non-French speakers. If you wish, it is also the opportunity to learn the language of your interlocutor for French speakers. 

We would like to have a quick feedback on these first experiences in order to know what can be improved, so you can already note the date of Thursday, March 3rd for this meeting (14h30, after coffe meeting). 

Please feel free to get in touch with us if you have any trouble or question in the meantime. 

Best, 
Andrea & Baptiste"""
    
def main():   
    
    pairs = list(zip(shuffle(nfs).T, shuffle(fs).T)) 
    
    for pair in pairs : print((df.loc[list(pair)]['First name'] + ' ' + df.loc[list(pair)]['Last Name']).values)
    
    answer = input('Want to keep these pairs and generate the emails ? [y/n]\t')
    if answer == 'y' : 
        pass
    elif answer == 'n':
        return None
    
    for i, pair in enumerate(pairs):
        
        df_temp = df.loc[list(pair)]
        
        names = list(df_temp['First name'])
        body_text = body(names)
        
        recipients = ','.join(list(df_temp['Mail address ']))
    
        if gen_email : gen(recipients, body_text)
            
        
if __name__ == '__main__':
    main()



