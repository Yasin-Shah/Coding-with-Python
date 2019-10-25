from time import *

tsec=time()
print("Time in sec: ",tsec)

utime=ctime(tsec)
print("Usable Time: ",utime)  # IST Time


gtime=gmtime()
print("GMT Time: ",gtime) # GMT Time

etime=gmtime(1)
print("Epoch Time: ",etime)

"""ltime= localtime()
print("Local Time: ",ltime)

utime=asctime(ltime)
print("Usable Time: ",utime)"""

