class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config",self.cpu,self.ram)

com1=computer("i5",16)
com2=computer("ryzen",8)

com1.config()
com2.config()