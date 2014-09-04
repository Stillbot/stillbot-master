#!/usr/bin/env python

import Arduino
from webapp.models import Thermistor, Temperature

class StillbotMaster(Arduino.Arduino):

    def thermistorCount(self):
        """Return the number of thermistors available in the Arduino."""
        cmd_str = Arduino.arduino.build_cmd_str('dscount')
        try:
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        else:
            return int(self.sr.readline().replace('\r\n', ''))


    def thermistorTemp(self, thermistorIndex):
        """Get the temperature from a thermistor."""
        cmd_str = Arduino.arduino.build_cmd_str('dstemp', (thermistorIndex, ))
        try:
            self.sr.write(cmd_str)
            self.sr.flush()
        except Exception, e:
            pass
        else:
            return float(self.sr.readline().replace('\r\n', ''))
