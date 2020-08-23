from __future__ import print_function
import time
import serial
import numpy as np
import matplotlib.pyplot as plt

class SerialDelayTest(serial.Serial):

    Baudrate = 115200
    BusyWaitSleepDt = 0.05
    DefaultTimeout = 10.0
    DefaultResetSleep = 2.0
    DefaultGearRatio = 1.0

    def __init__(self, port, timeout=DefaultTimeout, reset_sleep=DefaultResetSleep):
        params = {'baudrate': self.Baudrate, 'timeout': timeout}
        super(SerialDelayTest,self).__init__(port,**params)
        time.sleep(reset_sleep)

    def run(self, num_sample):

        dt_list = []

        for i in range(num_sample):
            #print('sample {}'.format(i))
            #sys.stdout.flush()
            t1 = time.time()
            self.write('s\n'.encode())
            self.readline()
            t2 = time.time()
            dt = t2 - t1
            dt_list.append(dt)

        dt_array = np.array(dt_list)

        print()
        print('min    = {}'.format(dt_array.min()))
        print('max    = {}'.format(dt_array.max()))
        print('mean   = {}'.format(dt_array.mean()))
        print('median = {}'.format(np.median(dt_array)))
        dt_median = np.median(dt)

        plt.hist(dt_array)
        plt.xlim(0,1.1*dt_array.max())
        plt.xlabel('dt round trip (sec)')
        plt.ylabel('count')
        plt.show()



# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port =  '/dev/ttyUSB0'
    test = SerialDelayTest(port)
    test.run(1000)

