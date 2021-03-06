import sys
sys.path.append('/home/bart/bin')

import socketserver
import subprocess
import servicemanager

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address[0]))
        print(self.data)
        command=self.data.decode('utf-8')
        if (command == 'kodi on'):
            subprocess.call(['startkodi'])
        elif (command == 'kodi off'):
            subprocess.call(['stopkodi'])
        elif (command == 'kodi status'):
            kodi = servicemanager.kodiservice()
            if (kodi.running()):
                self.request.sendall(b'1')
            else:
                self.request.sendall(b'0')


if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
