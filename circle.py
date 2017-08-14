class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


    def __str__(self):
        return 'x = {}, y = {}, r = {}' .format(self.x, self.y, self.r)

    def area(self):
        if self.x >= 0 and self.y >= 0 and self.r >= 0:
            area = 3.14 *(self.r * self.r)
            return area
        else:
            print 'No valid number'

    def lenght(self):
        if self.x >= 0 and self.y >= 0 and self.r >= 0:
            lenght = 2 * 3.14 * self.r
            return lenght
        else:
            print 'No valid number'
