import RPi.GPIO as GPIO
import time

MAX_UNCHANGE_COUNT = 100
STATE_INIT_PULL_DOWN = 1
STATE_INIT_PULL_UP = 2
STATE_DATA_FIRST_PULL_DOWN = 3
STATE_DATA_PULL_UP = 4
STATE_DATA_PULL_DOWN = 5
    
class DHT(object):

    def __init__(self, DHTPIN):
        self.DHTPIN = DHTPIN
        GPIO.setmode(GPIO.BCM) 

    def read_binary(self):
        GPIO.setup(self.DHTPIN, GPIO.OUT)
        GPIO.output(self.DHTPIN, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(self.DHTPIN, GPIO.LOW)
        time.sleep(0.02)
        GPIO.setup(self.DHTPIN, GPIO.IN, GPIO.PUD_UP)
        
        unchanged_count = 0
        last = -1
        data = []
        while True:
                current = GPIO.input(self.DHTPIN)
                data.append(current)
                if last != current:
                        unchanged_count = 0
                        last = current
                else:
                        unchanged_count += 1
                        if unchanged_count > MAX_UNCHANGE_COUNT:
                                break

        state = STATE_INIT_PULL_DOWN

        lengths = []
        current_length = 0

        for current in data:
                current_length += 1

                if state == STATE_INIT_PULL_DOWN:
                        if current == GPIO.LOW:
                                state = STATE_INIT_PULL_UP
                        else:
                                continue
                if state == STATE_INIT_PULL_UP:
                        if current == GPIO.HIGH:
                                state = STATE_DATA_FIRST_PULL_DOWN
                        else:
                                continue
                if state == STATE_DATA_FIRST_PULL_DOWN:
                        if current == GPIO.LOW:
                                state = STATE_DATA_PULL_UP
                        else:
                                continue
                if state == STATE_DATA_PULL_UP:
                        if current == GPIO.HIGH:
                                current_length = 0
                                state = STATE_DATA_PULL_DOWN
                        else:
                                continue
                if state == STATE_DATA_PULL_DOWN:
                        if current == GPIO.LOW:
                                lengths.append(current_length)
                                state = STATE_DATA_PULL_UP
                        else:
                                continue
        if len(lengths) != 40:
               # print( "Data not good, skip")
                return False

        shortest_pull_up = min(lengths)
        longest_pull_up = max(lengths)
        halfway = (longest_pull_up + shortest_pull_up) / 2
        bits = []
        the_bytes = []
        byte = 0

        for length in lengths:
                bit = 0
                if length > halfway:
                        bit = 1
                bits.append(bit)
                
        for i in range(0, len(bits)):
                byte = byte << 1
                if (bits[i]):
                        byte = byte | 1
                else:
                        byte = byte | 0
                if ((i + 1) % 8 == 0):
                        the_bytes.append(byte)
                        byte = 0

        checksum = (the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3]) & 0xFF
        if the_bytes[4] != checksum:
              #  print("Data not good, skip")
                return False

        return the_bytes[0], the_bytes[2]

    def read(self): # try to always use this method, as it is safe.
        result = self.read_binary()
        while(result == False):
                time.sleep(1) # the DHT11 only has a 1Hz out rate
            result = self.read_binary()
        return result
            

if __name__ == "__main__":
    dht = DHT(5)
    while(True):
        result = dht.read_binary()
        if result:
            humidity, temperature = result
            print("humidity: %s %%,  Temperature: %s C`" % (humidity, temperature))
            time.sleep(1)
