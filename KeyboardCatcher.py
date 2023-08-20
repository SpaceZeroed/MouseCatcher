import keyboard
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
    while True:

        if IsRecording:
            events = keyboard.record()
            print(events)
            startRecording()
        if IsPlaying:
            events = keyboard.play(events[1:])
            startPlaying()
