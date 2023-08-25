from gpiozero import Button, PWMLED
import os
import time

button_A = Button(2, hold_time=0.5)
button_B = Button(3, hold_time=0.5)
servo = PWMLED(17, frequency=50)
velocidad_Motor = 0
direccion_Motor_Giro = 0
motor_DC1 = PWMLED(14)
motor_DC2 = PWMLED(15)

angulo_Servo = 0

def menu_Principal():
    os.system('clear')
    print(" *****BIENVENIDO*****\n    a.) Motor DC\n    b.) Servomotor\n")
    input_Menu = input("¿Qué motor desea controlar? :   ")

    if input_Menu.lower() == 'a':
        motor_DC()
    elif input_Menu.lower() == 'b':
        servo_control()
    else:
        print("Opción incorrecta..")
        time.sleep(2)
        menu_Principal()

def motor_DC():
    global velocidad_Motor
    global direccion_Motor_Giro
    global motor_DC1
    global motor_DC2
    global direccion_Motor

    os.system('clear')
    print("Motor DC :\n     a.) Remoto\n     b.) Local\n  ")
    input_motor_DC = input("¿Qué deseas hacer?   : ")

    if input_motor_DC.lower() == 'a':
        os.system('clear')
        print("\nCONTROL DE VELOCIDAD\n\n   Velocidad actual :  " + str(velocidad_Motor))
        
        while True:
            if button_A.is_pressed:
                if velocidad_Motor < 100:
                    time.sleep(0.5)
                    velocidad_Motor += 1
                    os.system('clear')
                    print("\nCONTROL DE VELOCIDAD\n\n   Velocidad actual :  " + str(velocidad_Motor))
                    motor_DC1.value = 0
                    motor_DC2.value = (velocidad_Motor / 100) * 2
                else:
                    print("************** VALOR MÁXIMO ALCANZADO...*****************")
                    print("\nCONTROL DE VELOCIDAD\n\n   Velocidad actual :  " + str(velocidad_Motor))
                    time.sleep(2)

            if button_B.is_pressed:
                if velocidad_Motor > 0:
                    time.sleep(0.5)
                    velocidad_Motor -= 1
                    os.system('clear')
                    print("\nCONTROL DE VELOCIDAD\n\n   Velocidad actual :  " + str(velocidad_Motor))
                    motor_DC1.value = 0
                    motor_DC2.value = (velocidad_Motor / 100) * 2
                else:
                    print("************** VALOR MÍNIMO ALCANZADO...*****************")
                    print("\nCONTROL DE VELOCIDAD\n\n   Velocidad actual :  " + str(velocidad_Motor))
                    time.sleep(2)

            if button_A.is_held or button_B.is_held:
                motor_DC()

    elif input_motor_DC.lower() == 'b':
        os.system('clear')
        print("\nCONTROL DIRECCIÓN DE MOTOR Y VELOCIDAD\n\n     a.) Direccion\n     b.) Velocidad")
        submenu_Motor = input("")

        if submenu_Motor.lower() == 'a':
            print("a.)Derecha\nb.)Izquierda")
            direccion_Motor = input("")
            if direccion_Motor.lower() == 'a':
                direccion_Motor_Giro = 0
                time.sleep(3)
                motor_DC()
            elif direccion_Motor.lower() == 'b':
                direccion_Motor_Giro = 1
                time.sleep(3)
                motor_DC()

        elif submenu_Motor.lower() == 'b':
            print("Ingrese la velocidad de giro....  ")
            velocidad_Motor = int(input())
            if direccion_Motor_Giro == 0:
                motor_DC1.value = 0
                motor_DC2.value = (velocidad_Motor / 100) * 2

            elif direccion_Motor_Giro == 1:
                motor_DC1.value = 1
                motor_DC2.value = 0
                motor_DC1.value = (velocidad_Motor / 100) * 2
            
            if button_A.is_held or button_B.is_held:
                motor_DC()

if button_A.is_held or button_B.is_held:
    menu_Principal()

def servo_control():
    global angulo_Servo
    os.system('clear')
    print("CONTROL DE SERVOMOTOR\na.) Remoto\nb.) Local")
    submenu_servo = input("")
    if submenu_servo.lower() == 'a':
        while True:
            if button_A.is_pressed:
                if angulo_Servo < 180:
                    time.sleep(0.5)
                    angulo_Servo += 10
                    os.system('clear')
                    print("CONTROL DE SERVOMOTOR\n\nControl de angulo: " + str(angulo_Servo))
                    servo.value = (angulo_Servo / 1800) + 0.025
                    time.sleep(0.5)
                    servo.off()
                else:
                    print(" ********** VALOR DE MÁXIMO DE ÁNGULO ALCANZADO **********")
                    servo_control()

            if button_B.is_pressed:
                if angulo_Servo > 0:
                    time.sleep(0.5)
                    angulo_Servo -= 10
                    os.system('clear')
                    print("CONTROL DE SERVOMOTOR\n\nControl de angulo: " + str(angulo_Servo))
                    servo.value = (angulo_Servo / 1800) + 0.025
                    time.sleep(0.5)
                    servo.off()
                else:
                    print(" ********** VALOR DE MÍNIMO DE ÁNGULO ALCANZADO **********")
                    servo_control()

            if button_A.is_held or button_B.is_held:
                menu_Principal()

    elif submenu_servo.lower() == 'b':
        print("Ingrese el valor del angulo: ")
        angulo_Servo = int(input(""))
        servo.value = (angulo_Servo / 1800) + 0.025
        time.sleep(0.5)
        servo.off()
        if button_A.is_held or button_B.is_held:
            menu_Principal()

menu_Principal()
