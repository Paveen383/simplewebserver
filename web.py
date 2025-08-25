from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!DOCTYPE html>
<html>
<head>
    <title>College Details</title>
</head>
<body>
    <table border="5" align="center" cellspacing="20" cellpadding="20" bgcolor="white">
        <caption><b>Protocols List</b></caption>
        <tr bgcolor="green">
            <th>S.No</th>
            <th>Name of the layer</th>
            <th>Name of the protocol</th>
        </tr>
        <tr bgcolor="yellow">
            <td>1</td>
            <td>application layer</td>
            <td>HTTP,FTP,DNS,Telnet,SSH</td>
        </tr>
        <tr bgcolor="cyan">
            <td>2</td>
            <td>Transport Layer</td>
            <td>TCP/UDP</td>
        </tr>
        <tr bgcolor="red">
            <td>3</td>
            <td>Network Layer</td>
            <td>IPV4/IPv6</td>
        </tr>
        <tr bgcolor="blue">
            <td>3</td>
            <td>Link Layer</td>
            <td>Ethernet</td>
        </tr>
    </table>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()