import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        left, fleft, front, fright, right = lidar

        if left > right + 0.7:
            direction = 'left'
        elif right > left + 0.6:
            direction = 'right'
        else:
            direction = 'straight'

        if front < 0.7:
            motion = 'brake'
        elif velocity < 0.3 and front > 1.0:
            motion = 'accelerate'
        else:
            motion = 'coast'

        return (direction, motion)