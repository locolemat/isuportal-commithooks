from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

from bot import send_commit_message, send_merge_message

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version
        }).encode())
        return

    def do_POST(self):
        content_len = int(self.headers.get('content-length'))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)

        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            'method': self.command,
            'path': self.path,
            'real_path': parsed_path.query,
            'query': parsed_path.query,
            'request_version': self.request_version,
            'protocol_version': self.protocol_version,
            'body': data
        }).encode())

        endpoint = self.path

        if endpoint == '/commit':
            send_commit_message(msg=data['commits'][0]['message'], author=data['commits'][0]['author']['name'], branch=data['ref'].split('/')[-1], url=data['commits'][0]['url'])
        elif endpoint == '/merge':
            with open('log_merge.txt', 'a') as f:
                f.write(str(data))
                f.write('\n')

            send_merge_message('Мерж залетел!')
        return

if __name__ == '__main__':
    server = HTTPServer(('', 4444), RequestHandler)
    print('Starting server')
    server.serve_forever()