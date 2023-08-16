#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1)empty dic
empty_dic={}


# In[3]:


#2)with the key foo and value 42
my_dict = {'foo': 42}
value = my_dict['foo']
print(value) 


# In[4]:


#4)if we try to access a key that doesn't exist in the dictionary .It'll show KeyError
spam = {'bar': 100}
value = spam['foo']  


# In[5]:


#3)diff b/w list and dictionaries
#Dictionary                                  list
#unordered and mutuable                      ordered and mutuable


# In[3]:


#5)cat in spam : it checks whether the key is present in the dictionary  or not regargless of associated value
#spam = {'cat': 42, 'dog': 37, 'fish': 12}
#result = 'cat' in spam.keys
#spam.keys(): This expression checks whether the key 'cat' exists in the keys of the dictionary

#spam = {'cat': 42, 'dog': 37, 'fish': 12}
#result = 'cat' in spam  
#both will give the same result


# In[2]:


#6)cat' in spam checks if 'cat' is a key in the dictionary.
#'cat' in spam.values() checks if 'cat' is a value in the dictionary.


# In[11]:


#7)spam.setdefault('color', 'black')


# In[12]:


#8)
import json

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Pretty print the dictionary with an indentation of 4 spaces
pretty_printed = json.dumps(my_dict, indent=4)

print(pretty_printed)


# In[ ]:




