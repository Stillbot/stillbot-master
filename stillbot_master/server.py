#!/usr/bin/env python

from werkzeug.exceptions import HTTPException, NotAcceptable, NotFound, InternalServerError
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Response
import json
from arduino import StillbotMaster
from stillbot_master.webapp.models import Session, Thermistor, Temperature


class StillbotMasterWWW(object):

    url_map = Map([
        Rule('/start_session', endpoint='start_session'),
        Rule('/start_session/<session_id>', endpoint='resume_session'),
        Rule('/end_session', endpoint='end_session'),
        Rule('/thermistors', endpoint='get_thermistors'),
        Rule('/thermistors/<thermistor_id>/temperature', 'get_thermistor_temperature')
    ])
    thermistors = []
    session = ''
    

    def __init__(self):
        print('Opening connection to stillbot-slave..')
        self.bot = StillbotMaster(port='/dev/cu.usbserial-AD01TDU2')
        print('CONNECTION SUCCESS')


    def on_start_session(self, request):
        """Start recording the data coming from Arduino into the database."""
        if request.method == 'POST':
            if self.session:
                return NotAcceptable('Session already in progress with id %s' % self.sesion.id)
            
        try:
            sesh, is_new = Session.objects.get_or_create(name=request.form['name'], description=request.form['description'])
            self.session = sesh
        except Exception, e:
            return InternalServerError(e)


    def on_resume_session(self, request):
        """Start recording data to an pre-existent session."""
        pass


    def on_end_session(self, request):
        """Stop recording the data coming from the Arduino."""
        pass    # TODO


    def on_get_thermistors(self, request):
        """Return a JSON array of thermistors in the system.

        Returns an empty JSON array if there are no thermistors.
        """
        if not self.thermistors:
            pass    # TODO: get thermistor data and populate list
        error = None

    
    def on_get_thermisor_temperature(self, request, thermistor_id):
        """Return the latest temperature reading from the thermistor with id thermistor_id.

        Raises a NotFound exception if there is no thermistor with that id.
        """
        if thermistor_id not in [t.id for t in self.thermistors]:
            raise NotFound()
        resp = Response(json.dumps(self.bot.thermistorTemp(thermistor_id)))
        resp.headers['Content-Type'] = 'application/json'
        return resp


    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException, e:
            return e


    def wsgi_app(self, environ, start_response):
            from werkzeug.wrappers import Request
            request = Request(environ)
            response = self.dispatch_request(request)
            return response(environ, start_response)


    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)
    

if __name__ == '__main__':
    server = StillbotMasterWWW()
    thermistors_total = server.bot.thermistorCount()
    print('Thermistors present: %s' % thermistors_total)

    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 6666, server, use_debugger=True)
