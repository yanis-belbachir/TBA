"""
Module description: This module implements the features for the player.
"""

# Define the Player class.
class Player():
    """Class representing the features for the player."""

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.history = []
        self.current_room = None
        self.inventory = {}
        self.max_weight = 10


    # Define the move method.
    def move(self, direction):
        """Fonction permettant au joueur d'aller dans une direction."""
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Set the current room to the next room.
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        self.get_history()
        return True

    # Retoure les lieux visités
    def get_history(self):
        """Fonction permettant au joueur de connaître les lieux qu'il a déjà visité."""
        try:
            if len(self.history) >= 1:
                print("\nVous avez déjà visité les pièces suivantes:")
                for room in self.history:  # Exclut la pièce actuelle de l'historique affiché
                    print(f"    - {room.description[0:-1]}")
            else:
                print("\nVous n'avez visité aucune autre pièce.")
        except ValueError as e:
            print(f"\nUne erreur s'est produite lors de l'affichage de l'historique : {e}")

    # Define the back method.
    def back(self):
        """Fonction permettant au joueur de revenir en arrière."""
        try:
            if len(self.history) >= 1:
                # Set the current room to the previous room
                self.current_room = self.history.pop()
                print(self.current_room.get_long_description())
                self.get_history()
                return True

            print("\nVous ne pouvez pas revenir en arrière !\n")
            return False
        except ValueError as e:
            print(f"\nUne erreur inattendue s'est produite lors du retour en arrière : {e}")
            return False

    def get_inventory(self):
        """Fonction permettant au joueur de connaître son inventaire."""
        if not self.inventory:
            return "\nVotre inventaire est vide."

        # Utilisation de str.join() pour construire le contenu de l'inventaire
        inventory_items = "\n".join(f"  - {item}" for item in self.inventory.values())
        return f"\nVous disposez des items suivants :\n{inventory_items}"
