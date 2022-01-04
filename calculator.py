#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("\nCalculator")


# In[4]:


def add(x,y):
    return x + y
def div(x,y):
    return x / y
def sub(x,y):
    return x - y
def mult(x,y):
    return x * y


# In[8]:


print("\nChoose the math operation\n")
print("\n 1 - Sum")
print("\n 2 - Subtraction")
print("\n 3 - Multiplication")
print("\n 4 - Division")

op = input("\n Input the number (1,2,3 or 4): ")

nb1 = int(input("\n First number: "))
nb2 = int(input("\n Second number: "))


# In[9]:


if op == '1':
    print('\n')
    print(nb1, '+', nb2, '=', add(nb1, nb2))
    print('\n')
    
elif op == '2':
    print('\n')
    print(nb1, '-', nb2, '=', sub(nb1, nb2))
    print('\n')

elif op == '3':
    print('\n')
    print(nb1, '*', nb2, '=', mult(nb1, nb2))
    print('\n')

elif op == '4':
    print('\n')
    print(nb1, '/', nb2, '=', div(nb1, nb2))
    print('\n')

else:
    print('\n Invalid value')


# In[ ]:




