import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError, RobotFallError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        direction = 'E'
        asteroid = Asteroid(x + 1, y + 1)
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, 'W')


class TestRobotBehavior:

    def setup(self):
        self.x, self.y = 5, 5
        self.asteroid = Asteroid(self.x + 10, self.y + 10)

    @pytest.mark.parametrize(
        "curent_direction,expected_direction",
        (
                ('E', 'N'),
                ('N', 'W'),
                ('W', 'S'),
                ('S', 'E')
        )
    )
    def test_turn_left(self, curent_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, curent_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "curent_direction, expected_direction",
        (
                ('E', 'S'),
                ('S', 'W'),
                ('W', 'N'),
                ('N', 'E')
        )
    )
    def test_turn_right(self, curent_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, curent_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "direction, distance, expected_position",
        (
                ('N', 5, 10),
                ('S', 9, 14),
                ('W', 1, 6),
                ('E', 3, 8)
        )
    )
    def test_move_forward(self, direction, distance, expected_position):
        robot = Robot(self.x, self.y, self.asteroid, direction)
        if direction == 'N' or direction == 'S':
            current_position = robot.x
            robot.move_forward(distance)
        if direction == 'W' or direction == 'E':
            current_position = robot.y
            robot.move_forward(distance)
        assert current_position + distance == expected_position

    @pytest.mark.parametrize(
        "direction, distance, expected_position",
        (
                ('N', 1, 4),
                ('S', 3, 2),
                ('W', 4, 1),
                ('E', 2, 3)
        )
    )
    def test_move_backward(self, direction, distance, expected_position):
        robot = Robot(self.x, self.y, self.asteroid, direction)
        if direction == 'N' or direction == 'S':
            current_position = robot.x
            robot.move_backward(distance)
        if direction == 'W' or direction == 'E':
            current_position = robot.y
            robot.move_backward(distance)
        assert current_position - distance == expected_position

    @pytest.mark.parametrize(
        "direction, distance, expected_position",
        (
                ('N', 15, 20),
                ('S', 25, 30),
                ('W', 11, 16),
                ('E', 14, 19)
        )
    )
    def test_robot_fall_forward(self, direction, distance, expected_position):
        with pytest.raises(RobotFallError):
            robot = Robot(self.x, self.y, self.asteroid, direction)
            robot.move_forward(distance)

    @pytest.mark.parametrize(
        "direction, distance, expected_position",
        (
                ('N', 6, -1),
                ('S', 20, -15),
                ('W', 7, -2),
                ('E', 11, -6)
        )
    )
    def test_robot_fall_backward(self, direction, distance, expected_position):
        with pytest.raises(RobotFallError):
            robot = Robot(self.x, self.y, self.asteroid, direction)
            robot.move_backward(distance)
