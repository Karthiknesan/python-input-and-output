#!/usr/bin/env python
# coding: utf-8

# In[3]:


a_list = []
print("Please enter 10 numbers: ")

for num in range(10):
    list_num =int(input("Enter a number:"))
    a_list.append(list_num)
print(sum(a_list))


# In[4]:


import math

def factorial(n):
    return(math.factorial(n))

num=int(input())
print("factorial of",num,"is",factorial(num))


# In[9]:


print("even numbers from 1 to 100:")
for num in range(1,100):
    if num%2==0:
        print("It is a even number",num)


# In[14]:


print("odd numbers from 1 to 100:")
for num in range(1,100):
    if num%2!=0:
        print("It is a odd number",num)


# In[10]:


x=100
i=1
while i<=x:
    if i%2==0:
        print("It is a even number",i)
    i=i+1


# In[2]:


x= 100
i=1
while i<=x:
    if i%2!=0:
        print("It is odd number",i)
    i=i+1


# In[3]:


def is_leap(year):
    leap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return leap
        else:
            return True
    else:
        return leap

year = int(input())
print(is_leap(year))


# In[ ]:


if (year % 4) == 0:

