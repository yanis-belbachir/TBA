"""
Module description: This module implements the possible actions for the text-based adventure.
"""
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables
# and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


class Actions:
    """Class representing the actions."""
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """

        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        direction =direction.upper()
        if direction not in  game.direction:
            print("/n caractère non reconnue")
            return False
        direction=direction[0]  #on passe en maj toutes lettre pour
                                #comparer et pouvoir écrire les direction de toute les manière
        game.player.move(direction)
        return True
        # Si la direction est valide, essayer de déplacer le joueur
        if not game.player.move(direction):
            print("\nImpossible de se déplacer dans cette direction depuis ici."
                "Bulma ne veut pas....\n")




    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        # Vérifier les conditions de victoire

        current_room = player.current_room

        # Cas de victoire : Toutes les boules de cristal au "village"
        required_items = {"boule_de_cristal_1", "boule_de_cristal_2", "boule_de_cristal_3",
        "boule_de_cristal_4", "boule_de_cristal_5", "boule_de_cristal_6", "boule_de_cristal_7"}
        if current_room.name == "Village Namekien" and required_items.issubset(player.inventory.keys()):
            msg = print(f"\nBravo {player.name} ! Vous avez ramené les 7 boules de cristal au village."
            +" Vous avez sauvé l'Univers !\n")
            print(msg)
            game.finished = True
            return True

        # Cas de défaite : Le joueur est arrivé au vaisseau de Freezer
        if current_room.name == "Vaisseau Spatial de Freezer":
            msg = print(f"\nDommage {player.name}... Vous êtes arrivé au vaisseau de Freezer."
            +" Vous avez perdu !\n")
            print(msg)
            game.finished = True
            return True

        msg = print(f"\nBravo {player.name} ! Vous avez ramené les 7 boules de cristal au village."
        +" Vous avez sauvé l'Univers !")
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """Fonction qui sert pour l'historique des positions."""
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        game.player.get_history()
        return True  # Retourner True si tout s'est bien passé.

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """Fonction qui sert à revenir sur ses pas."""
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.back()

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """Fonction qui sert à voir ce qu'il y a dans chaque pièce."""
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        current_room = game.player.current_room

        # Afficher la description longue de la pièce
        print(current_room.get_long_description())

        # Afficher les objets et personnages présents
        print(current_room.get_inventory())

        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """Fonction qui prend en argument un item et qui sert à le ramasser."""
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        name_item = list_of_words[1].lower()
        total_weight = 0

        for poids in player.inventory.values() :
            total_weight += poids.weight

        for item in player.current_room.inventory :
            if name_item == item.name :

                total_weight += item.weight
                if total_weight > player.max_weight:
                    print("\nLimite d'objet atteinte,"
                    " il faut deposer un objet avant d'en prendre un nouveau.\n")
                    return True

                player.inventory[item.name]=item
                player.current_room.inventory.remove(item)
                print(f"\nVous avez pris l'objet : '{item.name}'.\n")
                return True
        if name_item in player.inventory:
            print(f"\nLa '{name_item}' est deja en votre possession.\n")
        else :
            print(f"\nLa '{name_item}' n'est pas dans cet endroit.\n")
        return True

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """Fonction qui prend en argument un item et qui sert à le déposer."""
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        name_item = list_of_words[1].lower()

        if name_item in player.inventory :
            item = player.inventory.pop(name_item)
            player.current_room.inventory.add(item)
            print(f"\nVous avez déposé l'objet : '{item.name}'.\n")
        else :
            print(f"\nVous ne possedez pas cet objet : '{name_item}'.\n")
        return True

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """Fonction qui sert à voir les items en notre possession."""
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print(f"\n{game.player.get_inventory()}")
        return True  # Ajoutez un return ici pour que la fonction retourne une valeur dans tous les cas.

    @staticmethod
    def talk(game, args, _):
        """Fonction qui prend en argument le nom d'un pnj et qui permet de dialoguer avec lui."""
        if len(args) < 2:
            print("Parlez à qui ?")
            return

        name = args[1]
        current_room = game.player.current_room

        if name in current_room.characters:
            character = current_room.characters[name]
            print(character.get_msg())
        else:
            print(f"{name} n'est pas ici.")
