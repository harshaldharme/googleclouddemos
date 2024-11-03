class Bird:
    def fly(self):
        return "Bird can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"

def show_flying_capability(bird):
    print(bird.fly())

penguin = Penguin()
show_flying_capability(penguin)   # Output: Penguin cannot fly

penguin = Bird()
show_flying_capability(penguin)   # Output: Bird can fly