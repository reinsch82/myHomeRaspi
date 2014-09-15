#! /usr/bin/python 
# -*- coding: utf-8 -*-
# simple http server for raspberry

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urlparse

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._writeheaders()

    def do_GET(self):
        (scm, netloc, path, params, query, fragment) = urlparse.urlparse(self.path, 'http')
        print 'Path: ' + str(path) + '\n\nParams: ' + str(params)
        
        self._writeheaders()
        if path == '/':
            self.wfile.write("""<HTML><HEAD><TITLE>Leinwand Steuerung</TITLE></HEAD><BODY>Leinwand Steuerung aus File lesen</BODY></HTML>""")
        if path == '/rauf':
            self.wfile.write("""<HTML><HEAD><TITLE>Leinwand RAUF</TITLE></HEAD><BODY>Leinwand RAUF</BODY></HTML>""")
        if path == '/runter':
            self.wfile.write("""<HTML><HEAD><TITLE>Leinwand RUNTER</TITLE></HEAD><BODY>Leinwand RUNTER</BODY></HTML>""")
            
        
        
serveraddr = ('', 8765)
srvr = HTTPServer(serveraddr, RequestHandler)
srvr.serve_forever()
