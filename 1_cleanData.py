'''
- Step 1: Clean Datasets
- Input folder: raw_datasets
- Output folder: cleaned_datasets
'''

import pandas as pd
import utils

'''Files'''
train_path='Suicide_Detection.csv', 
train_path2='suicide_notes.csv',
test_path='reddit_depression_suicidewatch.csv'

'''Input'''
path = train_path     ## Change this filename

''' Import'''
name = utils.convertTuple(path)
name = name.replace('.csv','')
df = pd.read_csv('raw_datasets/'+name+'.csv') 
#print(df.shape)
    
'''Processing'''
notes = df['text']
if name == 'Suicide_Detection':
    classfication = df['class']  
elif name == 'suicide_notes':
    df['class'] = 'suicide'
    classfication = 'suicide' 
elif name == 'reddit_depression_suicidewatch':
    df.loc[df['label'] == 'SuicideWatch', 'class'] = 'suicide'
    df.loc[df['label'] == 'depression', 'class'] = 'non-suicide'
    classfication = df['class']  

notesCleaned = pd.Series( [], dtype=str)

for i in range(0, len(notes)):
    each = (utils.a(notes[i]))
    if i%10000 == 0:
        print("At record = %s" %(i))
    notesCleaned[i] = each

df['notesCleaned'] = notesCleaned

'''Export'''
df.to_csv('cleaned_datasets/'+name+'.csv', index=False)

