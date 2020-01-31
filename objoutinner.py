class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap1=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap1.show()

    class laptop:
        def __init__(self):
            self.name="hp"
            self.cpu="i5"
            self.memory="1TB"
        def show(self):
            print(self.name,self.cpu,self.memory)


c1=student("nishant",26)
c1.show()
# print(c1.name,c1.rollno)
# lap1=student.laptop()