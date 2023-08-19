# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mouse
import time
import keyboard
# Press the green button in the gutter to run the script.
IsRecording = False
IsPlaying = False
def startRecording():
    global IsRecording
    if IsRecording:
        IsRecording = False
        print("Record is finished")
    else:
        IsRecording = True
        print("Record is started")
def startPlaying():
    global IsPlaying
    if IsPlaying:
        IsPlaying = False
        print("Play is finished")
    else:
        IsPlaying = True
        print("Play is started")
keyboard.add_hotkey("Ctrl + Shift", startRecording)
keyboard.add_hotkey("Ctrl + Space", startPlaying)
if __name__ == '__main__':
    events = {}
    while True:
        if IsRecording:
            events = mouse.record()
            startRecording()
        if IsPlaying:
            events = mouse.play(events[:-1])
            startPlaying()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
