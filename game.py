# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        namek_village = Room("Village Namekien", "dans un village paisible, entouré de maisons en forme de dômes. Les habitants méditent en silence sous les arbres Ajisa." )
        self.rooms.append(namek_village)
        guru_house = Room("Maison de Guru", "au sommet d'une colline rocheuse, dans la demeure sacrée du Grand Guru. L'air y est chargé d'une énergie mystérieuse.")
        self.rooms.append(guru_house)
        floating_islands = Room("Îles Flottantes", "au-dessus de l'océan turquoise, sur des îles flottantes maintenues par une force étrange. La lumière des deux soleils illumine tout.")
        self.rooms.append(floating_islands)
        ancient_cave = Room("Grotte Ancienne", "dans une ancienne caverne ornée de cristaux verts luminescents. Les murs murmurent l'histoire des anciens Namekiens.")
        self.rooms.append(ancient_cave)
        sacred_lake = Room("Lac Sacré", "au bord d'un lac immobile, dont la surface brille comme un miroir d'émeraude. Une aura de calme divin émane de cet endroit.")
        self.rooms.append(sacred_lake)
        Earth = Room("Terre", "Vous êtes sur la planète Terre, entouré de vastes prairies et de montagnes majestueuses. Le vent souffle doucement, apportant l'odeur des fleurs et de l'herbe fraîche. C'est un endroit paisible, mais une énergie étrange semble vibrer dans l'air, comme un appel à l'aventure.")
        self.rooms.append(Earth)
        goku_spaceship = Room("Vaisseau Spatial de Goku", "À bord d'un vaisseau sphérique argenté, conçu par le génie de Capsule Corporation.")
        self.rooms.append(goku_spaceship)
        freeza_spaceship = Room("Vaisseau Spatial de Freezer", "Un vaisseau en disque sombre, éclairé de violet. Au centre, un trône flottant domine, entouré de couloirs métalliques et de hangars menaçants.")
        self.rooms.append(frieza_spaceship)

        # Create exits for rooms

        namek_village = {"N" : None, "E" : sacred_lake, "S" : ancient_cave, "O" : None}
        guru_house = {"N" : None, "E" : floating_islands, "S" : sacred_lake, "O" : None}
        floating_islands = {"N" : None, "E" : None, "S" : freeza_spaceship, "O" : guru_house}
        ancient_cave = {"N" : namek_village, "E" : freeza_spaceship, "S" : None, "O" : None}
        sacred_lake = {"N" : guru_house, "E" : freeza_spaceship, "S" : ancient_cave, "O" : namek_village}
        Earth = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : goku_spaceship, "D" : None}
        goku_spaceship = {"N" : None, "E" : None, "S" : None, "O" : None,"U" : None, "D" : namek_village}
        frieza_spaceship = {"N" : None, "E" : None, "S" : None, "O" : ancient_cave}
        

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

                # If there is no command
        if command_word == "":
            return

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
