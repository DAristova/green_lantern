class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction
        if self.x > self.asteroid.x or self.y > self.asteroid.y:
           raise MissAsteroidError()

    def turn_left(self):
        turns_left = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
        self.direction = turns_left[self.direction]

    def turn_right(self):
        turns_right = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}
        self.direction = turns_right[self.direction]

    def move_forward(self, distance):
        if self.direction == 'N' or self.direction == 'S':
            if self.x + distance <= self.asteroid.x:
                self.x + distance
            else:
                raise RobotFallError
        if self.direction == 'W' or self.direction == 'E':
            if self.y + distance <= self.asteroid.y:
                self.y + distance
            else:
                raise RobotFallError

    def move_backward(self, distance):
        if self.direction == 'N' or self.direction == 'S':
            if self.x - distance >= 0:
                self.x - distance
            else:
                raise RobotFallError
        if self.direction == 'W' or self.direction == 'E':
            if self.y - distance >= 0:
                self.y - distance
            else:
                raise RobotFallError


class MissAsteroidError(Exception):
    pass


class RobotFallError(Exception):
    pass

