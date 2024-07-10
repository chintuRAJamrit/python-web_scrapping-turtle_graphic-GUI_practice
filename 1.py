#Develop a program that accept the list and iterates over a list of numbers lst and prints the numbers in the list whose square is divisible by 8.

#list = [2,3,5,7,8,9,12,16]
lists = input("enter the numbers in list with spaces")
lists = [int(x) for x in lists.split()]
for num in lists:
    if (num*num)%8==0:
        print(num)
    
