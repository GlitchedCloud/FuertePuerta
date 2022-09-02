# The Door Sound!

## Credits: 
First, I would like to thank these articles for help!
https://www.deviceplus.com/raspberry-pi/how-to-have-entrance-music-using-a-raspberry-pi/
https://www.circuitbasics.com/detecting-motion/

## What is it?
Well, this script is made for our door. It detects motion (with motion sensor) and plays a sound (with mpg321). 

## What do we need?
A microcomputer (A Raspberry Pi in our case)
A PIR motion sensor ()
A MP3 file (sound.mp3 on our repo)
An audio device for the sound (AUX of HDMI port)

## Let's setup!
First, clone this repo. 
Then, install mpg321 (sudo apt install mpg321)

## Attach your PIR motion sensor
For this, you can refer to the image in deviceplus article. 
We will be connecting directly to RPI's GPIO
Connect red to the 5V of PI
Black to RPI's Ground
and any other color to PIN 24 of the GPIO

## What next? 
python3 script.py

## Next?
Profit. You're done. 
As deviceplus suggests, you might want to add a if statement to check it is early / late. We don't need this, so we're done!