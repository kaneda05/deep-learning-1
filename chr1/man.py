class Man:
    """
    Sample Class
    """

    def __init__(self, name):
        self.name = name
        print("Initilized")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("kaneda")
m.hello()
m.goodbye()