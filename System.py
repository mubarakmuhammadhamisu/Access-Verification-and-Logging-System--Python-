import os
print("\n\n\n")
class system:
    def __init__ (self,user):
        self.user = user
# a function to return user name
    @property
    def name(self):
        return self.user.name
# verify if eligible to go       
    def check(self):
        vip=self.user.vipChecker()
        cl=self.user.clChecker()
        hc=self.user.hcChecker()
        if vip == 2 and cl == 1 and (hc ==1 or hc == 0):
            return 3
        elif vip == 1 and cl == 1 and hc ==1:
            return 2
        elif vip == 0 and cl == 0:
            return 0
        else:
            return 1
#a function to save the logs
def message(typ,name,message):
    if os.path.exists("log.txt"):
        with open("log.txt","a") as file:
            file.write(f"{typ}  {name}  {message}\n")
    else:
            with open("log.txt","w") as file:
                file.write(f"{typ}  {name}  {message}\n")

        

         
#u=User("mubarak",ck.vipU,ck.cle,"yes")
#sy1=system(u)
#print(sy1.check())
