import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000
HOST = 'localhost'
express_path = 'http://localhost:3000/users'


# This will create a proxy server running on localhost.
# When you make a request to the proxy server, it will forward the request to the Express API server
class ProxyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # can set express_path directly, but here I want to test with django web server, so I will use self.path
        # request_url = express_path
        request_url = self.path
        response = requests.get(request_url)
        self.send_response(response.status_code)
        for header, value in response.headers.items():
            self.send_header(header, value)
        self.end_headers()
        self.wfile.write(response.content)


server = HTTPServer((HOST, PORT), ProxyRequestHandler)
print("start proxy server")
server.serve_forever()
