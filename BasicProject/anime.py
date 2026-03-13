import numpy as np
import pandas as pd


df = pd.DataFrame(pd.read_csv("E:\\anime.csv"))

# print(df.head()) # Display the first five row
# print(df.loc[1])

def extract_episodes(txt):
    check = False
    data = ""

    for i in txt:
        if check and i == ")":
            break
        if check:
            data += i
        if i == "(":
            check = True
    return data

df['Episodes'] = df['Title'].apply(extract_episodes)
# print(df)

df['Episodes'] = df['Episodes'].str.replace(' eps', '')
# print(df)

df['Episodes'] = df['Episodes'].astype(int) 
# print(df)

# print(df['Episodes'].dtype)


def extracttime(txt):
    data = ""
    start = False

    for i in txt:
        if i == ")":      
            start = True
            continue
        
        if start:
            if i.isdigit() and len(data) > 18:  
                break
            data += i

    return data.strip()

df['Time'] = df['Title'].apply(extracttime)
# print(df[['Title','Time']])

max_ep = df['Episodes'].max()
print(max_ep)