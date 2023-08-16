#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) advantage of functions
#functions are in structured and organized manner.They provide reusability(we can call them whenever needed)readability(well named)and mainability(to fix a bug we can just focus on the relevant code without affecting the rest of the code)


# In[2]:


#2) when we call a function it's gonna execute not when it is specified


# In[5]:


#3) def creates a function
#def class(name)
#here class is a function


# In[6]:


#4) "function" mainly performs a specific task while "function call" execute the code inside that funtion


# In[7]:


#5) there is only one "global scope" while in global scope there is so many "local scopes"


# In[8]:


#6) when the function call returns  the variable inside the local scope will be  destroyed.


# In[9]:


#7) return value in function means we can provide that value again to the caller when the function is executed.It can also be used in expressions ,assignments etc.


# In[10]:


#8) f a function does not have a return statement, the return value of a call to that function is "None"


# In[12]:


#9) to make a function variable to global variable we use "global keyboard"  
global_var = 10  # This is a global variable

def modify_global():
    global global_var  # Declare the global variable
    global_var = 20  #Update the global variable within the function

print(global_var)  
modify_global()    
print(global_var)  


# In[13]:


#10) The data type of None is called "NoneType".
x = None
print(type(x))  


# In[14]:


#11) areallyourpetsnamederic means  the "import "statement to bring external modules or packages into your code, allowing you to access their functions, classes, and variables.  


# In[5]:


#12) spam is module name and bacon() is called function name
#import spam
#spam.bacon()



# In[2]:


#13) to save a programme from crashing we can use exception handling and aslo can use  logging


# In[3]:


#14) The try clause is used to enclose the code that might raise an exception.


# In[ ]:




