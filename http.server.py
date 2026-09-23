from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)

print("Serveur démarré sur http://localhost:8000")

server.serve_forever()