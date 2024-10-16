from pynput.keyboard import Key, Listener           # For Catching Keyboard Input
import serial                        # import Serial for Communication
import time                          # Delay

gotKeyPress = False


def getInput(key):
    global gotKeyPress, servoAngle       # Set gotKeypress to False at the start
    
    if key.char == ('a'):
        servoAngle = 0
        gotKeyPress = True                          # Set gotKeypress to True if you get input 'a' or 'd'

        
    if key.char == ('d'):
        servoAngle = 90
        gotKeyPress = True                          # Set gotKeypress to True if you get input 'a' or 'd'

        
    if key.char == ('w'):
        print("w")
        
    if key.char == ('s'):
        print("s")
         
    # by pressing 'enter' button 
    # you can terminate the loop                    # Press Enter for Termination
    if key == Key.enter: 
        print("Program stopped")
        return False
 
# Collect all event until released
with Listener(on_press = getInput) as listener:
    listener.join()
    
try:
    # create Serial Communication with Arduino
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        if gotKeyPress:
            ser.write(str(servoAngle).encode('utf-8'))  # Send ServoAngle
            sleep(0.1)
        else:
            ser.write(str(45).encode('utf-8'))  # Send ServoAngle 45
            sleep(0.1)
        
        
except KeyboardInterrupt:                           # Handle Keyboard Interrupts     
    print("KeyboardInterrupt used. Program terminated.")

    