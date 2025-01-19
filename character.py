"""
Module description: This module implements characters for the text-based adventure.
"""

import random
from config import DEBUG

class Character :
    """
    Classe représentant un PNJ dans le jeu.

    Attributs:
        name (str): Nom du PNJ.
        description (str): Sa description.
        current_room (str): Où il se trouve.
        message(str): ce que dit le personnage
    """

    #define the constructor
    def __init__(self,name,description_pnj,msgs):
        self.name = name
        self.description_pnj =  description_pnj
        self.msgs = msgs
        self.current_room = None

    def __str__(self):
        """
        Retourne une représentation textuelle du personnage.

        Returns:
            str: Nom, description, lieu où il se trouve, le message du PNJ.
        """

        return f"{self.name}, {self.description_pnj}, {self.msgs}"


    def get_msg(self):
        """Fonction qui permet d'afficher le msg des pnj."""
        #print(self.msgs, type(self.msgs)) # test
        if self.msgs: #not in ([] , [0]) :
            msg = self.msgs.pop(0)
            self.msgs.append(msg)
            return msg
        return f"{self.name} n'a rien à dire..."



    def move(self):
        """
    Le PNJ a une chance sur deux de se déplacer vers une pièce adjacente ou de rester sur place.
        """

        # Liste des pièces adjacentes
        adjacent_rooms = list(self.current_room.exits.values())
        adjacent_rooms = [room for room in adjacent_rooms if room is not None]

        # Si aucune pièce adjacente, rester sur place
        if not adjacent_rooms:
            if DEBUG:
                print(f"DEBUG: {self.name} ne peut pas se déplacer (aucune pièce adjacente).")
            return False

        # 50% de chance de rester sur place
        if random.choice([True, False]):
            # Choisir une pièce adjacente au hasard
            new_room = random.choice(adjacent_rooms)
            # Mettre à jour la pièce actuelle du PNJ
            self.current_room.pnj.pop(self.name, None)
            new_room.pnj[self.name] = self
            self.current_room = new_room

            if DEBUG:
                print(f"DEBUG: {self.name} s'est déplacé vers la salle {new_room}.")
            return True

        if DEBUG:
            print(f"DEBUG: {self.name} reste dans la salle {self.current_room}.")
        return False
