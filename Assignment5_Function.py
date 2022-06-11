#!/usr/bin/env python
# coding: utf-8

# ###### Q1.try to print a prime number in between 1 to 100

# In[7]:


def prime(number):
    """ This function is for printing all prime numbers between given range"""
    print("prime numbers between range {} and {} are ".format(1,number))
    for i in range(number) :
        l=[]
        if i > 10 :
            if i % 2 != 0 and i % 3 != 0 and i%4 != 0 and i%5 != 0 and i%6 != 0 and i%7 != 0 and i%8 != 0 and i%9 != 0:
                print(i)
        else :
            if i == 2 or i == 3 or i == 5 or i == 7 :
                print(i)


# In[8]:


prime(100)


# ###### Q2.try to write a function which is equavalent to print in python

# ###### Q3.try to write a function which is replica of list append, extend and pop function

# In[29]:


#this is insert function in list
def insert(*a,b=[],i) :
    """This is INSERT function in list
       provide list, value/values/another list to be inserted 
       also provide the place(index) where you want to insert"""
    empty_list = list(a)
    if i <= len(list(a)) :
        empty_list[i] = b
        return empty_list
    else :
        print("please provide the valid index number to insert") 
# this is extend function in list
def extnd(*a,b=[]) :
    """This is extend function, where you can give your first list and second list/value/values to be extended"""
    return list(a) + b
#this is append function in list
def appnd(*a,b=[]) :
    return list(a), b
# this is pop function in list
def pop(*list1,index,start_point,slice) :
    """ This is pop function in list. provide list, index, starting point
        ,slicing method"""
    if slice == 'y' :
        list2 = list(list1)
        list2[start_point : index] = []
        return list2
    else :
        list2 = list(list1)
        list2[index] = []
        return list2


# In[16]:


insert(1,2,3,4,5,6,b=[12,13,14,15],i=10)


# In[19]:


extnd(1,2,3,4,b=["name","city"])


# In[25]:


appnd(1,2,3,4,5,b=["name","city"])


# In[30]:


pop(1, 2, 3, [11, 22, 33], 4, 5, 6, 7, [345, 345], [345, 345], 345, 345,index=4,start_point=0,slice='n')


# ###### q4.try to write a function which can return concatination of all the string that we will pass

# In[31]:


def concat(*string) :
    i = 0
    out_string = ""
    while i < len(list(string)) :
        out_string = out_string + string[i]
        i += 1
    print(out_string)


# In[36]:


concat("out:-","As long as the countdown variable is greater than zero,","the code keeps appending text without a trailing newline and t(hen goes to sleep for one second.","Finally, when the countdown is finished, it prints Go! and terminates the line.")


# ###### q4.try to write a lambda function which can return concatination of all the string that we will pass

# In[41]:


dummy=""
def concat1(*string) :
    i = 0
    out_string = ""
    while i < len(list(string)) :
        out_string = out_string + string[i]
        i += 1
    print(out_string)
(lambda dummy : concat1("1234","3456")) (dummy)


# ###### q5.try to write lambda function which can return list of all data beween 1 - 100

# In[45]:


l= lambda i : [i for i in range(i)]
l(100)


# ###### q6.try to write a 10 different exampe of lambda function with choice of your tasks

# ##### q6.1. sum of all odd numbers between given range

# In[55]:


def func1(args) :
    sum = 0
    for i in range(args) :
        if i%2 != 0 :
            sum = sum + i
    print("sum of all odd numbers between 1 and {} is ".format(args),sum)
l = lambda count : func1(count)
l(100)


# ##### q6.2. sum of all even numbers between given range

# In[53]:


def func2(args) :
    sum = 0
    for i in range(args) :
        if i%2 == 0 :
            sum = sum + i
    print("sum of all even numbers between 1 and {} is " .format(args), sum)
l = lambda count : func2(count)
l(100)


# ##### q6.3.factorial of given number

# In[60]:


def fact(args) : 
    i = 1
    facto = args
    while i < args :
        facto = facto * (args - i)
        i = i + 1
    print(facto)


# In[62]:


l = lambda number : fact(number)
l(40)


# ###### q7.try to write a function which can perform a read operationfrom .txt file

# In[63]:


def read(args,mode) :
    file = open(args,mode)
    print(file.read())
    print() 


# In[64]:


read("testfile","r")

