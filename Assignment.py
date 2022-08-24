#!/usr/bin/env python
# coding: utf-8

# In[5]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# In[6]:


for x in range(2, 30, 3):
  print(x)


# ### Write a program to print the following number pattern using a loop ###

# In[11]:


rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")


# ### program to print the reverse number pattern using a loop ###

# In[12]:


rows = int(input("Enter the number of rows: "))  

for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print(j+1, end=' ')  
    print(" ")  


# ### program to check a given number is perfect or not in Python ###

# In[25]:


num = int(input("please give first number a: "))
sum=0
for i in range(1,(num//2)+1):
    remainder = num % i
    if remainder == 0:
        sum = sum + i
if sum == num:
    print("given no. is perfect number")
else:
    print("given no. is not a perfect number") 


# ### program to print the reverse star pattern using a loop ###

# In[13]:


rows = int(input("Enter the number of rows: "))  

for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  


# ### program to print the star pattern using a loop ###

# In[15]:


rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print("\n")


# ### program to check given number is prime or not ###

# In[17]:


i,temp=0,0
n = int(input("please give a number : "))
for i in range(2,n//2):
    if n%i == 0:
        temp=1
        break
if temp == 1:
    print("given number is not prime")
else:
    print("given number is prime") 


# ### program to find even number from 1 to 100 ###

# In[24]:


for i in range(1,101):
    if i%2 ==0:
        print("given no. is even",i)
    else:
        print("given no. is not even number",i)


# ## program to find odd number from 1 to 100 ###

# In[23]:


for i in range(1,101):
    if i%2 !=0:
        print("given no. is odd number",i)
    else:
        print("given no. is not odd number",i)

