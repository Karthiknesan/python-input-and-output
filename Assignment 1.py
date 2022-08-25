#!/usr/bin/env python
# coding: utf-8

# ### Number of digits in a number

# In[1]:


n = int(input('enter any number:'))
i = 1
count = 0
for i in range(n):
    rem = n%10
    n = n//10
    count = count + 1 
    if n==0:
        break
print("no.of digits in a number =", count)


# ### Amstrong number - Sum of digits raised to the power of no.of digits equal to number

# In[3]:


n = int(input('enter any number:'))
org = n
t = n
i = 1
count = 0
sum = 0
for i in range(t):
    rem = t%10
    t = t//10
    count = count + 1 
    if t==0:
        break
for i in range(n):
    rem = n%10
    cube = rem**count
    n = n//10
    sum = sum + cube 
    if n==0:
        break
if org==sum:
    print(org, "is amstrong number")
else:
    print(org, "is not amstrong number")


# ### Strong number - sum of factorial of digits equal to number

# In[4]:


n = int(input('enter any number:'))
org = n
i = 1
sum = 0
for i in range(n):
    rem = n%10
    j=1
    fac=1
    for j in range(1,rem+1):
        fac = fac*j
    sum = sum + fac
    n = n//10
    if n==0:
        break
if org==sum:
    print(org, "is strong number")
else:
    print(org, "is not strong number")


# ### Perfect number - sum of factors equal to number

# In[5]:


n = int(input('enter any number:'))
org = n
i = 1
sum = 0
for i in range(1,n):
    if n%i==0:
        sum = sum + i
if org==sum:
    print(org, "is perfect number")
else:
    print(org, "is not perfect number")


# ### Fibonacci series

# In[6]:


t1 = 0
t2 = 1
n = int(input('enter no.of terms want:'))
nxt_trm = t1 + t2
print(t1, end = ',')
print(t2, end = ',')
for i in range(3,n+1):
    print(nxt_trm, end = ',')
    t1 = t2
    t2 = nxt_trm
    nxt_trm = t1 + t2


# ### print factors

# In[8]:


n = int(input('enter any number:'))
i = 1
count = 0
for i in range(1,n+1):
    if n%i==0:
        print(i)

        i = i+1
        count = count+1
print("total no.of factors =", count)


# In[ ]:




