import binascii #import libraries needed to run code
import board
import busio
import digitalio
import time
import pwmio

from dabble import Dabble

dabble = Dabble(board.GP0, board.GP1, debug=True) #defines hardware and attatches variable to pin

from adafruit_motor import motor # Imports a function from the adafruit_motor library


left_motor_foward = board.GP12 # initializes the variable left_motor_foward and attatches it to GP12
left_motor_backward = board.GP13 # initializes the variable left_motor_backward and attatches it to GP13
right_motor_foward = board.GP14
right_motor_backward = board.GP15

pwm_La = pwmio.PWMOut(left_motor_foward, frequency=10000) # Tells the controller that the motor is an output
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)
pwm_Lc = pwmio.PWMOut(right_motor_foward, frequency=10000)
pwm_Ld = pwmio.PWMOut(right_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) # Configuration line (it is required)
Left_Motor_speed = 0 #Initiates the variable for the left_motot_speed and starts it at 0
Right_Motor = motor.DCMotor(pwm_Lc, pwm_Ld)
Right_Motor_speed = 0

def forward():
    Left_Motor_speed = .5 # Makes left motor roll foward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = .5 # Makes left motor roll foward
    Right_Motor.throttle = Right_Motor_speed

def backwards():
    Left_Motor_speed = -.5 # Makes left motor roll foward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -.5 # Makes left motor roll foward
    Right_Motor.throttle = Right_Motor_speed

def left():
    Left_Motor_speed = -.5 # Makes left motor roll foward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = .5 # Makes left motor roll backwards
    Right_Motor.throttle = Right_Motor_speed

def right():
    Left_Motor_speed = .5 # Makes left motor roll foward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -.5 # Makes left motor roll backwards
    Right_Motor.throttle = Right_Motor_speed

def stop():
    Left_Motor_speed = 0 # Makes left motor roll foward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0 # Makes left motor roll backwards
    Right_Motor.throttle = Right_Motor_speed


while True:
    message = dabble.read_message()
    if (message != None):
        print("Message: " + str(message))
        if (message.up_arrow_pressed):
            forward()
            print("Move both motors forward")
        elif (message.down_arrow_pressed):
            backwards()
            print("Move both motors backward")
        elif (message.right_arrow_pressed):
            right()
            print("Move left motor forward and right motor backward")
        elif (message.left_arrow_pressed):
            left()
            print("Move left motor backward and right motor forward")
        elif (message.no_direction_pressed):
            stop()
            print("Stop both motors")
        else:
            print("Something crazy happened with direction!")

        if (message.triangle_pressed):
            print("Raise arm")
        elif (message.circle_pressed):
            print("Lower arm")
        elif (message.square_pressed):
            print("Squirt water")
        elif (message.circle_pressed):
            print("Fire laser")
        elif (message.start_pressed):
            print("Turn on LED")
        elif (message.select_pressed):
            print("Do victory dance")
        elif (message.no_action_pressed):
            print("No action")
        else:
            print("Something crazy happened with action!")
