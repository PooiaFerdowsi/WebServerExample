import time
from http.server import BaseHTTPRequestHandler#, HTTPServer
from a import HTTPServer

hostName = "localhost"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.txt = """<h1><p style='color:green;background-color:black'></p></h1>"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Hello World!</p>", "utf-8"))
        self.wfile.write(bytes("<h1><a href='https://stackoverflow.com/questions/65988332/create-a-web-server-for-myself-like-apache-nginx-gws-etc'>Founded By This Question</h1>","utf-8"))
        self.wfile.write(bytes(self.txt,"utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except:
        webServer.server_close()
        print("Server stopped.")
webServer.serve_forever()
