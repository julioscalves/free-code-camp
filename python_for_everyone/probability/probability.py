import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.balls = kwargs
        self.contents = []
        
        for color, number in self.balls.items():
            for index in range(number):
                self.contents.append(color) 

    def draw(self, number):
        result = []

        for n in range(number):
            choice = random.choice(self.contents)
            result.append(choice)
            self.contents.remove(choice)

        return result

def compare(target, experiment):
    for target_key, target_value in target.items():

        if target_key not in experiment.keys():
            return False   

        for exp_key, exp_value in experiment.items():
            if target_key == exp_key:
                if exp_value < target_value:
                    return False

    return True

 
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    contents = hat.contents
    sucesses = 0

    for experiment in range(num_experiments):
        sorted_balls = {}
        sorter = copy.copy(contents)
        for drawn in range(num_balls_drawn):

            if len(sorter) > 0:                
                sorted_ball = random.choice(sorter)
                sorter.remove(sorted_ball)

            if sorted_ball not in sorted_balls.keys():
                sorted_balls[sorted_ball] = 1
            else:
                sorted_balls[sorted_ball] += 1

        if compare(expected_balls, sorted_balls):
            sucesses += 1
    
    probability = sucesses/num_experiments

    return probability
