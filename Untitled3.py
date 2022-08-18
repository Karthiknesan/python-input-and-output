#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=6
y=4
print("bitwise AND",x&y)
print("bitwise OR",x|y)


# In[2]:


x=2
print("bitwisw NOT",~x)


# In[3]:


x=8
y=2
print("bitwise XOR",x^y)


# In[4]:


x=6
print("bitwise right shift",x>>1)
print("bitwise left shift",x<<1)


# In[1]:


l=int(input())
b=int(input())
area = l*b
print("area of rectangle",area)


# In[2]:


l=int(input())
area=l*l
print("area of square",area)


# In[3]:


b=int(input())
h=int(input())
area=1/2*h*b
print("area of triangle",area)


# In[4]:


r=int(input())
area=3.14*r**2
print("area of triangle",area)


# In[15]:


basic=int(input())
da=float(basic*0.05)
hra=float(basic*0.07)
pf=float(basic*0.03)
netpay=float(basic+da+hra)
grosspay=float(netpay-pf)             
print("your net salary is",grosspay)


# In[16]:


import sys
k=34
print(id(k))
print(type(k))
print(sys.getsizeof(k))


# In[17]:


print(k,"is integer?",isinstance(k,int))


# In[18]:


import sys
k=34.2
print(id(k))
print(type(k))
print(sys.getsizeof(k))
print(k,"is integer?",isinstance(k,float))


# In[ ]:


import sys
k=34+2
print(id(k))
print(type(k))
print(sys.getsizeof(k))
print(k,"is integer?",isinstance(k,float))


# In[1]:


import sys
k=34+2j
print(id(k))
print(type(k))
print(sys.getsizeof(k))
print(k,"is complex?",isinstance(k,complex))


# In[2]:


a=True
b=False
print(type(a))


# In[3]:


isinstance(b,bool)


# In[5]:


a<b


# In[6]:


print("TEA"<"COFFE")


# In[9]:


import this


# In[48]:


def month_name(x):
    if (x==1):
        print ("Jan")
    if (x==2):
         print("Feb")
    if (x==3):
         print("March")
    if (x==4):
         print("April")
    if (x==5):
         print("May")
    if (x==6):
         print("June")
    if (x==7):
         print("July")
    if (x==8):
         print("August")
    if(x==9):
         print("September")
    if(x==10):
        print("October")
    if(x==11):
         print("November")
    if(x==12):
         print("December")
    else:
         print("Invalid input")
month = int(input("Enter the month number: "))
month_name(month)


# In[50]:


i=1
while i<=10:
    print("python")
    i=i+1


# In[3]:


i=5
while i<=100:
    i=i+5
    print(i)
    


# In[5]:


i=1
add=0
while i<=5:
    add=add+i
    print(i)
    i=i+1


# In[ ]:





# In[ ]:




