# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

class Player():
    matrix = {}
    history = []

    gamma = 0.9

    def build_matrix(self):
        options = ['R', 'P', 'S']
        for key in options:
            for subkey in options:
                self.matrix[key + subkey] = {}

        for key in self.matrix.keys():
            for subkey in self.matrix.keys():
                self.matrix[key].update({subkey: 100/9})

    def update_matrix(self):
        for key in self.matrix.keys():
            for subkey, subvalue in self.matrix[key].items():
                self.matrix[key][subkey] *= self.gamma
        
        self.matrix[self.history[-2]][self.history[-1]] += 1

    def display_matrix(self):
        for key in self.matrix.keys():
            for subkey, subvalue in self.matrix[key].items():
                print(f'{key} >>> {subkey}: {subvalue}')

    @staticmethod
    def play_random():
        return random.choice(['R', 'P', 'S'])

    def play(self):        
        counters = {'P': 'S', 'R': 'P', 'S': 'R'}

        if len(self.history) > 2:
            try:
                self.update_matrix()
                last_match = self.matrix[self.history[-1]]
                guess = counters[max(last_match, key=last_match.get)[-1]]
            except:
                guess = self.play_random()
        else:
            guess = self.play_random()

        return guess

def player(prev_play, opponent_history=[], player_history=[]):
    opponent_history.append(prev_play)
    persona = Player()

    if len(persona.matrix) == 0:
        persona.build_matrix()

    if len(player_history) > 2:
        last_match = player_history[-1] + opponent_history[-1]
        persona.history.append(last_match)
        guess = persona.play() 
    else:
        guess = persona.play_random()

    player_history.append(guess)

    return guess
