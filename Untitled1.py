#!/usr/bin/env python
# coding: utf-8

# In[2]:


def hello():
    print("helloworld")

hello()
hello()
hello()


# In[1]:


1 +1


# In[3]:


a="KARTHIK"
b="ARUMUGAM"
print(a+b)
print(a+" "+b)
print(a,b)


# In[4]:


l=int(input("enter the number"))
b=int(input("enter the number"))
area = l*b
print(area)


# In[6]:


a=5
b=3
print(a<b)


# In[9]:


x = True
y = False
print(x and y)
print(x or y)
print(not x)


# In[9]:


name = str(input("ENTER A YOUR NAME "))


# In[10]:


a=int(input())
b=int(input())
if a==b:
    print("BOTH ARE EQUAL")
else:
    print("BOTH ARE NOT EQUAL")


# In[14]:


a=int(input("ENTER YOUR MARK "))
if a>=50:
    print(" you have passed the exam with ",a)
else:
    print("you have failed the exam with ",a)


# In[16]:


Vote=int(input("ENTER YOUR Age "))
if a>=18:
    print(" your eligible to vote ")
else:
    print("your not eligible to vote-  ")


# In[2]:


num1=int(input("ENTER YOUR NUMBER "))
num2=int(input("ENTER YOUR NUMBER "))
if num1>num2:
    print("this the greatest number")
else:
    print("this is smaller number")


# In[4]:


num1=int(input("ENTER YOUR NUMBER "))
if (num1%2==0):
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")


# In[9]:


name="KARTHIK ARUMUGAM"
print("A" in name)


# In[10]:


name="KARTHIK ARUMUGAM"
print("A" not in name)

