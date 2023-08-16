#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) [] is a empty list

empty_list = []


# In[7]:


#2)
spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'       #it will assign to index 2


# In[ ]:


#['a' 'b' 'c' 'd'] for 3,4,5 ques


# In[10]:


#3) [int(int('3'*2)/11)] 
#steps:
#'3' is 3 
#and 3*2 is 33
#33/11 is 3
#['a' 'b' 'c' 'd']
##spam[3] == d


# In[11]:


#4) spam[-1]=d


# In[ ]:


#[3.14,'cat',11,'cat',True] for ques 6,7,8


# In[12]:


#5) spam[:2] = 0,1


# In[9]:


#6) bacon.index('cat') is 1  #since here index(1) & index(3) but bacon.index('cat') will take 1st index


# In[ ]:


#7) bacon.append(99) 
#[3.14, 'cat', 11, 'cat', True, 99]


# In[15]:


#8) bacon.remove('cat')
#[3.14, 11, 'cat', True, 99]


# In[19]:


#9) list concatenation(+)
# to combine two or more lists
list1 = [1,2,3]
list2 = [4,5,6]
result = list1+list2
# It allows you to create a new list by repeating the elements of an existing list a certain number of times.
original_list = [0, 1]
replicated_list = original_list * 3


# In[ ]:


#10) insert() is used to insert an element at a specific index within a list.
#remove() is used to remove the first occurrence of a specified element from a list


# In[3]:


#11) two methoda for removing items is 
#remove():to remove first occurance of a specified value
my_list = [1,2,3,4,5,6]
my_list.remove(2)
print(my_list)
#pop():to remove a item from a specified index
my_list = [1,2,3,4,5]
my_list.pop(2)
print(my_list)


# In[4]:


#12) list value and string value
# both have same sequence(ordered,unique index) 
#we can determinde the no. of items by using len() function in both


# In[6]:


#13) diff b/w tuple and list
#tuples                                                 list
#immutuable                                              mutuable
#for defining use ()                                       for defining use []
#built-in function as -- count(),index()               built in function as -- remove() ,insert()


# In[5]:


#14) tuple value of integer
my_tuple = (42,)
print(my_tuple)


# In[9]:


#15) list value's tuple and tuple's value list
#converting list value into tuple
my_list = [1,2,3,4,5,6]
my_tuple = tuple(my_list)
print(my_tuple)

#converting tuple value into list
my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
print(my_list)


# In[10]:


#16) variables that contain list values do not store list directly.Instead they store memory addresses to the list object in memory
#for ex lists,class or any mutuable objects


# In[12]:


#17) diff b/w copy.copy() and copy.deepcopy()
#copy.copy() is a shallow copy ,so we can make chaanges in this
import copy

original_list = [1, [2, 3]]
shallow_copy = copy.copy(original_list)

shallow_copy[1].append(4)
print(original_list)  
print(shallow_copy)  
#copy.deepcopy()
import copy

original_list = [1, [2, 3]]
deep_copy = copy.deepcopy(original_list)

deep_copy[1].append(4)
print(original_list)  
print(deep_copy)    



# In[ ]:




