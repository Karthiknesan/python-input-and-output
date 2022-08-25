#!/usr/bin/env python
# coding: utf-8

# ### program to check the alphabet is vowals or consonant

# In[4]:


n = input("Input a letter of the alphabet: ")

if n in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % n)
elif n == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." %n) 


# ### program to check voter is  eligble or not

# In[7]:


n = int(input("Enter a number "))
if n >=18:
    print("your eligble to  vote",n)
else:
    print("you are not eligble ",n)


# ### program to check numbers are positive,negative and zero

# In[9]:


n = int(input("Enter a number"))
if n >=1:
    print("given no. is positive",n)
elif n < 0:
    print("given no. is negative ",n)
elif n == 0:
    print("given no. is zero")


# ### program to Check a triangle is equilateral, isosceles or scalene

# In[10]:


print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")


# ### program to check selling a product is profit or loss

# In[15]:


product_price = int(input("Enter a product price "))
selling_price = int(input("enter a selling price "))
profit =selling_price-product_price 
if profit > 0:
    print("your are profit is ",profit)
else:
    print("your are in loss ",profit)


# #### print program enter two number and print greatest number

# In[16]:


a = int(input("Enter a number "))
b = int(input("Enter a number "))
if a>b:
    print(a," is greatest number")
else :
    print(b," is greatest number")


# #### print program enter two number and print smallest number

# In[18]:


a = int(input("Enter a number "))
b = int(input("Enter a number "))
if a>b:
    print(b," is smallest number")
else :
    print(a," is smallest number")


# #### print program enter three number and print smallest number

# In[20]:


a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))
if a>b:
    print(b," is smallest number")
elif b>c: 
    print(c," is smallest number")
elif c>a:
    print(a," is smallest number")


# #### print program enter three number and print greates tnumber

# In[21]:


a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))
if a>b:
    print(a," is greates number")
elif b>c: 
    print(b," is greates number")
elif c>a:
    print(c," is greatest number")


# ### program to calculate the root of quadratic equation

# In[12]:


print("Equation: ax^2 + bx + c ")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=b**2-4*a*c
d1=d**0.5
if(d<0):
    print("The roots are imaginary. ")
else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("The first root: ",round(r1,2))
    print("The second root: ",round(r2,2)) 


# ### program to enter the number(1-7) and print days of the week

# In[14]:


n = int(input("Enter a number 1 to 7: "))
if n == 1:
    print("monday")
elif n == 2:
    print("tuesday")
elif n == 3:
    print("wednesday")
elif n == 4:
    print("thursday")
elif n == 5:
    print("friday")
elif n == 6:
    print("saturday")
elif n == 7:
    print("sunday")
    


# ### program to enter the number(1-12) and print days of the month

# In[29]:


x = int(input("Enter the month number: "))
if (x==1):
    print ("January")
if (x==2):
    print("Febuary")
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
if (x==9):
    print("September")
if (x==10):
    print("October")
if (x==11):
    print("November")
if (x==12):
    print("December")


# ### program to entera number(1-4)and perform operators

# In[14]:


n = int(input("\n1.addition\n2.subraction\n3.multipilcatin\n4.division\n Enter a number 1 to 4 "))
a = int(input("Enter a number "))
b = int(input("Enter a number "))
if n==1:
    print("Your Addition is ",a+b)
if n==2:
    print("Your Subraction is",a-b)
if n==3:
    print("Your multiplication is",a*b)
if n==4:
    print("Your divison is ",a/b)


# ### program to print hello python 10 times

# In[2]:


i = 0;
while i < 10:
    print("hello python")
    i += 1


# ### program to print number from 1 to 10

# In[3]:


for i in range(1,11):
    print(i)


# ### program to print table of a number

# In[5]:


number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
print ("The Multiplication Table of: ", number)    
for i in range(1, 11):      
   print (number, 'x', i, '=', number * i)


# ### program to find even number from 1 to 100 

# In[7]:


for i in range(1,101):
    if i%2 ==0:
        print("given no. is even",i)
    else:
        print("given no. is not even number",i)


# ### program to find odd number from 1 to 100 

# In[9]:


for i in range(1,101):
    if i%2 !=0:
        print("given no. is odd number",i)
    else:
        print("given no. is not odd number",i)


# ### program to print grade

# In[6]:


print("Enter Marks Obtained in 5 Subjects: ")
maths = int(input())
english = int(input())
science = int(input())
computer = int(input())
evs = int(input())

total = maths +english+science+computer+evs
avg = total/5

if avg>=91 and avg<=100:
    print("Your Grade is A+")
elif avg>=81 and avg<91:
    print("Your Grade is A-")
elif avg>=71 and avg<81:
    print("Your Grade is B+")
elif avg>=61 and avg<71:
    print("Your Grade is B-")
elif avg>=51 and avg<61:
    print("Your Grade is C+")
elif avg>=41 and avg<51:
    print("Your Grade is C-")
elif avg>=35 and avg<41:
    print("Your Grade is D+")
elif avg>=0 and avg<35:
    print("Your Grade is f")


# ### program to  give bonus more than 5 years

# In[1]:


print ("enter salary")
salary = int(input())
print ("enter year of service")
years = int(input())
if years>4:
    s=0.05 * salary
    print ("bonus is",s)
else:
    print ("no bonus")


# ### program to check rectangle or square 

# In[4]:


a = int(input("enter a length"))
b = int(input("enter a breadth"))
if a==b:
    print("given measurment  is square")
else:
    print("given measurment  is rectangle")


# ### program to find 3 input age to  youngest and oldest among them

# In[8]:


age1=int(input('enter age1: '))
age2=int(input('enter age2: '))
age3=int(input('enter age3: '))
if age1>age2 and age1>age3:
    print("age1 is oldest1 ",age1)
elif age2>age1 and age2>age3:
    print("age2 is oldest ",age2)
else:
    print("age3 is oldest ",age3)
if age1<age2 and age1<age3:
    print("age1 is youngest ",age1)
elif age2<age1 and age2<age3:
    print("age2 is youngest ",age2)
else:
     print("age3 is youngest ",age3)

