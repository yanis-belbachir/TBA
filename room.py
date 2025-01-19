"""
Module description: This module implements the rooms for the text-based adventure.
"""

# Define the Room class.

class Room:
    """Class representing the rooms."""

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.characters = {}

    # Define the get_exit method.
    def get_exit(self, direction):
        """Return the room in the given direction if it exists."""

        if direction in self.exits:
            return self.exits[direction]

        return None

    def get_exit_string(self):
        """Return a string describing the room's exits."""

        exit_string = "Sorties: "
        for exit in self.exits:
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_inventory(self):
        """Fonction qui permet d'associer des objets et des pnj à un lieu."""

        # Liste pour les descriptions des contenus de la pièce
        contents = []

        # Ajouter les objets présents
        if self.inventory:
            for item in self.inventory:
                contents.append(f"- {item.name} : {item.description} ({item.weight} kg)")

        # Ajouter les PNJs présents
        if self.characters:
            for name, character in self.characters.items():
                contents.append(f"- {name} : {character.description_pnj}")

        # Si rien n'est trouvé, indiquez que la pièce est vide
        if not contents:
            return "Il n'y a rien ici."

        # Retournez les contenus combinés
        return "On voit:\n    " + "\n    ".join(contents)

    # Return a long description of this room including exits.
    def get_long_description(self):
        """Fonction qui permet de dire et de décrire le lieu où le joueur se situe."""
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
