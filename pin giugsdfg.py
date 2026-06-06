class bird:
    def __init__(self):
        print("bird is ready")

    def whoistihis(self):
        print("bird")

    def swim(self):
        print("swin faster")

class penguin(bird):

    def __init__(self):

        super().__init__()
        print("penguin")


    def whoistihis(self):
        print("bird")

    def run(self):
        print("run faster")

peggy = penguin()
peggy.whoistihis()
peggy.swim()
peggy.run()