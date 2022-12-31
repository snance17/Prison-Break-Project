#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes

# We begin by importing some helper functions.

# In[19]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[22]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'


# In[23]:


data = data_from_url(url)


# Let's print the first three rows

# In[24]:


print(data[0:2])


# In[25]:


index = 0
for row in data:
    data[index] = row[0:4]
    index += 1
print(data[0:3])


# In[26]:


for row in data:
    row[0] = fetch_year(row[0])
print(data[0:3])


# In[30]:


years = []
for row in data:
    years.append(row[0])
print(years)


# In[33]:


unique_years = []

for year in years:
    
    if year in unique_years:
        pass
    else:
        unique_years.append(year)
print(unique_years)


# In[34]:


attempts_per_year = []
for year in unique_years:
    attempts_per_year.append([year,0])
print(attempts_per_year)


# In[35]:


for ya in attempts_per_year:
    for year in years:
        if ya[0] == year:
            ya[1] += 1
print(attempts_per_year)


# In which year did the most attempts at breaking out of prison with a helicopter occur?

# In[36]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[37]:


countries_frequency = df["Country"].value_counts()
print_pretty_table(countries_frequency)


# In[ ]:




