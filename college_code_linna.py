#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:12:32 2017

@author: linnaha
"""

import pandas as pd 
import matplotlib.pyplot as plt


url1 = "https://raw.githubusercontent.com/fivethirtyeight/data/master/"
url2 = url1 + "college-majors/recent-grads.csv"

college = pd.read_csv(url2) #put into data frame
print(college.columns)
college.columns = [var.lower() for var in college.columns]
print(college.columns)
#%%
college["percent_women"] = college["sharewomen"] * 100 #how can we do this using a for loop?

#%%
wmajors= college[["percent_women","major"]] #created a smaller dataset from the larger set

wmajors = wmajors.sort_values(by="percent_women")
#%%

wm2= wmajors.head(20) #created an even smaller data set.. now how to sort by percentage?
wm2.set_index("percent_women", inplace = True) #set index as percentage
wm2= wm2.sort_index() #sort by lowest to highest 

#%%
fig, ax = plt.subplots()
wm2["percent_women"].plot(ax = ax)


ax.set_title("Share of Women in Majors", fontsize = 14, fontweight = "bold") 
ax.set_ylabel("Percentage of women", fontsize = 14,)
ax.set_xlabel("Major", fontsize = 14,)

#why is it not showing major names?

#%% #let's try a bar graph

fig, ax = plt.subplots()
wm2.plot(kind='barh', ax=ax)

fig, ax = plt.subplots()
wm2[["percent_women","major"]].plot(kind='barh', ax=ax)

#still not showing major names

