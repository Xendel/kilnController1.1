# Import required libraries
import sys
import RPi.GPIO as GPIO
import time

toDisplay="14.38" # numbers and digits to display

delay = 0.005 # delay between digits refresh

# --------------------------------------------------------------------
# PINS MAPPING AND SETUP
# selDigit activates the 4 digits to be showed (0 is active, 1 is unactive)
# display_list maps segments to be activated to display a specific number inside the digit
# digitDP activates Dot led
# --------------------------------------------------------------------

selDigit = [14,15,18,23]
# Digits:   1, 2, 3, 4

display_list = [24,25,8,7,1,12,16] # define GPIO ports to use
#disp.List ref: A ,B ,C,D,E,F ,G

digitDP = 20
#DOT = GPIO 20

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Set all pins as output
GPIO.setwarnings(False)
for pin in display_list:
  GPIO.setup(pin,GPIO.OUT) # setting pins for segments
for pin in selDigit:
  GPIO.setup(pin,GPIO.OUT) # setting pins for digit selector
GPIO.setup(digitDP,GPIO.OUT) # setting dot pin
GPIO.setwarnings(True)

#GPIO13 for Red LED(temperature) and GPIO19 for Green LED (time left)



# DIGIT map as array of array ,
#so that arrSeg[0] shows 0, arrSeg[1] shows 1, etc

arrSeg = [[0,0,0,0,0,0,1],\
          [1,0,0,1,1,1,1],\
          [0,0,1,0,0,1,0],\
          [0,0,0,0,1,1,0],\
          [1,0,0,1,1,0,0],\
          [0,1,0,0,1,0,0],\
          [0,1,0,0,0,0,0],\
          [0,0,0,1,1,1,1],\
          [0,0,0,0,0,0,0],\
          [0,0,0,0,1,0,0]]

# Use this block instead of above for common cathode-anode
# arrSeg = [[1,1,1,1,1,1,0],\
#           [0,1,1,0,0,0,0],\
#           [1,1,0,1,1,0,1],\
#           [1,1,1,1,0,0,1],\
#           [0,1,1,0,0,1,1],\
#           [1,0,1,1,0,1,1],\
#           [1,0,1,1,1,1,1],\
#           [1,1,1,0,0,0,0],\
#           [1,1,1,1,1,1,1],\
#           [1,1,1,1,0,1,1]]

GPIO.output(digitDP,0) # DOT pin change to 1 for common cathode-anode

# --------------------------------------------------------------------
# MAIN FUNCTIONS
# splitToDisplay(string) split a string containing numbers and dots in
#   an array to be showed
# showDisplay(array) activates DIGITS according to array. An array
#   element to space means digit deactivation
# --------------------------------------------------------------------

def showDisplay(digit):
 GPIO.output(tempDisplay,1)
 for i in range(0, 4): #loop on 4 digits selectors (from 0 to 3 included)
  sel = [0,0,0,0]
  sel[i] = 1
  GPIO.output(selDigit, sel) # activates selected digit
  if digit[i].replace(".", "") == " ": # space disables digit
   GPIO.output(display_list,0)
   continue
  numDisplay = int(digit[i].replace(".", ""))
  GPIO.output(display_list, arrSeg[numDisplay]) # segments are activated according to digit mapping
  if digit[i].count(".") == 1:
   GPIO.output(digitDP,0) # if the Dot is on when not intended switch this 1 (common anode-common cathode)
  else:
   GPIO.output(digitDP,1) # if the Dot is on when not intended switch this 0 (common anode-common cathode)
  time.sleep(delay)

def splitToDisplay (toDisplay): # splits string to digits to display
 arrToDisplay=list(toDisplay)
 for i in range(len(arrToDisplay)):
  if arrToDisplay[i] == ".": arrToDisplay[(i-1)] = arrToDisplay[(i-1)] + arrToDisplay[i] # dots are concatenated to previous array element
 while "." in arrToDisplay: arrToDisplay.remove(".") # array items containing dot char alone are removed
 return arrToDisplay

# --------------------------------------------------------------------
# MAIN LOOP
# persistence of vision principle requires that digits are powered
#   on and off at a specific speed. So main loop continuously calls
#   showDisplay function in an infinite loop to let it appear as
#   stable numbers display
# --------------------------------------------------------------------

try:
 while True:
  showDisplay(splitToDisplay(toDisplay))
except KeyboardInterrupt:
 print('interrupted!')
 GPIO.cleanup()
sys.exit()
