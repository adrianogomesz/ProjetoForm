import http.server
import socketserver

HOST = '127.0.0.1'
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("Servidor iniciado em: ", PORT)
    httpd.serve_forever()