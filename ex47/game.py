# Making a simple game for ex47
class Room(object):

    def __init__(self, name, description): # constructor
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        """
        Function for getting directions in the game
        """
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        """
        Function for updating paths
        """
        self.paths.update.(paths)
