class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    class laptop:
        def __init__(self):
            self.name="hp"
            self.cpu="i5"
            self.memory="1TB"



c1=student("nishant",26)
c2=student("swarna",28)
lap1=c1.lap
lap2=c2.lap
print(c1.name,c1.rollno)

