# Define the Player class.
class Player():
    """
    This class represents a player in a text-based adventure game. A player has a name and is located in a specific room.

    Attributes:
        name (str): The name of the player.
        current_room (Room): The room where the player is currently located.

    Methods:
        __init__(self, name): The constructor.
        move(self, direction): Moves the player to a different room based on the specified direction.
        """
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory={}
   
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        self.history.append(self.current_room)
        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
       
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        self.get_history()
        return True
       
    def get_history(self):
        if len(self.history) == 0:
            print("\n aucune salle n'a été visité\n")
            return
        print("\nvous avez déjà visité:\n")
        for i in range(len(self.history)):
            print("\t-"+self.history[i].description+"/n")
        return