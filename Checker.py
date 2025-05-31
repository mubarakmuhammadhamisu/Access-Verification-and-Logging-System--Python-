
class User:
    # access code = ac
    # clearance = cl
    # humen check = hc
    def __init__(self,name,ac,cl,hc):
        self.name=name
        self.ac = ac
        self.cl =  cl
        self.hc = hc
#checkig if a person is a vip user            
    def vipChecker(self):
        vip="1a5"
        nonVip="123"
        if self.ac == vip:
            return 2
        elif self.ac == nonVip:
            return 1
        else:
            return 0
#checking valid clearance                
    def clChecker(self):
        validCl = 20
        if self.cl == validCl:
            return 1
        else:
            return 0
# checking if is a human                
    def hcChecker(self):
        if self.hc == "yes":
            return 1
        else:
            return 0
            
               
vipU = "1a5"
nonvip="123"
cle = 20
                            
#use1=User("mubarak",vipU,cle,"yes")  
#use2=User("muhammad",nomalU,2,"yes") 
    
    