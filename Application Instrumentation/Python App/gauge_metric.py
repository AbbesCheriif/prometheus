import http.server
from prometheus_client import start_http_server, Gauge
import time

REQUEST_IN_PROGRESS = Gauge('request_in_progress', "Number of live Request on Application")
REQUEST_LAST_EXECUTED = Gauge('request_last_served', "Time the application was last served")

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUEST_IN_PROGRESS.inc()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First python Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to the first Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close
        time.sleep(7)
        REQUEST_LAST_EXECUTED.set(time.time())
        REQUEST_IN_PROGRESS.dec()

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('0.0.0.0', 5000), HandleRequests)
    server.serve_forever()