class computer:
    def __init__(self):
        self.name="nishant"
        self.age=28
    def update(self):
        self.age=30
    def compare(self,c2):
        if self.age==c2.age:return True
        else : return False

c1=computer()
c2=computer()
c1.name="swarna"
c1.age=26

if c1.compare(c2):
    print("they are same")
else:
    print("they are not same ")
print(c1.name,c1.age)
print(c2.name,c2.age)