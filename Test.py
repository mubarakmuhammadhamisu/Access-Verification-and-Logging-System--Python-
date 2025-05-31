import os
import System as Sy
from System import system as sy
import Checker as ck
from Checker import User

def area(person):
    verification=person.check()
    grant = "  Access granted"
    denied ="  Access denied"
    alt = "  ALERT: Unauthorized access attempt!"
    if verification == 3:
        print(person.name, grant)
        Sy.message("vip",person.name,grant)
                
                
    elif verification == 2:
        print( person.name,grant)
        Sy.message("Ga",person.name,grant)
                
    elif verification == 1:
        print(person.name,denied)
        Sy.message("Da",person.name,denied)
    
    else: 
        print(person.name,alt)
        Sy.message("Ua",person.name,alt)

user1=User("mubarak",ck.vipU,ck.cle,"yes")
user2 =User("tim",ck.nonvip,ck.cle,"yes")
user3 =User("kally",1,0,"yes")
user4 =User("phive ",ck.nonvip,ck.cle,"no")
user5 =User("joy",ck.nonvip,0,"yes")

sc1=sy(user1)
sc2=sy(user2)
sc3=sy(user3)
sc4=sy(user4)
sc5=sy(user5)

area(sc1)
area(sc2)
area(sc3)
area(sc4)
area(sc5)