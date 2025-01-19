"""
Module description: This module implements the main game logic for the text-based adventure.
"""
# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from config import DEBUG


class Game:

    """Class representing the main game logic."""
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions = set()
        self.items = []
        self.actions = Actions

    # Setup the game
    def setup(self):

        """Function representing the commands."""
        # Setup commands
        self.direction= set(["N","NORD","OUEST","O","S","SUD","E","EST",'U',"UP",'D',"DOWN"])
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)"
        , Actions.go, 1)
        self.commands["go"] = go
        back = Command("back",":permet de retourner dans la salle précédente",Actions.back,0)
        self.commands["back"]= back
        history = Command("history","obtenir l'historique du parcours effectué",Actions.history,0)
        self.commands["history"]= history
        look = Command("look","savoir ce qu'il y a dans l'inventaire",Actions.look,0)
        self.commands["look"]= look
        take = Command("take","prendre un item dans la salle",Actions.take,1)
        self.commands["take"]= take
        drop = Command("drop","déposer un item dans la salle",Actions.drop,1)
        self.commands["drop"]= drop
        check = Command("drop","permet de vérifier ce que contient son inventaire",Actions.check,0)
        self.commands["check"]= check
        talk = Command("talk", " <nom> : parler avec un personnage non joueur", Actions.talk, 1)
        self.commands["talk"] = talk




         # Setup rooms

        namek_village = Room("Village Namekien",
        " dans un village paisible, entouré de maisons en forme de dômes."
        " Les habitants méditent en silence sous les arbres Ajisa.")
        self.rooms.append(namek_village)
        guru_house = Room("Maison de Guru",
        " au sommet d'une colline rocheuse, dans la demeure sacrée du Grand Guru."
        " L'air y est chargé d'une énergie mystérieuse.")
        self.rooms.append(guru_house)
        floating_islands = Room("Îles Flottantes",
        " au-dessus de l'océan turquoise, sur des îles flottantes maintenues par une force étrange."
        " La lumière des deux soleils illumine tout.")
        self.rooms.append(floating_islands)
        ancient_cave = Room("Grotte Ancienne",
        " dans une ancienne caverne ornée de cristaux verts luminescents."
        " Les murs murmurent l'histoire des anciens Namekiens.")
        self.rooms.append(ancient_cave)
        sacred_lake = Room("Lac Sacré",
        " au bord d'un lac immobile, dont la surface brille comme un miroir d'émeraude."
        " Une aura de calme divin émane de cet endroit.")
        self.rooms.append(sacred_lake)
        Earth = Room("Terre",
        "sur la planète Terre, entouré de vastes prairies et de montagnes majestueuses.")
        self.rooms.append(Earth)
        goku_spaceship = Room("Vaisseau Spatial de Goku",
        "à bord d'un vaisseau sphérique argenté, conçu par le génie de Capsule Corporation.")
        self.rooms.append(goku_spaceship)
        freeza_spaceship = Room("Vaisseau Spatial de Freezer",
        "dans le vaisseau de Freezer, un gigantesque disque effreyant, éclairé de violet.")
        self.rooms.append(freeza_spaceship)
        space = Room("Espace", "dans l'espace.")
        self.rooms.append(space)




        # Create exits for rooms

        namek_village.exits = {"N" : None, "E" : sacred_lake,
        "S" : ancient_cave, "O" : None,"U" : None, "D" : None}
        guru_house.exits = {"N" : None, "E" : floating_islands,
        "S" : sacred_lake, "O" : None,"U" : None, "D" : None}
        floating_islands.exits = {"N" : None, "E" : None,
        "S" : freeza_spaceship, "O" : guru_house,"U" : None, "D" : None}
        ancient_cave.exits = {"N" : namek_village, "E" : freeza_spaceship,
        "S" : None, "O" : None,"U" : None, "D" : None}
        sacred_lake.exits = {"N" : guru_house, "E" : freeza_spaceship,
        "S" : ancient_cave, "O" : namek_village,"U" : None, "D" : None}
        Earth.exits = {"N" : None, "E" : None, "S" : None,
        "O" : None, "U" : goku_spaceship, "D" : None}
        goku_spaceship.exits = {"N" : None, "E" : space,
        "S" : None, "O" : None,"U" : None, "D" : Earth}
        freeza_spaceship.exits = {"N" : None, "E" : None,
        "S" : None, "O" : ancient_cave,"U" : None, "D" : None}
        space.exits = {"N" : None, "E" : None, "S" : None,
        "O" : None,"U" : None, "D" : namek_village}


        # Setup item
        boule_de_cristal_4 = Item("boule_de_cristal_4",
        "une boule de crstal marquée du chiffre 4" ,5)
        self.items.append(boule_de_cristal_4)
        namek_village.inventory.add(boule_de_cristal_4)

        boule_de_cristal_2 = Item("boule_de_cristal_2",
        "une boule de crstal marquée du chiffre 2" ,5)
        self.items.append(boule_de_cristal_2)
        guru_house.inventory.add(boule_de_cristal_2)

        boule_de_cristal_3 = Item("boule_de_cristal_3",
        "une boule de crstal marquée du chiffre 3" ,5)
        self.items.append(boule_de_cristal_3)
        floating_islands.inventory.add(boule_de_cristal_3)

        boule_de_cristal_1 = Item("boule_de_cristal_1",
        "une boule de crstal marquée du chiffre 1" ,5)
        self.items.append(boule_de_cristal_1)
        sacred_lake.inventory.add(boule_de_cristal_1)

        boule_de_cristal_5 = Item("boule_de_cristal_5",
        "une boule de crstal marquée du chiffre 5" ,5)
        self.items.append(boule_de_cristal_5)
        ancient_cave.inventory.add(boule_de_cristal_5)

        boule_de_cristal_6 = Item("boule_de_cristal_6",
        "une boule de crstal marquée du chiffre 6" ,5)
        self.items.append(boule_de_cristal_6)
        #goku_spaceship.inventory.add(boule_de_cristal_6)

        boule_de_cristal_7 = Item("boule_de_cristal_7",
        "une boule de crstal marquée du chiffre 7" ,5)
        self.items.append(boule_de_cristal_7)
        #Earth.inventory.add(boule_de_cristal_7)
        guru_house.inventory.add(boule_de_cristal_7)
        ancient_cave.inventory.add(boule_de_cristal_6)

        # Setup character

        Guru = Character("Guru", "Chef des Namekiens."
        "C'est lui le plus ancien et le plus sage, ainsi que le créateur des boules de cristal.",
        ["Bonjour jeune saiyan. Tu es venu pour les boules de cristal je présume?",
        "Prends garde, Freezer est aussi à leur recherche. Tiens, en voici 2. Bonne chance."])
        guru_house.characters[Guru.name] = Guru

        Freezer = Character("Freezer",
        "Horrible tyran très puissant, à la recherche des boules de cristal pour devenir immortel.",
        ["Hahaha je t'ai trouvé misérable saiyan."
        " Combien de boules de cristal as-tu en ta possession?",
        "Hoho parfait, grâce à toi je vais devenir immortel!!"])
        freeza_spaceship.characters[Freezer.name] = Freezer

        Bulma = Character("Bulma",
        "Fille du créateur de la Capsule Corporation et ami d'enfance de Goku."
        "C'est aussi une bonne mécanicienne",
        ["Ah te voila enfin, c'est pas trop tôt!!",
        "Je t'avais dis de faire attention au vaisseau"
        " mais tu ne m'as pas écouté comme d'habitude!",
        "Les habitants de ce village m'ont donné la boule de cristal numéro 4 en arrivant."
        " Tiens prends le dragon radar et va chercher les 6 autres, puis ramène les ici."
        " Pendant ce temps je vais réparer le vaisseau pour qu'on puisse quitter cette planète."])
        namek_village.characters[Bulma.name] = Bulma

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Earth


    # Play the game
    def play(self):
        """Permet de jouer au jeu."""
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))


    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """Process the command entered by the player."""
        #if not command_string:   #if the word isn't in the command string we do nothing
           # return
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(">")
            #print(f"\nCommande '{command_word}' non reconnue.
            #Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)



    # Print the welcome message
    def print_welcome(self):
        """Affiche un msg de bienvenue au début du jeu."""
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())


def main():
    """
    Create a game object and play the game
    """
    Game().play()


if __name__ == "__main__":
    main()
