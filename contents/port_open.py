import socket
import sys
from .decorator import timeout

HOST = sys.argv[1]
PORT = int(sys.argv[2])
TIMEOUT = int(sys.argv[3])


@timeout
def open(PORT, host=HOST, timeout=TIMEOUT):
    try:
        s = socket.create_connection((host, port), timeout)
        s.close()
        return True
    except socket.error:
        pass


