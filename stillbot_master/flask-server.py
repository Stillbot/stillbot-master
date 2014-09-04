#!/usr/bin/env python

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
import random
from arduino import StillbotMaster
from stillbot_master.webapp.models import Session, Thermistor, Temperature


app = Flask(__name__)
api = Api(app)
arduino = ''


THERMISTORS = {
}


def abort_if_thermistor_doesnt_exist(thermistor_id):
    #if thermistor_id not in THERMISTORS:
    num_of_thermistors = arduino.thermistorCount()
    tid = int(thermistor_id) 
    if  0 < tid < num_of_thermistors + 1:
        abort(404, message="Thermistor {} doesn't exist".format(thermistor_id))


class Thermistor(Resource):

    def get(self, thermistor_id):
        abort_if_thermistor_doesnt_exist(thermistor_id)
        #return THERMISTORS[thermistor_id]
        return {thermistor_id : {'temp': arduino.thermistorTemp(thermistor_id)}, 'model': 'DS18(S)20' }

# ThermistorList
class ThermistorList(Resource):
    def get(self):
        return THERMISTORS

##
## Actually setup the Api resource routing here
##
api.add_resource(ThermistorList, '/thermistors')
api.add_resource(Thermistor, '/thermistors/<string:thermistor_id>')


if __name__ == '__main__':
    print('Connecting to Arduino...')
    try:
        arduino = StillbotMaster(port='/dev/cu.usbserial-AD01TDU2')
    except:
        print('Failed miserably :(')
        exit()
    else:
        print('(port: %s)' % arduino.sr.port)
        print('(version: %s)' % arduino.version())
        print('Thermistors found: %s' % arduino.thermistorCount())
    app.run(debug=True)
