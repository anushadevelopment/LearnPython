import os
import os.path
#if os.path.exists("/users/anusha/documents/anusha_sp/pythonstudy/testfile.txt"):
#    os.remove("/users/anusha/documents/anusha_sp/pythonstudy/testfile.txt")
#else:
#    print("file does not exit")

try:
    with open("/users/anusha/documents/anusha_sp/pythonstudy/testfile.txt") as f:
        print (f.readlines())
except IOError:
        print ("File not accessible")

