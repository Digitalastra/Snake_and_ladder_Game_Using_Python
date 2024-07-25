import random

class Die:
    def roll(self):
        return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self, steps):
        self.position += steps

    def __str__(self):
        return f"{self.name} is at position {self.position}"


class Board:
    def __init__(self, size=100, snakes=None, ladders=None):
        self.size = size
        self.snakes = snakes if snakes else {}
        self.ladders = ladders if ladders else {}

    def check_snake_or_ladder(self, position):
        if position in self.snakes:
            return self.snakes[position]
        elif position in self.ladders:
            return self.ladders[position]
        return position

    def is_winner(self, position):
        return position >= self.size

    def __str__(self):
        board_str = f"Board Size: {self.size}\nSnakes: {self.snakes}\nLadders: {self.ladders}"
        return board_str


class Game:
    def __init__(self):
        self.board = Board(
            size=100,
            snakes={16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78},
            ladders={1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        )
        self.players = []
        self.die = Die()

    def add_player(self, player_name):
        self.players.append(Player(player_name))

    def play(self):
        while True:
            for player in self.players:
                print(f"\n{player.name}'s turn")
                roll = self.die.roll()
                print(f"Rolled a {roll}")
                player.move(roll)
                player.position = self.board.check_snake_or_ladder(player.position)
                print(player)

                if self.board.is_winner(player.position):
                    print(f"{player.name} wins!")
                    return


# Create and start the game
game = Game()
number_of_players = int(input("Enter the number of players: "))
for i in range(number_of_players):
    player_name = input(f"Enter the name of player {i+1}: ")
    game.add_player(player_name)
game.play()
