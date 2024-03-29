from machine import RTC
import rp2
import sys
import utime as time
import usocket as socket
import ustruct as struct
import constants

# wintertime / Summerzeit
GMT_OFFSET = 3600 * 1 # 3600 = 1 h (wintertime)
#GMT_OFFSET = 3600 * 2 # 3600 = 1 h (summertime)

# NTP-Host
NTP_HOST = constants.NTP_HOST

# Function: get time from NTP Server
def getTimeNTP():
    NTP_DELTA = 2208988800
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(NTP_HOST, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    ntp_time = struct.unpack("!I", msg[40:44])[0]
    return time.gmtime(ntp_time - NTP_DELTA + GMT_OFFSET)

# Function: copy time to PI pico´s RTC
def setTimeRTC():
    rtc = RTC()
    tm = getTimeNTP()
    rtc.datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
