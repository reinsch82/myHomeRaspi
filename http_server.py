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
            piFace.output_pins[0].turn_on()
            piFace.output_pins[1].turn_on()
            Timer(25.0, switchOff, [0, 1]).start()
        if path.startswith("/up"):
            piFace.output_pins[0].turn_on()
            piFace.output_pins[1].turn_off()
            Timer(25.0, switchOff, [0]).start()


            
if __name__ == "__main__":        
	
	
	serveraddr = ('', 8080)
	srvr = HTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()
