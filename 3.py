print()
insert=input("ewlcome to ICICI Bank = ")
language=int(input("enter a language = "))
if language==1:
    print("Hindi")
elif language==2:
    print("english")
elif language==3:
    print("kannada")
pin=int(input("enter a ATM pin = "))
if pin>0:
    print("continue")
t_of_Tranjaction=int(input("enter a type of tranjection = "))
if t_of_Tranjaction==1:
    print("withdrawal amount")
elif t_of_Tranjaction==2:
    print("Balance inquiry")
elif t_of_Tranjaction==3:
    print("change pin") 
s_account=int(input("entr type of account = ")) 
if s_account==1:
    print("Saving account")
elif s_account==2:
    print("current account")
amount=int(input("enter a your amount = "))
if amount>0:
    print("collect your amount") 
receipt=input("enter a yes or no = ")
if receipt=="yes" or receipt=="no":
    print("take your print") 
else:
    print("invalid")                            