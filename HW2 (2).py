#!/usr/bin/env python
# coding: utf-8

# In[142]:


import os
import pandas as pd


# In[143]:


budget_data = pd.read_csv("/Users/cla/Desktop/UM Data Science/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")


# In[144]:


#Testing the data:
budget_data.head()


# In[145]:


#Count of number of months:
Datecount = budget_data.Date.count()
Datecount


# In[146]:


#Net income for the period given:
NItotal = budget_data["Profit/Losses"].sum()
"$ " + str(NItotal)


# In[147]:


#Finding the change in profit/losses from month to month:
budget_data['Change in Profit/Losses'] = budget_data['Profit/Losses'] - budget_data['Profit/Losses'].shift(+1)
budget_data['Change in Profit/Losses'].round(decimals=2)
budget_data.head()




# In[148]:


#Finding the average change:
average1 = budget_data["Change in Profit/Losses"].mean()
average1 = "$ " + str(average1) 
average1


# In[149]:


#finding the max change:
maxchange = budget_data["Change in Profit/Losses"].max()
maxchangedate = budget_data.loc[budget_data['Change in Profit/Losses'] == 1926159.0 , 'Date'].iloc[0]


# In[150]:


#finding the min change:
minchange = budget_data["Change in Profit/Losses"].min()
minchangedate = budget_data.loc[budget_data['Change in Profit/Losses'] == -2196167.0 , 'Date'].iloc[0]


# In[151]:


#getting the summarized results:
x1 = ("Financial Analysis")
x2 = ("---------------------------------")
x3 = (" ")
x4 = ("Total months: " + str(Datecount))
x5 = ("Total : $" + str(NItotal))
x6 = ("Average Change: " + (average1))
x7 = "Greatest increase in profits: $" + str(maxchange) + " on " + str(maxchangedate)
x8 = "Greatest decrease in profits: $" + str(minchange) + " on " + str(minchangedate)

result1 = (print(x1),print(x2),print(x3),
print(x4),
print(x5),
print(x6),
print(x7),
print(x8))





# In[152]:


row = [x1,x2,x3,x4,x5,x6,x7,x8]
row



# In[153]:


#printing the results into a .txt file:
result = {'str': [x1,x2,x3,x4,x5,x6,x7,x8]}
      
output = pd.DataFrame(result)

output.to_csv('Py_bank.txt',header=False,index=False)


# In[ ]:





# In[ ]:




