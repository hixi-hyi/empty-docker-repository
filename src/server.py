import http.server
import socketserver
import os

PORT = os.environ.get('PORT', 80)

class RequestHandler(http.server.SimpleHTTPRequestHandler):

    def message(self):
        parts = []
        parts.append("Hello world")
        for key, val in os.environ.items():
            parts.append("{}:{}".format(key, val))
        message = "\n".join(parts)
        return message

    def do_GET(self):
        msg = self.message()
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header("Content-Length", len(msg))
        self.end_headers()

        print(msg, flush=True)
        self.wfile.write(msg.encode("utf8"))
        return

httpd = socketserver.TCPServer(("", int(PORT)), RequestHandler)
print("Listening on port {}".format(PORT), flush=True)
httpd.serve_forever()
