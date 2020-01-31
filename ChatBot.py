import random
import time

# Introduction
print('Hello, Iam ZX85. I am a chatbot')
time.sleep(1)

print('I like to talk about Coffee and Food')
time.sleep(2)

# Take input of name variable
name = input('What is your name?\n')
time.sleep(5)

print('Hello', name, 'Nice to meet you')
time.sleep(5)

# year conversation
year = input(' I am not very good at dates. What year is it?\n')
time.sleep(5)

print('Ah yes', year, 'I think thats correct. Thank you!')
time.sleep(5)

# age conversation
myage = input('Can you guess my age? - enter a number: -\n ')
time.sleep(5)

print('Yes, you are right I am', myage, )
time.sleep(3)

# Math to calculate chatbot age in 100 years
myage = int(myage)
years = 100 - myage
print('I will be 100 in ', years, 'years')
time.sleep(6)

print('That will be the year', int(year) + years, '\n')
time.sleep(6)

# food Conversation
print('I love Chocolate Cake and I also like trying out new food ')
time.sleep(2)

food = input('How about you? What is youre favroite food?\n')
time.sleep(6)

print('I like', food, "too\n")
time.sleep(6)

# Coffee Conversation
print('I love Coffee!')
time.sleep(2)

coffee = input('Whats youre favorite Coffee order?\n')
time.sleep(5)

print('Mine too!\n')
time.sleep(4)



# Favroite Color using the random choice function
favcolor = input('What is youre favorite color?\n')
color = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Pink']
time.sleep(3)

print("My favorite color is   " + random.choice(color), '\n')
time.sleep(3)


#Goodbye
print('Goodbye  ' + name, ',It was nice to talk to you')
