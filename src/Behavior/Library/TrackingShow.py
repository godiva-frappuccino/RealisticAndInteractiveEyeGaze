from .Behavior import Behavior

class Tracking(Behavior):
    def __init__(self, eye):
        self.eye = eye
        self.target_x = 0.0
        self.target_y = 0.0

    def update(self):
        target_x = self.target_x
        target_y = self.target_y
        now_x, now_y = self.eye.getEyeAngle()
        diff_x = target_x - now_x
        diff_y = target_y - now_y
        self.eye.update(x=(now_x + diff_x/3), y=(now_y + diff_y/3))

    def getEyeAngle(self):
        return self.eyeAngle

    def trackHuman(self, frame=None, rect=None):
        if frame is None or rect is None:
            self.update()
            return self.eye.getEyeAngle()

        frame_center_x = frame.shape[1]/2
        rect_center_x = (rect.left() + rect.right()) / 2
        self.target_x = round((rect_center_x - frame_center_x) / frame.shape[1] * 4, 2)

        frame_center_y = frame.shape[0]/2
        rect_center_y = (rect.top() + rect.bottom()) / 2
        self.target_y = round((rect_center_y - frame_center_y) / frame.shape[1] * 4, 2)

        self.update()
        return self.eye.getEyeAngle()
