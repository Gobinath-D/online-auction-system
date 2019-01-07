import random
import time
print("\t\t\t**ONLINE AUCTION SYSTEM**\t\t\t")
i=int(input("enter the value 1 or 2 1:new user 2:exsisting user\n"))
file = open('gobi.txt','w') 
def create():
    name=str(input("Enter your name\n"))
    file.write(name)
    file.write("\n")
    contact()
    auction()
def contact():
        conno=str(input("enter your contact number\n"))
        mobno=len(conno)
        if int((mobno)==10):
            print("OTP IS SEND YOUR MOBILE NUMBER")
            contents = "1234567890"
            pw_length =1
            out= ""
            for i in range(pw_length):
                next_index = random.randrange(len(contents))
                out = out +contents[next_index]
                print(out)
                print("ENTER YOUR OTP")
                a=str(input(""))
                if a == out:
                    file.write(conno)
                    file.write("\n")
                    add=str(input("Enetr your address\n"))
                    file.write(add)
                    file.write("\n")
                    file.close()
                else:
                    print("password is wrong if you want re-enter press 1")
                    i=int(input(""))
                    if i==1:
                        contact()
                    else:
                        create()
                    
        else:
            contact()

def exsistinguser():
    name=str(input("Enter your name\n"))
    contacts()
def contacts():
    conno=str(input("enter your contact number\n"))
    mobno=len(conno)
    if int((mobno)==10):
        print("OTP IS SEND YOUR MOBILE NUMBER")
        contents = "1234567890"
        pw_length =1
        out= ""
        for i in range(pw_length):
            next_index = random.randrange(len(contents))
            out = out +contents[next_index]
            print(out)
            print("ENTER YOUR OTP")
            a=str(input(""))
            if a == out:
                auction()
            else:
                print("password is wrong if you want re-enter press 1")
                i=int(input(""))
                if i==1:
                    contacts()
            
    else:
        contacts()
def amount():
    print("online payment only")
    print("Enter your creadit card number")
    cn=str(input(""))
    cvv=str(input("enter cvv number\n"))
    lencn=len(cn)
    lencvv=len(cvv)
    if lencn==13 and lencvv==3:
        print("your payement success\n")
        print("**********************\n")
        print("The house detail are\n")
        print("**********************\n")
        print("Enter house number 1 or 2")
        count=int(input(""))
        if count==1:
            file = open('house.txt','r')
            house=file.read()
            print(house)
        else:
            file = open('house1.txt','r')
            house1=file.read()
            print(house1)
            
    else:
        amount()
def amountcar():
    print("online payment only")
    print("Enter your creadit card number")
    cn=str(input(""))
    cvv=str(input("enter cvv number\n"))
    lencn=len(cn)
    lencvv=len(cvv)
    if lencn==13 and lencvv==3:
        print("your payement success\n")
        print("**********************\n")
        print("The car details are")
        print("**********************\n")
        print("Enter car number 1 or 2")
        count=int(input(""))
        if count==1:
            file = open('car.txt','r')
            car=file.read()
            print(car)
        else:
            file = open('car1.txt','r')
            car1=file.read()
            print(car1)
            
    else:
        amount()
    
def auction():
    print("\t\t\t**WELCOME TO AUCTION**\t\t\t")
    print("Auction produt's are 1:House 2:car ")
    print("*********************Week Shedule For Auction*****************")
    print(" _________________________________________________________________")
    print("|        |                 |       Time           |               |")
    print("| Date   |   Car Name      |----------------------|   Starting    |")
    print("|        |                 |starting   |   ending |     Rate      |")
    print("|-----------------------------------------------------------------|")
    print("| 14-dec |     Shift       | 10:00:00  | 10:30:00 |    3lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 15-dec |     i10         | 10:30:00  | 11:00:00 |    2lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 16-dec |     city        | 11:00:00  | 11:30:00 |    5lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 17-dec |     polo        | 11:30:00  | 12:00:00 |    3lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 18-dec |     WagonR      | 12:00:00  | 12:30:00 |    2.5lakhs   |")
    print("|-----------------------------------------------------------------|")
    print("| 19-dec |     Brezza      | 12:30:00  | 1:00:00  |    3lakhs     |")
    print("|-----------------------------------------------------------------|")
    print("| 20-dec |     Scorpio     | 12:30:00  | 1:00:00  |    5lakhs     |")
    print("|_________________________________________________________________|")
    print(" _______________________________________________________________")
    print("|        |                 |       Time           |             |")
    print("|  Date  |   House area    |----------------------|   Starting  |")
    print("|        |                 |starting   |   ending |     Rate    |")
    print("|---------------------------------------------------------------|")
    print("| 14-dec |   Gandhipuram   |  1:00:00  |  1:30:00 |   23lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 15-dec |   Kuniyamuthur  |  1:30:00  |  2:00:00 |   12lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 16-dec |     Ukkadam     |  2:00:00  |  2:30:00 |   25lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 17-dec |     Hopes       |  2:30:00  |  3:00:00 |   23lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 18-dec |    Singanallur  |  3:00:00  |  3:30:00 |   2lakhs    |")
    print("|---------------------------------------------------------------|")
    print("| 19-dec |  Saravanampatti |  3:30:00  |  4:00:00 |   13lakhs   |")
    print("|---------------------------------------------------------------|")
    print("| 20-dec |  Ramanathapuram |  3:30:00  |  4:00:00 |   13lakhs   |")
    print("|_______________________________________________________________|")

    print("House comes auction an 10:00:00 between 10:30:00")
    print("Car comes action an 12:00:00 between 12:30:00")
    i=time.strftime("%I:%M:%S")
    print(i)
    i='10:00:20'
    #i='01:25:20'
    print(i)
    if i<'01:30:00'and i>'01:00:00':
        print("House an action")
        print("starting amount is=23000000 if you buy this home press 1")
        hr=int(input(""))
        if hr==1:
            g=int(input("Enter the amount is "))
            for i in range(g,5000000,225000):
                print(i)
            print("the winner is gobi final amount=",i)
            amount()
        else:
            auction()
    elif i<'10:30:00'and i>'10:00:00':
        print("car an action")
        print("amount is=10000000 if you buy this car press 1")
        hr=int(input(""))
        if hr==1:
            g=int(input("Enter the amount is "))
            for i in range(g,5000000,225700):
                print(i)
            print("the winner is gobi final amount=",i)
            amountcar()
        else:
            auction()
        
    else:
        print("better luck next time")
     
if i==1:
    print("new user\n")
    create()
elif i==2:
    print("Exsisting user\n")
    exsistinguser()
else:
    print("Enter valid number 1 to 2\n")


