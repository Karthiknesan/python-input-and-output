#!/usr/bin/env python
# coding: utf-8

# In[11]:


string= str(input("Enter the string:  "))
if (string==string[::-1]):
    print("This is palindrome")
else:
    print("This is not palindrome")


# In[32]:


num=int(input("Enter the number"))
factor=[]
for i in range(1,num+1):
    if num%i==0:
        factor.append(i)
print(" factors of :",num,factor)


# In[25]:


num=str(int(input("Enter the number")))
print(num[::-1])


# In[44]:


num=int(input("Enter the number"))
for i in range(num,0,-1):
    print(i)


# In[9]:


num=int(input("Enter the number"))
reverse = 0
while num>0:
    reminder = num%10
    reverse = (reverse *10)+ reminder
    num = num//10
    print("\n reversed entered number",reverse)
    


# In[11]:


num=int(input("Enter the number"))
reverse = 0
for i in range(num,0,-1):
    reminder = num%10
    reverse = (reverse *10)+ reminder
    num = num//10
    print("\n reversed entered number",i)


# In[6]:


num=int(input("Enter the number"))
i=1
reverse = 0
for i in range(num):
    reminder = num%10
    reverse = (reverse *10)+ reminder
    num = num//10
print(reverse)


# In[ ]:





# In[ ]:




