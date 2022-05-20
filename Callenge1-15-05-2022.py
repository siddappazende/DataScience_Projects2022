#!/usr/bin/env python
# coding: utf-8

# # Challenge1_15/05/2022

# In[1]:


s = "this is My First Python programming class and i am learNING python string and its function"


# ###### 1 . Try to extract data from index one to index 300 with a jump of 3 

# In[2]:


s[1:300:3]


# ###### 2. Try to reverse a string without using reverse function 

# In[5]:


s[::-1]


# ###### 3. Try to split a string after conversion of entire string in uppercase 

# In[8]:


s.upper()


# In[9]:


s.split(' ')


# ###### 4. try to convert the whole string into lower case

# In[10]:


s.lower()


# ###### 5 . Try to capitalize the whole string 

# In[12]:


s.capitalize()


# ###### 6 . Write a diference between isalnum() and isalpha()

# isaknum() - This function checks if the entire string is combination of both numbers and alphabets
# isalpha() - This function checks if the entire string contains only alphabets and no numbers

# ###### 7. Try to give an example of expand tab

# In[29]:


s1="this\tis\tan\texample for expand tab"


# In[33]:


s1.expandtabs(2)


# ###### 8 . Give an example of strip , lstrip and rstrip 

# In[34]:


s2="       this is an example for strip     "


# In[35]:


s2.strip()


# In[36]:


s2.rstrip()


# In[37]:


s2.lstrip()


# ###### 9.  Replace a string charecter by another charector by taking your own example 

# In[52]:


s3="This is my example for replacing charecter in the string is is"


# In[53]:


s3.replace("is","IS")


# ###### 10 . Try  to give a defination of string center function with and exmple 

# In[54]:


s4="this is string centre example"


# In[58]:


s4.center(50,' ')


# string centre function is used keep the input string in the centre with given width and its filled with given single charecter before and after the input string

# ###### 11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language

# Both are required for a program written in any programming langauge into machine language(computer can understand, binary)
# but the main difference compiler reads entire programs once and converts it into machine language but the interpretor will read each
#     sentence at a time and converts it into machine understndable language.

# ###### 12 . Python is a interpreted of compiled language give a clear ans with your understanding

# As we know that any code is written by a programmer needs to be converted into machine understandable language either through compiler
# or through interpretor. Python language is comipled first then interpreted. whenever we execute the python code it first compiles
# and it hides or deltes the compiled part in the background,it start executing in interpreted mode for us.

# ###### 13 . Try to write a usecase of python with your understanding.

# python is a high level language(english like language), interpreted nature,open sourceand its vast varity of libraries, beacuse of 
# all these advantages python is widely preferred language and used every where including, web development,Gaming, AI & ML, Education sector
# , Finance sector, Automation, Retail etc.
