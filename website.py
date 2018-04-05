from http.server import HTTPServer, BaseHTTPRequestHandler


# TODO Refactor this to use Flask instead of the default http server
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Running!")
    httpd.serve_forever()


run()
