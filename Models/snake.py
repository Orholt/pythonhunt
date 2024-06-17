# This file contains the Snake class
from random import randint

from Models.snake_type import SnakeType


class Snake:
    def __init__(self, snakeType: SnakeType):
        self.__type = snakeType
        self.__speed = 0
        self.__health = 0
        self.alive = True
        self.direction = randint(1, 2)
        self.points = 0

        switcher = {
            SnakeType.Regular: self.__init_regular(),
            SnakeType.Fast: self.__init_fast(),
            SnakeType.Tank: self.__init_tank()
        }

        switcher.get(snakeType)

    def __init_regular(self):
        self.__speed = 1
        self.__health = 1
        self.points = 10

    def __init_fast(self):
        self.__speed = 2
        self.__health = 1
        self.points = 50

    def __init_tank(self):
        self.__speed = 1
        self.__health = 2
        self.points = 100
