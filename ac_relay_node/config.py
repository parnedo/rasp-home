# 5v  GN                                                       OUT
#-----------------------------------------------------------------#
# 2    4  6  8  10 12 14 16   18 20 22 24 26 28 30 32 34 36 38 40 #
# 1    3  5  7  9  11 13 15   17 19 21 23 25 27 29 31 33 35 37 39 #
#-----------------------------------------------------------------#
#      

import RPi.GPIO as GPIO
ac_relay = {}
ac_relay['light1']={'pin':3, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}
ac_relay['light2']={'pin':5, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}
ac_relay['light3']={'pin':7, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}
ac_relay['light4']={'pin':11, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}
ac_relay['light5']={'pin':13, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}
ac_relay['light6']={'pin':15, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}
ac_relay['light7']={'pin':35, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}
ac_relay['light8']={'pin':37, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}



ac_relay['pin21']={'pin':40, 'ES': GPIO.OUT, 'initial':GPIO.HIGH}
