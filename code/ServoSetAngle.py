from hackerschool import Servo

servo = None


HSTerm.term_exec('Set the servo to 90 degrees.')
servo = Servo(2)
servo.set_angle(90)
