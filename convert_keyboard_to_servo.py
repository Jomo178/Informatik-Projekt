from gpiozero import Servo                          # For Servo
from pynput.keyboard import Key, Listener           # For Catching Keyboard Input
from time import sleep                              # Delay

servo = Servo(25)                                  # I/O Portnum on Raspberry Pi

gotKeyPress = False
servoAngle = 0

def getInput(key):
    global gotKeyPress, servoAngle       # Set gotKeypress to False at the start
    
    if key.char == ('a'):
        servoAngle = 0.5
        gotKeyPress = True                          # Set gotKeypress to True if you get input 'a' or 'd'
        print("a")
        
    if key.char == ('d'):
        servoAngle = -0.5
        gotKeyPress = True                          # Set gotKeypress to True if you get input 'a' or 'd'
        print("d ")
        
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
    while True:
        if gotKeyPress:
            servo.value = servoAngle                    # Set Servo to Value determined by Keypress
            sleep(0.1)
        else:
            servo.value = 0                             # Set Servo to Nil if there was no Keypress
            sleep(0.1)
        
        
except KeyboardInterrupt:                           # Handle Keyboard Interrupts     
    print("KeyboardInterrupt used. Program terminated.")

    