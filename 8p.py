print("welcom to bike shop")
bikes = ["a","b","c","d"]

while True:
    print("option \n 1. see bikes\n 2. see cost \n 3. buy \n 4. exit")
    a = int (input("enter the choice : "))
    if a==1:
        for i in bikes :
            print(i)
    elif a==2:
        print( "1. hourly - 100 \n 2. daily - 500 \n 3. weekly - 2500 \n ( for familyu pack buy 3-5 bikes )")
    elif a==3:
        c= int(input("number of bikes you want"))
        d =int(input("hor how long u want"))
        if d==1:
            cost = 100*c
        elif d==2:
            cost = 500*c
        elif d==3:
            cost = 2500*c
        else:
            print(" enter the correct option")

        if c in range (3,6):
            print("do u want to avial family discount")
            dis = input("y for yes \n n for no\n")
            if dis =="y":
                cost = cost*0.7
            else:
                cost = cost
            
        print(" thank you purshing" , cost, "is your final bill")

       
        
    
    else:
        break    
        
        
