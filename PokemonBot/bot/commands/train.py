class Train:
    def __init__(self):
        self.experience = 0
        self.level = 1

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        print("Congratulations! Your Pokemon leveled up to level", self.level)

    def view_level(self):
        return self.level

    def view_experience(self):
        return self.experience

train = Train()