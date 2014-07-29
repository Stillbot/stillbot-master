#!/usr/bin/env python

import Arduino
import Pyro4
from webapp.models import Thermistor, Temperature

class StillbotMaster(Arduino.Arduino):
    def thermistorCount(self):
        cmd_str = Arduino.arduino.build_cmd_str('dscount')
        try:
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        else:
            return int(self.sr.readline().replace('\r\n', ''))

    def thermistorTemp(self, thermistorIndex):
        cmd_str = Arduino.arduino.build_cmd_str('dstemp', (thermistorIndex, ))
        try:
            self.sr.write(cmd_str)
            self.sr.flush()
        except Exception, e:
            pass
        else:
            return float(self.sr.readline().replace('\r\n', ''))

    def dispatch_request(self, request):
            from werkzeug.wrappers import Response
            import json
            d = [
                {'thermistor': 0, 'temperature': self.thermistorTemp(0)},
                {'thermistor': 1, 'temperature': self.thermistorTemp(1)}
            ]
            
            response = Response(json.dumps(d))
            response.headers['Content-Type'] = 'application/json'
            return response

    def wsgi_app(self, environ, start_response):
            from werkzeug.wrappers import Request
            request = Request(environ)
            response = self.dispatch_request(request)
            return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

if __name__ == '__main__':
    # https://stackoverflow.com/questions/8068945/django-long-running-asynchronous-tasks-with-threads-processing
    print('Opening connection to stillbot-slave..')
    bot = StillbotMaster()
    print('CONNECTION SUCCESS')
    thermistors_total = bot.thermistorCount()
    print('Thermistors present: %s' % thermistors_total)

    # http://werkzeug.pocoo.org/docs/tutorial/
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 6666, bot, use_debugger=True)

    """
    thermistors = [Thermistor.objects.get_or_create(index=i)[0] for i in xrange(0, thermistors_total)]
    thermistors = sorted(thermistors, key=lambda t: t.index)
    
    # @BUG: The temperature output is inconsistent when the interval is set at anything other than 1
    while True:
        for thermistor in thermistors:
            t = Temperature.objects.create(thermistor=thermistor,
                                           temp=bot.thermistorTemp(thermistor.index))
            print('#%s: %s' % (thermistor.index, thermistor.latest_temp))
        import time
        time.sleep(1)
    """
