# Develop a program that accept an input string, count occurrences of all characters within a string.

mystr = input("enter the string : ")
myset = set(mystr)
for ele in myset:
    countchar = 0
    for char in mystr:
        if char == ele:
            countchar += 1
    print("count of char {} is - {} ".format(ele, countchar))
