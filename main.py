# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
length_list = len(names)
random_name = random.randint(0,length_list - 1)
print(names[random_name])




