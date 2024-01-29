from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Process the received data (post_data) here
        # For now, let's just print it
        print("Received data:")
        print(post_data.decode('utf-8'))
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Results received successfully.')

def run_server(server_class=HTTPServer, handler_class=MyHTTPHandler, port=443):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

# Usage
if __name__ == '__main__':
    run_server()
