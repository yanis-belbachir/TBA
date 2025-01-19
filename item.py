"""
Module description: This module implements the items for the text-based adventure.
"""

class Item:
    """Class representing the items (his name, his description, his weight)."""

    # Define the constructor.
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    # The string representation of the command.
    def __str__(self):
        return  f"{self.name} : {self.description} ({self.weight} kg)"
