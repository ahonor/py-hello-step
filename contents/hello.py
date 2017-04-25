import os
import sys

message = sys.argv[1]

sys.stdout.write("message is %s\n" % message)

os._exit(0)