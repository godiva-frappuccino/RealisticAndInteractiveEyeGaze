from abc import ABCMeta, abstractmethod

class Behavior(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def getEyeAngle(self):
        pass

    @abstractmethod
    def update(self):
        pass
