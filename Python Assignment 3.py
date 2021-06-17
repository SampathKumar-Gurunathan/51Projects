# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:10:00 2021

@author: sampathkumar
"""
# Import the Data
import pandas as pd
pd.set_option('display.max_rows',10)
df = pd.read_csv("C:/Users/Dell/Desktop/Practice/titles.csv")
df.head(10)
df.describe()

# How many movies are listed in the titles dataframe?
df['title'].nunique()

# What are the earliest two films listed in the titles dataframe?
df.loc[df['year'] == df["year"].min(),'title']

# How many movies have the title "Hamlet"?
len(df.loc[df['title'] == "Hamlet"])
len(df.query('title == "Hamlet"'))

# How many movies are titled "North by Northwest"?
len(df.loc[df['title'] == "North by Northwest"])
len(df.query('title == "North by Northwest"'))

# When was the first movie titled "Hamlet" made?
df.loc[df['title'] == "Hamlet",'year'].min()
df_new = df.query('title == "Hamlet"')
df_new["year"].min()

# List all of the "Treasure Island" movies from earliest to most recent.
df_new = df.loc[df['title'] == "Treasure Island",['title','year']]
df_new.sort_values('year',ascending = True)
df_new = df.query('title == "Treasure Island"')
df_new.sort_values('year',ascending = True)

# How many movies were made in the year 1950?
len(df.loc[df['year'] == 1950])
len(df.query("year==1950"))

# How many movies were made in the year 1960?
len(df.loc[df['year'] == 1960])
len(df.query("year==1960"))

# How many movies were made from 1950 through 1959?
len(df.loc[(df['year'] >= 1950) & (df['year'] <= 1959)])
len(df.query("year>=1950 and year<=1959"))

# In what years has a movie titled "Batman" been released?
df.loc[df['title'] == "Batman", 'year']

df = pd.read_csv("C:/Users/Dell/Desktop/Practice/cast.csv")
df.head()
# How many roles were there in the movie "Inception"?
df.loc[df['title'] == "Inception", ['name','type']]
len(df.loc[df['title'] == "Inception", 'type'])

# How many roles in the movie "Inception" are NOT ranked by an "n" value?
df_new = df.fillna(0)
len(df_new.loc[(df_new['title'] == "Inception") & (df_new['n'] == 0)])

# But how many roles in the movie "Inception" did receive an "n" value?
len(df_new.loc[(df_new['title'] == "Inception") & (df_new['n'] != 0)])

# Display the cast of "North by Northwest" in their correct "n"-value order, 
# ignoring roles that did not earn a numeric "n" value.
df_new.loc[(df_new['title'] == "North by Northwest") & (df_new['n'] != 0)].sort_values('n')

# Display the entire cast, in "n"-order, of the 1972 film "Sleuth".
df_new.loc[(df_new['title'] == "Sleuth") & (df_new['year'] == 1972)].sort_values('n')

# Now display the entire cast, in "n"-order, of the 2007 version of "Sleuth".
df_new.loc[(df_new['title'] == "Sleuth") & (df_new['year'] == 2007)].sort_values('n')

# How many roles were credited in the silent 1921 version of Hamlet?
len(df_new.loc[(df_new['title'] == "Hamlet") & (df_new['year'] == 1921),'character'])

# How many roles were credited in Branagh’s 1996 Hamlet?
len(df_new.loc[(df_new['title'] == "Hamlet") & (df_new['year'] == 1996),'character'])

# How many "Hamlet" roles have been listed in all film credits through history?
len(df_new.loc[df_new['title'] == "Hamlet",'character'])

# How many people have played an "Ophelia"?
len(df_new.loc[(df_new['character'] == "Ophelia")])

# How many people have played a role called "The Dude"?
len(df_new.loc[(df_new['character'] == "The Dude")])

# How many people have played a role called "The Stranger"?
len(df_new.loc[(df_new['character'] == "The Stranger")])

# How many roles has Sidney Poitier played throughout his career?
df_new.loc[(df_new['name'] == "Sidney Poitier"),'character'].nunique()

# How many roles has Judi Dench played?
df_new.loc[(df_new['name'] == "Judi Dench"),'character'].nunique()

# List the supporting roles (having n=2) played by Cary Grant in the 1940s, in order by year.
df_new.loc[(df_new['name'] == "Cary Grant") & (df_new['n'] == 2) & 
           (df_new['year'] >= 1940) & (df_new['year'] <= 1949),['character','year']].sort_values('year')

# List the leading roles that Cary Grant played in the 1940s in order by year.
df_new.loc[(df_new['name'] == "Cary Grant") & (df_new['year'] >= 1940) & 
           (df_new['year'] <= 1949),['character','year']].sort_values('year')

# How many roles were available for actors in the 1950s?
df_new.loc[(df_new['year'] >= 1950) & (df_new['year'] <= 1959) 
           & (df_new['type'] == 'actor'),'character'].nunique()

# How many roles were available for actresses in the 1950s?
df_new.loc[(df_new['year'] >= 1950) & (df_new['year'] <= 1959) 
           & (df_new['type'] == 'actress'),'character'].nunique()

# How many leading roles (n=1) were available from the beginning of film history through 1980?
df_new.loc[(df_new['year'] >= df_new['year'].min()) & (df_new['year'] <= 1989) 
           & (df_new['n'] == 1),'character'].count()

# How many non-leading roles were available through from the beginning of film history through 1980?
df_new.loc[(df_new['year'] >= df_new['year'].min()) & (df_new['year'] <= 1989) 
           & (df_new['n'] != 1),'character'].count()

# How many roles through 1980 were minor enough that they did not warrant a numeric "n" rank?
df_new.loc[(df_new['year'] >= 1980) & (df_new['year'] <= 1989) 
           & (df_new['n'] == 0),'character'].count()

