import sys
from serial_delay_test import SerialDelayTest

if len(sys.argv) > 1:
    port = sys.argv[1]
else:
    port =  '/dev/ttyUSB0'

test = SerialDelayTest(port)
test.run(1000)

