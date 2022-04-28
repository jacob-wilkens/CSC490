from Item import Item

class Bin:
    def __init__(self, name, width, height, length):
        self.name = name
        self.width = width
        self.height = height
        self.length = length
        self.items = []

    def string(self):
        """To String of all current attributes"""
        return "%s(%sx%sx%s) vol(%s)" % (
            self.name, self.width, self.height, self.length, self.get_volume()
        )

    def get_volume(self):
        """Current Volume"""
        return self.width * self.height * self.length, self.number_of_decimals

    def put_item(self, item):
        """Determines if item can be put in box"""
        pass

        # valid = False

        # if len(self.items) == 0:
            #valid = True
        
        # else:
            # Do some logic for checking different orientations along with checking for valid placement of other items

        
        # return valid