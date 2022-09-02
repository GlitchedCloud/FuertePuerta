from time import sleep
from signal import pause
from subprocess import run, Popen, PIPE
from gpiozero import MotionSensor

sleep(600) # This gives you 10 minutes to leave your home
pir = MotionSensor(24)

while True:
p1 = Popen([“ping”, “-c”, “1”, “192.168.0.5”], stdout=PIPE)
stdout_value = p1.communicate()[0]
if b’Destination Host Unreachable’ not in stdout_value:
break
sleep(2)

sleep(5)

pir.wait_for_motion()
run(“mpg123 ~/entrancemusic/’Sexy Boy (Shawn Michaels).mp3′”, shell=True)
