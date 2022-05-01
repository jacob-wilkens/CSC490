from RotationType import RotationType

class Item:
    
    def __init__(self, name, width, height, length):
        self.name = name
        self.width = width
        self.height = height
        self.length = length
        self.rotation_type = 0
        self.position = [0, 0, 0]

    def string(self):
        """To String of all current attributes"""
        return "%s(%sx%sx%s) pos(%s) rt(%s) vol(%s)" % (
            self.name, self.width, self.height, self.length,
            self.position, self.rotation_type, self.get_volume()
        )

    def get_volume(self):
        """Current Volume"""
        return self.width * self.height * self.length

    def get_dimension(self):
        """Current Dimension"""
        if self.rotation_type == RotationType.RT_WHL:
            dimension = [self.width, self.height, self.length]
        elif self.rotation_type == RotationType.RT_HWL:
            dimension = [self.height, self.width, self.length]
        elif self.rotation_type == RotationType.RT_HLW:
            dimension = [self.height, self.length, self.width]
        elif self.rotation_type == RotationType.RT_LHW:
            dimension = [self.length, self.height, self.width]
        elif self.rotation_type == RotationType.RT_LWH:
            dimension = [self.length, self.width, self.height]
        elif self.rotation_type == RotationType.RT_WLH:
            dimension = [self.width, self.length, self.height]
        else:
            dimension = []

        return dimension