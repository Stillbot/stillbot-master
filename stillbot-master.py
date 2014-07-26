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
    import argparse

    parser = argparse.ArgumentParser(prog='stillbot-master.py',
                                     description='The stillbot master controller.')
    parser.add_argument('--interval', nargs='?', const=1, default=1, type=int,
                        help='The delay (in seconds) between fetching data from the slave (default: 1s)')
    args = parser.parse_args()

    print('Connecting to slave..')
    bot = StillbotMaster()
    num_of_thermistors = bot.thermistorCount()
    print('There are %s thermistors connected.\n' % num_of_thermistors)

    from stillbot_master.webapp.models import Thermistor, Temperature
    thermistors = [Thermistor.objects.get_or_create(index=i)[0] for i in xrange(0, num_of_thermistors)]
    thermistors = sorted(thermistors, key=lambda t: t.index)

    # @BUG: The temperature output is inconsistent when the interval is set at anything other than 1
    print('Now polling the slave at %s second intervals..' % args.interval)
    while True:
        for thermistor in thermistors:
            t = Temperature.objects.create(thermistor=thermistor,
                                           temp=bot.thermistorTemp(thermistor.index))
            print('#%s: %s' % (thermistor.index, thermistor.latest_temp))
        time.sleep(args.interval)
        print('\n')
