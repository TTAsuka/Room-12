# server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class BusInfoRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        bus_info = [
            {"route": "1", "next_stop": "Central Station", "eta": "6 mins"},
            {"route": "2A", "next_stop": "Main St", "eta": "3 mins"},
            {"route": "5B", "next_stop": "North Plaza", "eta": "9 mins"},
        ]


        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


        self.wfile.write(json.dumps(bus_info).encode())


port = 9091
server_address = ('', port)
httpd = HTTPServer(server_address, BusInfoRequestHandler)

print(f"Bus Information Service running on port {port}")
httpd.serve_forever()