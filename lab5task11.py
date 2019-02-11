def __init__(self,*args):

        self.ipaddr=args[0]

        self.maskval=args[1]

    def getNetwork(self):

        self.network=self.ipaddr[:-1]+[0]

        return self.network

    def getMask(self):

        #CREATE YOUR OWN SUBNET MASK GENERATOR

        self.masked=[255,255,255,0]

        return self.masked

    def getAddress(self):

        return self.ipaddr

    def __str__(self):

        return '.'.join(str(e) for e in self.getAddress())

        

ip=IP4ADDRES([192,168,0,34],23)

print (ip)

print (ip.getNetwork())

print (ip.getMask())





