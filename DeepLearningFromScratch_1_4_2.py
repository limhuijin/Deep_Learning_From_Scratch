class Man:
    def __init__(self, name):
        self.name = name
        print("init name")
        
    def hello(self):
        print("Hello " + self.name + "!")
        
    def goobye(self):
        print("Good-bye " + self.name + "!")
        
m = Man("David")
m.hello()
m.goobye()