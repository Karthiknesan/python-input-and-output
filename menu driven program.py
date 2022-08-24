#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("CALCULATE AREA")  
print("1. Circle")  
print("2. Rectangle")  
print("3. Square")   
a = int(input("Enter the number of shape:"))  
if a == 1:  
    r = int(input("Enter Radius of Circle:"))  
    area = 3.14*r*r
    print("area of circle",area)
    if a == 2:  
        h = int(input("Enter Height of Rectangle:"))  
        w = int(input("Enter Width of Rectangle:"))  
        rectangle(h, w)
        area = h*w
        print("area of rectangle",area)
        if a == 3:  
            l = int(input("Enter Side of Square:"))  
            square(l)
            area=l*l
            print("area of square",area)
else:  
    print("Incorrect Choice:")
  

        


# In[ ]:




