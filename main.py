from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Icon, Side
from usys import stdin
from uselect import poll

hub = PrimeHub()

motor1 = Motor(Port.C)
motor2 = Motor(Port.B)
motor3 = Motor(Port.A)
eyes = UltrasonicSensor(Port.D)
forceL = ForceSensor(Port.E)
forceR = ForceSensor(Port.F)
keyboard = poll()
keyboard.register(stdin)


#Wheel positioning for distance tracker
motor1.run_target(9999,0)
motor2.run_target(9999,0)
print("Executing in 5 seconds. ")
wait(5000)

def mainExecution():
    '''Robot's primary code neccesary for execution'''
    while True:
        #Tracks distance traveled only in Automatic Mode
        motor1Inches = str(abs(((12 * motor1.angle() / 7312.8)))) 

        #Brakes and waits for user input on how to proceed
        if eyes.distance() < 200 or forceL.pressed(0.1) or forceR.pressed(0.1):
            motor1.brake()
            motor2.brake()
            # hub.speaker.beep(500,1000)
            hub.display.icon(Icon.SAD)
            wait(200)
            print("Obstacle found. Please reroute. ")
            while 1==1:
                if keyboard.poll(0):

                    key = stdin.read(1)
                    print("You pressed:", key)
                    
                    #Forward
                    if key == 'w':
                        hub.display.icon(Icon.ARROW_UP)
                        motor1.run(-400)
                        motor2.run(400)
                        print(motor1Inches + " total feet")
                    #Back
                    elif key =='s':
                        hub.display.icon(Icon.ARROW_DOWN)
                        motor1.run(397)
                        motor2.run(-400)
                    #Left
                    elif key == 'a':
                        hub.display.icon(Icon.ARROW_LEFT)
                        motor2.run(400)
                    #Right
                    elif key == 'd':
                        hub.display.icon(Icon.ARROW_RIGHT)
                        motor1.run(-397)
                    #Turn left and back
                    elif key == 'c':
                        motor1.run(400)
                        motor2.run(-400)
                        wait(500)
                        motor2.brake()
                        motor1.run_angle(-400, -420)
                    #Brake and wait for input
                    elif key == 'q':
                        hub.display.icon(Icon.PAUSE)
                        motor1.brake()
                        motor2.brake()
                        eyes.lights.on()
                    #Reenter Automatic mode
                    elif key == 'b':
                        break
                    #Manual fast mode
                    elif key == 'e':
                        hub.display.icon(Icon.HAPPY)
                        motor1.run(-790)
                        motor2.run(790)
                        print(motor1Inches + " total feet")
                    else:
                        print('Command is invalid. Please try again or analyze code.')
        #Automatic Mode
        elif eyes.distance() >= 200:
            hub.display.icon(Icon.HAPPY)
            motor1.run(-790)
            motor2.run(790)
            print(motor1Inches + " total feet")

mainExecution()
