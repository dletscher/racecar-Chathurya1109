import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        left, fleft, front, fright, right = lidar

        if left > right + 0.16:
            direction = 'left'
        elif right > left + 0.16:
            direction = 'right'
        else:
            direction = 'straight'

        if front < 0.15:
            motion = 'brake'
        elif velocity < 0.15 and front > 1.0:
            motion = 'accelerate'
        else:
            motion = 'coast'

        action = (direction, motion)
        if action not in possibleActions:
            action = random.choice(possibleActions)

        return action