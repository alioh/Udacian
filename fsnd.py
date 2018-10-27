from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


class WebServerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
    	#Submit the form
        self.send_response(301)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        ctype, pdict = cgi.parse_header(
            self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            name = fields.get('name')
            city = fields.get('city')
            enrollment = fields.get('enrollment')
            nanodegree = fields.get('nanodegree')
            status = fields.get('status')
        memory = []
        form = '''<!DOCTYPE html>
            <title>Udacian</title>
            <form method="POST" action="http://localhost:8000/">
                <textarea name="name">name</textarea>
                <br>
                <textarea name="city">city</textarea>
                <br>
                <textarea name="enrollment">enrollment</textarea>
                <br>
                <textarea name="nanodegree">nanodegree</textarea>
                <br>
                <textarea name="status">status</textarea>
                <br>
                <button type="submit">Post it!</button>
            </form>
            <pre>
            {}
            </pre>
            '''.format(name, city, enrollment,nanodegree,status)
        self.wfile.write(form)
        print(form)


    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            memory = []
            form = '''<!DOCTYPE html>
            <title>Udacian</title>
            <form method="POST" action="http://localhost:8000/">
                <textarea name="name">name</textarea>
                <br>
                <textarea name="city">city</textarea>
                <br>
                <textarea name="enrollment">enrollment</textarea>
                <br>
                <textarea name="nanodegree">nanodegree</textarea>
                <br>
                <textarea name="status">status</textarea>
                <br>
                <button type="submit">Post it!</button>
            </form>
            <pre>
            {}
            </pre>
            '''
            self.wfile.write(bytes(form, "utf-8"))
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print ("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()