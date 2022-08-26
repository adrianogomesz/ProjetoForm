import http.server
import socketserver

HOST = 'localhost'
PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("Servidor iniciado em: ", PORT)
    httpd.serve_forever()