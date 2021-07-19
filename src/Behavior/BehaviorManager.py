# import all
from .Library.ReadShow import Read
from .Library.ZeroShow import Zero
from .Library.AliveShow import Alive
from .Library.EngageShow import Engage
from .Library.GlanceShow import Glance
from .Library.AcknowledgeShow import Acknowledge
#  param

class BehaviorManager:
    def __init__(self):
        # param
        self.theta = None
        self.attention = None
        # load states
        self.Zero = Zero()
        self.Alive = Alive()
        self.Read = Read()
        self.Engage = Engage()
        self.Glance = Glance()
        self.Acknowledge = Acknowledge()
        # init state
        self.state = self.Read
        pass

    def update(self):
        self.updateState()
        self.updateParam()

    def updateState(self):
        pass

    def updateParam(self):
        self.state.update()
        pass

    def getEyeAngle(self):
        return self.state.getEyeAngle()
