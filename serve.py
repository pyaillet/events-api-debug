#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import json

logging.basicConfig(level=logging.INFO)

ADDR = "0.0.0.0"
PORT = 8000

count_requests = 0
count_events = 0

class GetHandler(
        BaseHTTPRequestHandler
        ):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


    def do_GET(self):
        logging.error(self.headers)
        self._set_headers()
        self.wfile.write("Hi!")

    def do_POST(self):
        global count_requests
        global count_events
        count_requests = count_requests + 1
        try:
            content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            data = json.loads(post_data)
            #print(data)
            count_events = count_events + len(data['events'])
            
            logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                    str(self.path), str(self.headers), post_data.decode('utf-8'))
        except:
            pass
        
        self._set_headers()
        self.wfile.write("POST!".encode("utf8"))
        print(f"=============> Events: {count_events}")
        print(f"=============> Requests: {count_requests}")

Handler = GetHandler

server_address = (ADDR, PORT)
httpd = HTTPServer(server_address, Handler)

print(f"Starting httpd server on {ADDR}:{PORT}")
httpd.serve_forever()


