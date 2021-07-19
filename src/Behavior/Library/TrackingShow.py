from .Behavior import Behavior

class Tracking(Behavior):
    def __init__(self):
        self.eyeAngle = 0.0

    def update(self):
        pass

    def getEyeAngle(self):
        return self.eyeAngle

    def trackHuman(self, frame=None, rect=None):
        if frame is None or rect is None:
            return self.eyeAngle

        frame_center_x = frame.shape[1]/2
        rect_center_x = (rect.left() + rect.bottom()) / 2
        self.eyeAngle = round((rect_center_x - frame_center_x) / frame.shape[1] * 4, 2)

        return self.eyeAngle
