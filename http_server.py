#! /usr/bin/python 
# -*- coding: utf-8 -*-
# simple http server for raspberry

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SimpleHTTPServer
import urlparse
from threading import Timer

import pifacedigitalio as pf

piFace = pf.PiFaceDigital()

def switchOff(*args):
    print "switch off pins " + str(args)
    for arg in args:
        piFace.output_pins[arg].turn_off();

def switchPins(*args):
    print "switch pins " + str(args)
    for pin in args:
        if pin[1]:
            print "pin " + str(pin[0]) + " switched on"
            piFace.output_pins[pin[0]].turn_on()
        else:
            print "pin " + str(pin[0]) + " switched off"
            piFace.output_pins[pin[0]].turn_off()
    Timer(25.0, switchOff, [0, 1]).start()

    
"SimpleHTTPServer.SimpleHTTPRequestHandler"
class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        print 'headers'
        self._writeheaders()

    def do_GET(self):
        (scm, netloc, path, params, query, fragment) = urlparse.urlparse(self.path, 'http')
        print self.path + ' Path: ' + str(path) + '\n\nParams: ' + str(params)
        
        'self._writeheaders()'
        if self.path == '/':
            self.path = '/web/index.html'
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        if path.startswith('/web'):
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
            
            
    def do_POST(self):
        (scm, netloc, path, params, query, fragment) = urlparse.urlparse(self.path, 'http')
        print "path: " + path
        if path.startswith("/down"):
            switchPins((0, True), (1, True)) 
        if path.startswith("/up"):
            switchPins((0, True), (1, False))
        self.send_response(200)


            
if __name__ == "__main__":        
	
	
	serveraddr = ('', 8080)
	srvr = HTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()
