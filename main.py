#1. From the machine library, import the Pin and I2C classes. These are used to communicate with the OLED screen, attached to the GPIO of the Pico. 
from machine import Pin, I2C, PWM
import time
# import framebuf (this is framebuffer for images! yay!)
import framebuf
#2.  Import the OLED screen library.
from ssd1306 import SSD1306_I2C
from time import sleep

buzzerPIN=16
BuzzerObj=PWM(Pin(buzzerPIN))

#quarter note duration
qn = 0.25

playing = 0

# Author of buzzer function: peppe8o
# Blog: https://peppe8o.com

def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):
    # Set duty cycle to a positive value to emit sound from buzzer
    buzzerPinObject.duty_u16(int(65536*0.2))
    # Set frequency
    buzzerPinObject.freq(frequency)
    # wait for sound duration
    sleep(sound_duration)
    # Set duty cycle to zero to stop sound
    buzzerPinObject.duty_u16(int(65536*0))
    # Wait for sound interrumption, if needed 
    sleep(silence_duration)

def updateOledText(text):
    oled.fill(0)
    oled.text(text, 0, 0)
    oled.show()

def happyBirthdayFirstTwo():
    #C
    #HA
    updateOledText('ha')
    buzzer(BuzzerObj,523,qn * 0.75,0.1)
    #C
    #PPY
    updateOledText('happy')
    buzzer(BuzzerObj,523,qn * 0.25,0.1)
    #D
    #BIRTH
    updateOledText('birth')
    buzzer(BuzzerObj,587,qn,0.1)
    #C
    #DAY
    updateOledText('birthday')
    buzzer(BuzzerObj,523,qn,0.1)

#3. Create an object, i2c, which stores the I2C channel in use, in this case zero,  the SDA and SCL pins that we are connected to, and finally the frequency at which we connect to the OLED screen.
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
#4. Create an object, oled, which will be used to communicate with the OLED screen. It has three arguments, the width and height of the screen (128 x 64 pixels) and the I2C connection details.
oled = SSD1306_I2C(128, 64, i2c)

# tell our program which pin to listen out for
# give it a name that helps us remember what it's doing
button_pin = Pin(14, Pin.IN, Pin.PULL_UP)

# our variables!
button_presses = 0
last_press_ms = 0
button_delay_ms = 50

text_to_display = ''

# a function! this increases the value of button_presses by 1 each time
def handle_press(pin):
    print(pin)
    global button_presses, last_press_ms
    global playing

    now = time.ticks_ms()
    if (now > last_press_ms + button_delay_ms and playing == 0):
        playing = 1
        last_press_ms = now
        button_presses += 1
        # 1st phrase
        happyBirthdayFirstTwo()
        #F
        #TO
        updateOledText('to')
        buzzer(BuzzerObj,698,qn,0.1)
        #E
        #YOU
        updateOledText('you')
        buzzer(BuzzerObj,659,qn * 2,0.1)

        # 2nd phrase
        happyBirthdayFirstTwo()
        #G
        #TO
        updateOledText('to')
        buzzer(BuzzerObj,780,qn,0.1)
        #F
        #YOU
        updateOledText('you')
        buzzer(BuzzerObj,698,qn * 2,0.1)

        #3rd phrase
        #C
        #HA
        updateOledText('ha')
        buzzer(BuzzerObj,523,qn * 0.75,0.1)
        #C
        #PPY
        updateOledText('happy')
        buzzer(BuzzerObj,523,qn * 0.25,0.1)
        #C ^
        #BIRTH
        updateOledText('birth')
        buzzer(BuzzerObj,1046,qn,0.1)
        #A
        #DAY
        updateOledText('birthday')
        buzzer(BuzzerObj,880,qn,0.1)
        #F
        #DEAR
        updateOledText('dear')
        buzzer(BuzzerObj,698,qn,0.1)
        #E
        #SI
        updateOledText('SI')
        buzzer(BuzzerObj,659,qn,0.1)
        #D
        #MEY
        updateOledText('SIMEY')
        buzzer(BuzzerObj,587,qn * 2,0.1)

        #4th phrase
        #A#
        #HA
        updateOledText('ha')
        buzzer(BuzzerObj,932,qn * 0.75,0.05)
        #A#
        #PPY
        updateOledText('happy')
        buzzer(BuzzerObj,932,qn * 0.25,0.05)
        #A
        #BIRTH
        updateOledText('birth')
        buzzer(BuzzerObj,880,qn,0.1)
        #F
        #DAY
        updateOledText('birthday')
        buzzer(BuzzerObj,698,qn,0.1)
        #G
        #TO
        updateOledText('to')
        buzzer(BuzzerObj,784,qn,0.1)
        #F
        #YOU
        updateOledText('you')
        buzzer(BuzzerObj,698,qn * 2,0.1)

        playing = 0

        #Deactivates the buzzer
        BuzzerObj.deinit()


# here we tell our button pin to run the function handle_press when it gets pressed
button_pin.irq(trigger=Pin.IRQ_RISING, handler=handle_press)
    


