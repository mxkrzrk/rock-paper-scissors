import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        # initialization of the list for the move function
        # in the class CyclePlayer
        self.my_move = self.moves
        # random choise for first round
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        # moves of the players stored
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        # random move
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        # reflects the choice of the previous round
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        # choses a different move of the last round
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class HumanPlayer(Player):
    def move(self):
        # repeats the input statement until there is
        # a match with the list or exit
        while True:
            move_human = input("Rock, paper, scissors? > ")
            if move_human.lower() in self.moves:
                return move_human.lower()
            elif move_human.lower() == 'exit':
                exit()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # scores initialization
        self.score_p1 = 0
        self.score_p2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def rounds(self):
        # repeats the input statement until there is
        # a valid choose or exit
        while True:
            self.number_rounds = input(
                "How many rounds do you want want play? > ")
            if self.number_rounds.isdigit():
                return self.number_rounds
            elif self.number_rounds.lower() == 'exit':
                exit()

    def play_round(self):
        # move
        move1 = self.p1.move()
        move2 = self.p2.move()
        # resault of the match and storing player score
        if self.beats(move1, move2):
            self.score_p1 += 1
            winner = '**** PLAYER ONE WINS ****'
        elif move1 == move2:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            winner = '**** TIE ****'
        else:
            self.score_p2 += 1
            winner = '**** PLAYER TWO WINS ****'
        # output the match information
        print(
            f"> You played : {move1}"
            f"\n> Opponent played : {move2}"
            f"\n{winner}"
            f"\nScore: Player one ( {self.score_p1} ),"
            f"Player two ( {self.score_p2} )"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(
            ">>>> Game start! <<<<"
            "\n(If do you want exit game, please digits \'exit\'"
            " when the game will ask you the number of rounds or your move)"
        )
        self.rounds()
        for round in range(int(self.number_rounds)):
            print(f"\nRound {round + 1} --")
            self.play_round()
        if self.score_p1 == self.score_p2:
            print(
                f"\n---- The game ended in a tie! ----"
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )"
            )
        elif self.score_p1 > self.score_p2:
            print(
                f"\n---- Player ONE has won! ----"
                f"\nScore: Player one ( {self.score_p1} )*,"
                f"Player two ( {self.score_p2} )"
            )
        else:
            print(
                f"\n---- Player TWO has won! ----"
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )*"
            )


if __name__ == '__main__':
    # organize the game with a human player and
    # randomly choose an attitude from the other player
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
