#!/usr/bin/env python
#coding=utf-8

"""
Usage:
"""
import socket
import select
import struct

#while True:
#    strtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')
#    print strtime
#    time.sleep(0.001)

class BytesStreamR:
    def __init__(self, data):
        self.pos = 0
        self.data = data
    def ReadByte(self):
        res = struct.unpack("!B", self.data[self.pos])
        self.pos += 1
        return res[0]
    def ReadUint16(self):
        res = struct.unpack("!H", self.data[self.pos : self.pos + 2])
        self.pos += 2
        return res[0]
    def ReadUint32(self):
        res = struct.unpack("!I", self.data[self.pos : self.pos + 4])
        self.pos += 4
        return res[0]
    def ReadUint64(self):
        res = struct.unpack("!Q", self.data[self.pos : self.pos + 8])
        self.pos += 8
        return res[0]
    def ReadString(self, strlen):
        res = struct.unpack("!%ds"%int(strlen), self.data[self.pos : self.pos + strlen])
        self.pos += strlen
        return res[0]
    def ReadBytes(self, datalen):
        res = struct.unpack("!%ds"%int(datalen), self.data[self.pos : self.pos + datalen])
        self.pos += datalen
        return res[0]

class BytesStreamW:
    def __init__(self):
        self.data = ""
        self.pos = 0
    def WriteByte(self, data):
        tmp = struct.pack("!B", data)
        self.data += tmp
    def WriteUint16(self, data):
        tmp = struct.pack("!H", data)
        self.data += tmp
    def WriteUint32(self, data):
        tmp = struct.pack("!I", data)
        self.data += tmp
    def WriteUint64(self, data):
        tmp = struct.pack("!Q", data)
        self.data += tmp
    def WriteString(self, data):
        tmp = struct.pack("!%ds"%len(data), data)
        self.data += tmp
    def WriteBytes(self, data):
        tmp = struct.pack("!%ds"%len(data), data)
        self.data += tmp
    def Data(self):
        return self.data

class TCPClient:
    def __init__(self):
        self.init()
    def init(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._senddata = None

    def connect(self, address):
        self._sock.connect(address)
    def close(self):
        self._sock.close()
    def send(self, data):
        self._senddata = data
        self._sock.send(data) 
    def recv(self):
        data = self._sock.recv(1024)
        return data
    def getSock(self):
        return self._sock

class UDPClient:
    def __init__(self):
        self.init()
    def init(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._senddata = None
    def close(self):
        self._sock.close()
    def sendto(self, data, addr):
        self._senddata = data
        self._sock.sendto(data, addr) 
    def recvfrom(self):
        data, addr = self._sock.recvfrom(1024)
        #print data, addr
        return data, addr
    def getSock(self):
        return self._sock

class UNIXSockClient:
    def __init__(self):
        self.init()
    def init(self):
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._senddata = None
    def connect(self, address):
        self._sock.connect(address)
    def close(self):
        self._sock.close()
    def send(self, data):
        self._senddata = data
        self._sock.send(data) 
    def recv(self):
        data = self._sock.recv(1024)
        return data
    def getSock(self):
        return self._sock
