#!/usr/bin/env python
# coding: utf-8

# In[18]:


name = input("Введите имя:")
age = int(input("Введите возвраст:"))
age = str(2118-age)
print(name + " исполнится 100 лет в "+ age)


# In[1]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x <= 5:
        print(x)


# In[ ]:


import random
num = random.randint(1,9)
guess = 0
tr = 0
while guess != num and guess != "exit":
    guess = input("Введите число между 1 и 9 ")
    if guess == "exit":
        break
    guess = int(guess)
    tr += 1
    if guess < num:
        print("Больше")
    elif guess > num:
        print("Меньше")
    else:
        print("Угадал с ", tr, " попытки!")
input()


# In[ ]:




