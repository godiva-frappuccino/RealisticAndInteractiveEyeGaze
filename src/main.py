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
    detector = Detector()
    behaviorManager = BehaviorManager()

    DEVICE_ID = 0
    cap = cv2.VideoCapture(DEVICE_ID)
    # write init camera
    while True:
        # read camera
        ret, frame = cap.read()
        #perception
        rects = detector.detectFace(frame)
        if len(rects) > 0:
            frame = detector.drawRects(frame, rects)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # update state
        behaviorManager.update()
        # read behavior
        eyeAngle = behaviorManager.getEyeAngle()
        # send to Server
        client.send("Eye", eyeAngle)



if __name__ == "__main__":
    main()
