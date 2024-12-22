class Bird:
    def fly(self):
        pass


class eagle(Bird):
    def fly(self):
        print("eagle is flying")


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguin can't fly")



def make_bird_fly(bird):
    bird.fly()

shalaby = eagle()
make_bird_fly(shalaby)  

penguin = Penguin()

