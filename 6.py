#6). Develop a program that takes as input an hourly wage and the number of hours an employee worked in the last week. The program should compute and return the employee’s
#pay. Overtime work is calculated as: any hours beyond 40 but less than or equal 60 should be paid at 1.5 times the regular hourly wage. Any hours beyond 60 should be paid at 2 times the
#regular hourly wage.

def calwag(time , wages):
    if time > 60:
        return 2*time*wages
    elif  time > 40:
        return 1.5*time*wages
    else:
        return time*wages


tim = int(input("enter the time worked"))
wag = int(input("enter the wages her hr"))

result = calwag(tim , wag)

print(result)
