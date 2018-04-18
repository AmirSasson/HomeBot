""" set interval like JS"""
import threading


def set_interval(func, sec):
    """ set interval like JS"""

    def func_wrapper():
        """ set interval like JS"""
        set_interval(func, sec)
        func()

    timer = threading.Timer(sec, func_wrapper)
    timer.start()
    return timer
