""" RandoMouse

    A Module that will create a random mouse movements.
    All it needs to do is make my mouse move so that my 
    status in MSTeams is always available when i'm away.

"""

__author__ = 'Mark Prado'


from time import time, sleep
from win32api import SetCursorPos, GetSystemMetrics
from random import randrange

class RandoMouse:
    def __init__(self,timer=None):
        """
            Initializes an instance,
            takes timer as an arguement should be in Integer/Float.
            If timer is None, set default self.timer = 60
            Also takes the screen resolution.
        """

        self._max_w = GetSystemMetrics(0)
        self._max_h = GetSystemMetrics(1)
        
        if timer is None:
            self._timer = 60
        elif isinstance(timer, (int, float)) and timer > 0:
            self._timer = timer
        else:
            raise TypeError("input must be a positive number")

        self._running = False 
        self._speed = 0.01

    def set_timer(self,t):
        """
            _timer variable setter
        """
        self._timer = t

    def set_speed(self,s):
        """
            Sets mouse move speed
        """
        self._speed = s

    def _get_y_in_line(self,x,x1,y1,x2,y2):
        """
            Solving for the coordinates between two points with a given x value
            and retuns y
        """
        slope = (y2-y1)/(x2-x1)
        b = y1 - (slope*x1)
        y = (slope*x) + b
        return int(y)

    def _move(self,x,y):
        """
            Executes mouse move
        """
        SetCursorPos((x,y))

    def start(self):
        """
            Start the fun
        """
        self._running = True
        timeout = time() + self._timer

        prev_coor = [randrange(self._max_w),randrange(self._max_h)]
        next_coor = [randrange(self._max_w),randrange(self._max_h)]

        while self._running:
            x1 = prev_coor[0]
            y1 = prev_coor[1]

            x2 = next_coor[0]
            y2 = next_coor[1]


            x_list = [x for x in range(min([x1,x2]),max([x1,x2]),10)]
            if x1 > x2:
                x_list.sort(reverse=True)

            y_list = list()

            for x in x_list:
                y_list.append(self._get_y_in_line(x,x1,y1,x2,y2))


            for coor in zip(x_list,y_list):
                self._move(*coor)
                sleep(self._speed)

            prev_coor = list(next_coor)
            next_coor = [randrange(self._max_w),randrange(self._max_h)]

            if time() > timeout:
                self._running = False