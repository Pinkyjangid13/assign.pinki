#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) keywords are prereserved words that can't be used as identifiers such as variable names class name etc.
import keyword
all_keywords = keyword.kwlist
print(all_keywords)


# In[2]:


#2) rules to create variables in python
#a) variable name should start with letters(a-z,A-Z)or underscore(_) 
#b) after the letters we can use digits(1,2...)
#c) variables name can't start with digits


# In[1]:


#3) for the nomencluture of variables 
# use snake_case(lower case letters i.e variable_name )
#use meaningful name i.e total_count not as tc
#Do not use names of built-in functions, classes, or keywords as variable names


# In[2]:


#4) if we use keywords as variables names then it'll result a syntax error.
if = 42  
#it'll result a syntax error bcz if is  a preresvered keyword


# In[7]:


#5) def is used to define functions.
#def function_name():


# In[6]:


#6) '/'(backsalsh) 


# In[9]:


#7) 
#(a) Homogeneous list: a list where all the elements have the same data types such as int,float,strings etc.
integer_list = [1,2,3,4,5]

#(b) heterogeneous set:  a set where the elements can have different data types. Unlike a list, which can contain element
heterogeneous_set = {1, "apple", 3.14, (1, 2, 3)}

#(c)A homogeneous tuple: a tuple where all the elements have the same data type. 


# In[11]:


#8) mutuable data types:Mutable data types are those where the value stored in the memory location can be modified without changing the memory location itself
#examples: list,dictionaries and sets 
my_list=[1,2,3,4,5]
my_list[1]=90
print(my_list)

#immutuable data types: where the value stored in memory location can't be changed after it is created.
#examples:integers,floats,strings and tuples
my_string = "hello"
new_string = my_string.upper()  
print(my_string)   
print(new_string) # it has changed to new string 



# In[8]:


#9) 
for i in range(5):
    for j in range(i+1):
        
        print('*', end=' ')
    
    print()


# In[16]:


#10)
rows = 5
while rows>0:
    for i in range(rows):
        print("|",end='')
     
    print()
    
    rows -=1


# In[ ]:




