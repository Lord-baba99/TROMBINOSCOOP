from http.server import CGIHTTPRequestHandler, HTTPServer

port = 8080

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print(f"Demarrage du server web sur le port : {port}")
httpd.serve_forever()
