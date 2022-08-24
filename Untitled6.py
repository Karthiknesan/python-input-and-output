#!/usr/bin/env python
# coding: utf-8

# ### string ###

# In[1]:


var1= "Hello world!"
print(type(var1))


# In[2]:


var1= "Hello world!"
print(var1.upper())


# In[3]:


var1= "HELLO WORLD!"
print(var1.lower())


# In[4]:


var1= "HELLO WORLD!"
print(len(var1))


# In[5]:


msg="python is high level programming language"


# In[6]:


msg[0:5:2]


# In[7]:


msg[-15:-3]


# In[8]:


msg.upper()


# In[9]:


len(msg)


# In[10]:


msg.count("m")


# In[11]:


msg


# In[12]:


msg.find("high")


# In[13]:


msg1='python is HIGH level programming language'


# In[14]:


msg1.replace("HIGH","high ")


# In[15]:


greet = "welcome "
name = "karthik "
last = "Arumugam"


# In[16]:


msg = greet + name


# In[17]:


print(msg)


# In[18]:


msg ="{}{}{}".format(greet,name,last)


# In[19]:


msg


# In[20]:


msg=f"{greet} {name}"


# In[21]:


msg


# In[22]:


msg=f"{greet} {name.upper()} {last.lower()}"


# In[23]:


msg


# In[24]:


dir(msg)


# In[25]:


a="hello, world"


# In[26]:


print(a.split(","))


# In[27]:


print(a.capitalize())


# In[28]:


help(int)


# In[29]:


a= "__Hello world!__"
print(a.rstrip("_"))


# In[30]:


a= "__Hello world!__"
print(a.lstrip("_"))


# In[31]:


age = 22
txt = "i am karthik and i am ("
print(txt.format(age))


# In[32]:


num=int(input("Enter the number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number"


# In[ ]:


a='python is HIGH level programming language'
b=a[-4:]
print(b)


# In[ ]:


a='python is high level programming language'
a[len(a)-1]


# In[ ]:


a='python is high level programming language'
print('is' in a)
print('hello' in a)


# In[ ]:


a='python is high level programming language'
k=a.partition("level")


# In[ ]:


k


# In[ ]:


type(k)


# In[ ]:


a1='python is high level programming language and easy and simple to use'
k=a1.rpartition("and")


# In[ ]:


k


# In[ ]:


a1='  hello  python world   '
a1.strip()


# In[ ]:


a1='  hello  python world   '
a1.rstrip()


# In[ ]:


a="*********hello**********world******"
a.strip("*")


# In[ ]:


a="*********hello**********world*****"
a.rstrip("*")


# In[ ]:


a="*********hello**********world*****"
a.lstrip("*")


# In[ ]:


str1="hi how are you?"


# In[ ]:


str1.startswith("hi")


# In[ ]:


str1.endswith("?")


# In[ ]:


s=str1.split()
s


# In[ ]:


type(s)


# In[50]:


s="welcome everyone"
s=s.center(20,"*")


# In[51]:


print(s)


# In[53]:


s="welcome everyone"
s=s.center(100,"*")
print(s)
len(s)


# In[54]:


s="welcome everyone"
s=s.rjust(50,"*")
print(s)
len(s)


# In[55]:


s="welcome everyone"
s=s.ljust(50,"*")
print(s)
len(s)


# In[58]:


s="welcome everyone"


# In[59]:


k=s.index("m")
print(k)


# In[60]:


m="1234567890A"
print(m.isalpha())
print(m.isalnum())
print(m.isdecimal())
print(m.isnumeric())


# In[61]:


m="abc"
print(m.isalpha())
print(m.isalnum())
print(m.isdecimal())
print(m.isnumeric())


# In[62]:


t="one two three one two three one two three"


# In[63]:


print(len(t))


# In[64]:


l=t.rfind("r")


# In[65]:


l


# In[ ]:


print(len())

