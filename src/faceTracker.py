# import interface, perception?, BehaviorManager
import argparse
import time
import cv2
from Interface.Client import UDPClient
from Behavior.BehaviorManager import BehaviorManager
from Perception.Detector import Detector
from Perception.Memory import Memory

def main():
    client = UDPClient("127.0.0.1")
    behaviorManager = BehaviorManager()
    behaviorManager.selectState("tracking")
    detector = Detector()

    DEVICE_ID = 0
    cap = cv2.VideoCapture(DEVICE_ID)
    # write init camera
    while True:
        # read camera
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        #perception
        rects = detector.detectFace(frame)
        if len(rects) > 0:
            frame = detector.drawRects(frame, rects)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # track human
        rect = rects[0] if len(rects) > 0 else None # select human 0
        eyeAngle = behaviorManager.Tracking.trackHuman(frame=frame, rect=rect)
        # send to Server
        client.send("Eye", eyeAngle)

        time.sleep(0.1)



if __name__ == "__main__":
    main()
