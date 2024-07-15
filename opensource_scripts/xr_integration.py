python
import openvr
import numpy as np

def initialize_vr():
    openvr.init(openvr.VRApplication_Scene)

def get_vr_events():
    event = openvr.VREvent_t()
    while openvr.VRSystem().pollNextEvent(event):
        print(f"VR event: {event.eventType}")

def main():
    initialize_vr()
    while True:
        get_vr_events()

if __name__ == "__main__":
    main()
