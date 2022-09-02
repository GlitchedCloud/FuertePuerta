from subprocess import run
from gpiozero import MotionSensor

pir = MotionSensor(24) #The GPIO your sensor is on.

while True:
    pir.wait_for_motion()
    run(“mpg321 'https://raw.githubusercontent.com/GlitchedCloud/FuertePuerta/main/sound.mp3'”, shell=True)

    pir.wait_for_no_motion()