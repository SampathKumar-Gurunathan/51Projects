# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:17:19 2021

@author: sampathkumar
"""
import pandas as pd
df = pd.read_csv("C:/Users/Dell/Desktop/Practice/cast.csv")
df.head()
df_new = df.fillna(0)

# What are the ten most common movie names of all time?
mn = df_new['title'].value_counts()
mn.iloc[0:10]

# Which three years of the 1930s saw the most films released?
df_temp = df_new.loc[(df_new['year'] >= 1930) & (df_new['year'] <= 1939)]
yc = df_temp['year'].value_counts()
yc.iloc[0:3]

# Plot the number of films that have been released each decade over the history of cinema.
import seaborn as sb
import matplotlib.pyplot as pt
df_temp = df_new
df_temp['Decade'] = df_temp.year // 10*10
sb.countplot(x = 'Decade',data = df_temp)

# Plot the number of "Hamlet" films made each decade.
df_h = df_new.loc[(df_new['title'] == 'Hamlet')]
df_h['Decade'] = df_h.year // 10*10
sb.countplot(x = 'Decade',data = df_h)

# Plot the number of "Rustler" characters in each decade of the history of film.
df_r = df_new.loc[(df_new['character'] == 'Rustler')]
df_r['Decade'] = df_r.year // 10*10
sb.countplot(x = 'Decade',data = df_r)

# Plot the number of "Hamlet" characters each decade.
df_c = df_new.loc[(df_new['character'] == 'Hamlet')]
df_c['Decade'] = df_c.year // 10*10
sb.countplot(x = 'Decade',data = df_c)

# What are the 11 most common character names in movie history?
cn = df_new['character'].value_counts()
cn.iloc[0:11]

# Who are the 10 people most often credited as "Herself" in film history?
df_temp = df_new.loc[(df_new['character'] == 'Herself')]
cn = df_temp['name'].value_counts()
cn.iloc[0:10]

# Who are the 10 people most often credited as "Himself" in film history?
df_temp = df_new.loc[(df_new['character'] == 'Himself')]
cn = df_temp['name'].value_counts()
cn.iloc[0:10]

# Which actors or actresses appeared in the most movies in the year 1945?
df_temp = df_new.loc[((df_new['type'] == 'actor') | (df_new['type'] == 'actress')) & 
                     (df_new['year'] == 1945)]
an = df_temp['name'].value_counts()
an.iloc[0:1]

# Which actors or actresses appeared in the most movies in the year 1985?
df_temp = df_new.loc[((df_new['type'] == 'actor') | (df_new['type'] == 'actress')) & 
                     (df_new['year'] == 1985)]
an = df_temp['name'].value_counts()
an.iloc[0:1]

# Plot how many roles Mammootty has played in each year of his career.
import seaborn as sb
import matplotlib.pyplot as pt
df_temp = df_new.loc[df_new['name'] == 'Mammootty',['type','year']]
df_temp.head()
rm = sb.countplot(x = "year", data = df_temp)

# What are the 10 most frequent roles that start with the phrase "Patron in"?
df_temp = df_new.loc[df_new['character'].str.startswith('Patron in')]
tn = df_temp['character'].value_counts()
tn.iloc[0:10]

# What are the 10 most frequent roles that start with the word "Science"?
df_temp = df_new.loc[df_new['character'].str.startswith('Science')]
tn = df_temp['character'].value_counts()
tn.iloc[0:10]

# Plot the n-values of the roles that Judi Dench has played over her career.
import seaborn as sb
import matplotlib.pyplot as pt
df_temp = df_new.loc[(df_new['name'] == 'Judi Dench')]
sb.barplot(y = 'character', x = 'n', data = df_temp)

# Plot the n-values of Cary Grant's roles through his career.
import seaborn as sb
import matplotlib.pyplot as pt
df_temp = df_new.loc[(df_new['name'] == 'Cary Grant')]
sb.distplot(df_temp.n)

# Plot the n-value of the roles that Sidney Poitier has acted over the years.
import seaborn as sb
import matplotlib.pyplot as pt
df_temp = df_new.loc[(df_new['name'] == 'Sidney Poitier')]
sb.relplot(y = 'character', x = 'n', data = df_temp)

# How many leading (n=1) roles were available to actors, and how many to actresses, in the 1950s?
df_temp = df_new.loc[((df_new['type'] == 'actor') | (df_new['type'] == 'actress')) & 
                     (df_new['year'] >= 1950) & (df_new['year'] <= 1959) & (df_new['n'] == 1)]
df_temp['n'].value_counts()                                                

# How many supporting (n=2) roles were available to actors, and how many to actresses, in the 1950s?
df_temp = df_new.loc[((df_new['type'] == 'actor') | (df_new['type'] == 'actress')) & 
                     (df_new['year'] >= 1950) & (df_new['year'] <= 1959) & (df_new['n'] == 2)]
df_temp['n'].value_counts() 