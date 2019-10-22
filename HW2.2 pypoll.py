#!/usr/bin/env python
# coding: utf-8

# In[45]:


import os
import pandas as pd


# In[46]:


poll_data = pd.read_csv("/Users/cla/Desktop/UM Data Science/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")


# In[47]:


poll_data.head()


# In[48]:


total_votes = poll_data.County.count()
total_votes


# In[49]:


candidates_list = poll_data['Candidate'].unique()
candidates_list


# In[ ]:





# In[50]:


khan_votes = poll_data.loc[poll_data.Candidate == 'Khan', 'Candidate'].count()
correy_votes = poll_data.loc[poll_data.Candidate == 'Correy', 'Candidate'].count()
li_votes = poll_data.loc[poll_data.Candidate == 'Li', 'Candidate'].count()
tooley_votes = poll_data.loc[poll_data.Candidate == "O'Tooley", "Candidate"].count()

print("Khan: " + str(khan_votes) + " votes")
print("Correy: " + str(correy_votes) + " votes")
print("Li: " + str(li_votes) + " votes")
print("Tooley: " + str(tooley_votes) + " votes")


# In[51]:


khan_percent = round((khan_votes/total_votes) * 100,2)
correy_percent = round((correy_votes/total_votes) * 100,2)
li_percent = round((li_votes/total_votes) * 100,2)
tooley_percent = round((tooley_votes/total_votes) * 100,2)

print("Khan: " + str(khan_percent) + "%")
print("Correy: " + str(correy_percent) + " %")
print("Li: " + str(li_percent) + " %")
print("Tooley: " + str(tooley_percent) + " %")


# In[52]:


print('                   Election Results')
print('--------------------------------------------------------')
print(f'Total Votes: {total_votes}')
print('                            ')
print(f'Khan: {khan_percent}% ({khan_votes })')
print(f'Correy: {correy_percent}% ({correy_votes})')
print(f'Li: {li_percent}% ({li_votes})')
print("O'Tooley: " + str(tooley_percent) +"%"+"("+ str(tooley_votes)+")")
print('                            ')
print('--------------------------------------------------------')
print('                     The Winner is Khan')
print('--------------------------------------------------------')


# In[62]:


x1 = ('                   Election Results')
x2 = ('--------------------------------------------------------')
xd = ('                            ')
x3 = (f'Total Votes: {total_votes}')
x4 = ('                            ')
x5 = (f'Khan: {khan_percent}% ({khan_votes })')
x6 = (f'Correy: {correy_percent}% ({correy_votes})')
x7 = (f'Li: {li_percent}% ({li_votes})')
x8 = ("O'Tooley: " + str(tooley_percent) +"%"+"("+ str(tooley_votes)+")")
x9 = ('                            ')
x10 = ('--------------------------------------------------------')
x11 = ('                     And the winner is... Khan !!')
x12 = ('--------------------------------------------------------')


# In[63]:


result2 = {'str': [x1,x2,xd,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]}
      
output2 = pd.DataFrame(result2)

output2.to_csv('Py_poll.txt',header=False,index=False)


# In[ ]:





# In[ ]:





# In[ ]:




