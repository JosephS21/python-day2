#Given a list as a parameter,write a function that returns a list of numbers that are less than ten


#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

l_1 = [1,11,14,5,8,9]
# Use the following list - [1,11,14,5,8,9]
l_1 = [1,11,14,5,8,9]
l_2 = []
for n in l_1:
    if n >=10:
        continue
    if n not in l_2:
        l_2.append(n)

print(l_2)


#Write a function that takes in two lists and returns the two lists merged together and sorted
#Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def newlist(l_1,l_2):
    return sorted(l_1 + l_2)

print(l_1 + l_2)
print(newlist(l_1, l_2))
