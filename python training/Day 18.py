class Dude:
    def _int_(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print('%i and %i' % (self.x, self.y))

    def add (self, num):
        print (self.x + self.y + num)
foo = Dude('3','4')

