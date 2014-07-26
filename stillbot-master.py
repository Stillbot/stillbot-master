#!/usr/bin/env python

import Arduino

class StillbotMaster(Arduino.Arduino):
    def thermistorCount(self):
        cmd_str = Arduino.arduino.build_cmd_str('dscount')
        try:
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        else:
            return int(self.sr.readline().strip())

    def thermistorTemp(self, thermistorIndex):
        cmd_str = Arduino.arduino.build_cmd_str('dstemp', (thermistorIndex, ))
        try:
            self.sr.write(cmd_str)
            self.sr.flush()
        except Exception, e:
            print e.message
            pass
        else:
            return float(self.sr.readline().strip())

if __name__ == '__main__':
    import time

    print('Connecting to Arduino..')
    bot = StillbotMaster()
    num_of_thermistors = bot.thermistorCount()
    print('There are %s thermistors connected.\n' % num_of_thermistors)

    from stillbot_master.webapp.models import Thermistor, Temperature
    thermistors = [Thermistor.objects.get_or_create(index=i)[0] for i in xrange(0, num_of_thermistors)]
    while True:
        for thermistor in thermistors:
            temp = bot.thermistorTemp(thermistor.index)
            Temperature.objects.create(thermistor=thermistor, temp=temp)
            print('#%s: %s' % (thermistor.index, temp))
        time.sleep(1)
        print('\n')

