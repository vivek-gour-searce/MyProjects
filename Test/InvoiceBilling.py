__author__ = 'vivek.gour'

import telnetlib
import pymongo


class Billing():
    def __init__(self, userid, password, telnetHostIP, telnetPort = 23):
        self.telnetHostIP = telnetHostIP
        self.telnetPort = telnetPort
        self.userid = userid
        self.password = password

    def steps(self):
        return {
            "1": {"value": "checkpoint", "mustString": "HGPSFO01", "checkString": "CEVA FREIGHT MANAGEMENT", "decision": []},
            "2": {"value": "IAHAEVXG"},
            "3": {"value": "\t"},
            "4": {"value": "searce12"},
            "5": {"value": "\r"},
            "6": {"value": "checkpoint", "mustString": "Display Program Messages", "checkString": "a",
                  "decision": [{"text": "Press Enter to continue", "goTo": ""}, {"text": "", "goTo": ""}]}
        }

    def login(self, system, chkstring, muststring):
        self.system = system
        self.chkstring = chkstring
        self.muststring = muststring
        self.tn = telnetlib.Telnet(self.telnetHostIP, self.telnetPort)
        self.tn.set_debuglevel(10)
        self.tn.write(self.userid)
        print 'user id sent'
        chk = BS.checkpoint("HGPSFO01")
        if not chk:
            exit(0)
        else:
            print 'chkstring'
        self.tn.write('\t')
        self.tn.write(self.password)
        self.tn.write('\r')
        chk = BS.checkpoint("a")
        if not chk:
            print "got an error, not reached to desired screen"
            self.errorHandling()
            exit(0)
        else:
            print 'chkstring'

    def checkpoint(self, chkstr):
        if chkstr:
            res_str = self.tn.read_until(self.chkstring, timeout=2)
            if chkstr in res_str:
                return True
            else:
                return False

    def errorHandling(self):
        print "try to handle error"

if __name__ == '__main__':

    system = "class" #raw_input('Enter system name : ')
    systemtype = "live" #raw_input('Enter system type : ')

    if systemtype == 'live':
        if system == 'ofs':
            BS = Billing('iahuvlg','welcome1','10.235.108.20')
            BS.login('ofs','Matrix OFS','EPIOFSP1')
        elif system == 'class':
            BS = Billing('iahaevxg','searce12','57.33.98.226')
            BS.login('class','CEVA FREIGHT','HGPSFO01')
        elif system == 'wp':
            BS = Billing('iahaevyg','welcome1','57.33.98.7')
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


