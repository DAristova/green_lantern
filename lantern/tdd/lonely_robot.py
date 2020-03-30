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
        self.forward_movement = self.get_forward_movement()
        self.backward_movement = self.get_backward_movement()
        if self.x > self.asteroid.x or self.y > self.asteroid.y:
           raise MissAsteroidError()

    def turn_left(self):
        turns = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {'W': 'N', 'N': 'E', 'E': 'S', 'S': 'W'}
        self.direction = turns[self.direction]

    def get_backward_movement(self):
        return {
            'N': self.move_backward_y,
            'S': self.move_forward_y,
            'W': self.move_forward_x,
            'E': self.move_backward_x
        }

    def get_forward_movement(self):
        return {
            'N': self.move_forward_y,
            'S': self.move_backward_y,
            'W': self.move_backward_x,
            'E': self.move_forward_x
        }

    def move_forward_y(self, distance):
        if self.y + distance <= self.asteroid.y:
            self.y += distance
        else:
            raise RobotFallError

    def move_backward_y(self, distance):
        if self.y - distance >= 0:
            self.y -= distance
        else:
            raise RobotFallError

    def move_forward_x(self, distance):
        if self.x + distance <= self.asteroid.x:
            self.x += distance
        else:
            raise RobotFallError

    def move_backward_x(self, distance):
        if self.x - distance >= 0:
            self.x -= distance
        else:
            raise RobotFallError

    def move_forward(self, distance):
        move_func = self.forward_movement.get(self.direction, lambda: None)
        move_func(distance)

    def move_backward(self, distance):
        move_func = self.backward_movement.get(self.direction, lambda: None)
        move_func(distance)


class MissAsteroidError(Exception):
    pass


class RobotFallError(Exception):
    pass