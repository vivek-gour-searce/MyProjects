__author__ = 'vivek.gour'

import telnetlib
import pymongo


class Billing():
    def __init__(self, userid, password, telnetHostIP, telnetPort = 23):
        self.telnetHostIP = telnetHostIP
        self.telnetPort = telnetPort
        self.userid = userid
        self.password = password


    def login(self, system, chkstring, muststring):
        self.system = system
        self.chkstring = chkstring
        self.muststring = muststring
        self.tn = telnetlib.Telnet(self.telnetHostIP, self.telnetPort)
        self.tn.set_debuglevel(10)
        self.tn.write(self.userid)
        print 'user id sent'
        chk = BS.checkpoint(self.chkstring)
        if chk == 'False':
            exit(0)
        else:
            print 'chkstring'
        self.tn.write('\t')
        self.tn.write(self.password)
        self.tn.write('\r')

    def checkpoint(self,chkstr):
        if chkstr:
            res_str = self.tn.read_until(self.chkstring,2)
            if chkstr in res_str:
                return True
            else:
                return False



if __name__ == '__main__':

    system = raw_input('Enter system name : ')
    systemtype = raw_input('Enter system type : ')

    if systemtype == 'live':
        if system == 'ofs':
            BS = Billing('iahuvlg','welcome1','10.235.108.20','23')
            BS.login('ofs','Matrix OFS','EPIOFSP1')
        elif system == 'class':
            BS = Billing('iahaevxg','welcome8','57.33.98.226','23')
            BS.login('class','CEVA FREIGHT','HGPSFO01')
        elif system == 'wp':
            BS = Billing('iahaevyg','welcome1','57.33.98.7','23')
            BS.login('wp','CEVA FREIGHT','EAGLE1')
    elif systemtype == 'test':
        print('Test system currently not available')
        #if system == 'ofs':
            #BS = Billing('iahuvlg','welcome1','10.235.108.20','23')
            #BS.login('ofs','Matrix OFS','EPIOFSP1')
        #elif system == 'class':
            #BS = Billing('iahaevxg','welcome8','57.33.98.226','23')
            #BS.login('class','CEVA FREIGHT','HGPSFO01')
        #elif system == 'wp':
            #BS = Billing('iahaevyg','welcome1','57.33.98.7','23')
            #BS.login('wp','CEVA FREIGHT','EAGLE1')


