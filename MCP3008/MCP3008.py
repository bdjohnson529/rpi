import RPi.GPIO as GPIO
import time


## Set Raspberry Pi pin numbers.
GPIO.setmode(GPIO.BOARD)
CLK  = 40
MISO = 38
MOSI = 36
CS   = 32
CHNL = 0
VREF = 3.0

GPIO.setwarnings(False) 
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(MISO, GPIO.IN)
GPIO.setup(MOSI, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)


## Create object class for the analog to digital converter
class converter:
    clock = 0
    dac = 0
    read = 0
    def readadc(self, num, clk, din, dout, cs, vref):
        self.clock = 0
        self.dac = 0
        if ((num > 7) or (num < 0)):
            return -1

        GPIO.output(cs , 1) # Stopping any previous transitions
        GPIO.output(clk, 0) # start clock
        GPIO.output(cs , 0) # Selecting slave to start transition

        command = num 
        command |= 0x18     # Puting 2 ones at front of the number
        command <<= 3       # Moving the number to the first 5 digits
        
        ## clock cycles 1-5, programming MCP3008 input din
        for i in range(5):
            if (command & 0x80):
                GPIO.output(din, 1)
                t = 1
            else:
                GPIO.output(din, 0)
                t = 0
                
            command <<= 1
            GPIO.output(clk, 1) # clock pulse to shift
            GPIO.output(clk, 0)
            self.clock = self.clock + 1
  
        ## clock cycle 6, no information exchange
        for i in range(1):
            GPIO.output(clk, 1) # clock pulse to shift
            GPIO.output(clk, 0)
            self.clock = self.clock + 1
        
        ## read dout during clock cycles 7 - 17
        for i in range(11):
            GPIO.output(clk, 1) # clock pulse to shift
            GPIO.output(clk, 0)
            self.clock = self.clock + 1
            out = GPIO.input(dout)
            a = 1.0 / (2 ** i)
            b = a * out
            self.dac += 2.5 * b
            
        GPIO.output(cs , 1) # Deselecting slave to stop transmition
        out >>= 1
        return(self.dac)
 
MCP3008 = converter()

voltage = MCP3008.readadc(CHNL, CLK, MOSI, MISO, CS, VREF)
print('Channel 0: {0}'.format(value))
