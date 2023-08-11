#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) two values of data type:
#true(1)
#false(0)


# In[2]:


#2) three diff type of operators
#And: This operator returns true if both operands are true, otherwise it returns false
#OR: This operator returns false  if both of the operands is false,otherwise it returns true
#NOT:The NOT operator is used to reverse the value of a boolean expression


# In[3]:


#3)AND
#  operand1    operand2     result
  #   0           0          0
 #    1           0          1
   #  0           1          1
  #   1           1          1
#OR

 #   1          1          1
 #   0          0          0
#    1          0          0
 #   0          1          0
   
##NOT
#   1                   0
#   0                   1


# In[4]:


#4) (5 > 4) and (3 == 5) not (5>4) result: true
#not(5>4)    result:false
#(5 > 4) or (3 == 5)  result:true
#not ((5 > 4) or (3 == 5)) result:false


# In[5]:


#5)Equal to (==): Compares whether two values are equal.
#Not equal to (!=): Compares whether two values are not equal.
#Greater than (>): Checks if the value on the left is greater than the value on the right.
#Less than (<): Checks if the value on the left is less than the value on the right.
#Greater than or equal to (>=): Checks if the value on the left is greater than or equal to the value on the right.
#Less than or equal to (<=): Checks if the value on the left is less than or equal to the value on the right.


# In[ ]:


#6)diff b/w assignment and equal to
#        assignment                                   equal to
#to assign a value                                      #to compare the value
# it doesn't compare values                             #used in condtion  or expression that involve comparsion


# In[8]:


#7) Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')
print('spam')


# In[8]:


#8 code
spam=int(input("Enter a value for spam"))
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings")


# In[9]:


#9) If  programme is stuck in an endless loop,then we'll press Ctrl+c


# In[21]:


#10) break and continue 
#break:break is used to exist from it's current execution and terminate the current loop
#i.e
for i in range(5):
    if i == 4:
        break  # This will terminate the loop when i is 3
    print(i)
    
#continue:this will skip the current iteration of the loop and will move to the next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # This will skip the current iteration


# In[10]:


#11)range(10) : stopping value
#range(0,10):start value and stopping value
#range(0,10,1):start,stopping and step value


# In[12]:


#12).using  for loop
for i in range(1,11):
    print(i)
#using while loop
i=1
while i<=10:
    print(i)
    i+=1


# In[17]:


#13)
#import spam     #after importing the spam you can call the function bacon
#spam.bacon()


# In[ ]:




