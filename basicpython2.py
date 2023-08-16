#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1) 
first_variable = 59
second_variable = 90
print(first_variable)
print(second_variable)
#addition
addition = first_variable + second_variable
print(addition)
#subtraction
sub = first_variable-second_variable
print(sub)
#multiplication
mult = first_variable*second_variable
print(mult)
#division
div = first_variable/second_variable
print(div)


# In[9]:


#2) diff b/w following operators
#(a) '/'&'//'
#'/'(division operator) : used to divide two numbers (int or float) 
#for ex 5/2 = 2.5 and 4/2=2
# '//'(Floor Division operator): it calculates the largest integer and if both operands are integers it'll give integer values
#for ex 5//2 = 2

#(b) '**' & '^' 
# '**'(Exponentiation operator): it will use a number to power 
#for ex ; 2**3 = 8
#'^'(Bitwise XOR operator): it will use a bitwise operator b/w two binary numbers
#for ex; 5^3 will be 6
# 5(101) 3(011) 110(6)


# In[10]:


#3) list of logical operators
#and : operator returns True if both operands are True.
#or :  The "or" operator returns True if at least one of the operands is True.
#not:  The "not" operator returns the opposite Boolean value of its operand.


# In[2]:


#4) right and left shift  operator
#right shift operator:it is a bitwise operator which shift the bits towards the right
#for ex;
a = 10>>2
# 1010  >> 0010 i.e 2
#left shift operator: it is a bitwise operator which shift the bits towards left
a=10<<2
1010   << 101000


# In[6]:


#5) 
int_list = [1,2,34,5,66,7,88,9,10,11,23,19,12,14,15]
len(int_list)
if 10 in int_list:
    print("10 is present in list")
else:
    print("10 is not present in list")


# In[ ]:




