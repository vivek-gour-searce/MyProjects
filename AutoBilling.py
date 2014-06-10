import pymongo
import telnetlib


class TelnetAutomation():
    def __init__(self, telnetHost="10.235.108.20",telnetPort=23):
        """

        """
        self.telnetHost = telnetHost
        self.telnetPort = telnetPort
        self.debugFlag = True
        self.data = [""]
        self.charges = [
#                 {"chargeCode":"1003","currency":"USD","rate":"7.48","chargeableWt":"128"},
#                 {"chargeCode":"1008","currency":"USD","rate":"2.29","chargeableWt":"128"},
#                 {"chargeCode":"1101","currency":"USD","rate":"0.1","chargeableWt":"128"},
#                 {"chargeCode":"1201","currency":"USD","rate":"20","chargeableWt":"1"},
#                 {"chargeCode":"1516","currency":"USD","rate":"20","chargeableWt":"1"},
#                 {"chargeCode":"1411","currency":"USD","rate":"20","chargeableWt":"1"},
#                 {"chargeCode":"1908","currency":"USD","rate":"20","chargeableWt":"1"},
#                 {"chargeCode":"1411","currency":"USD","rate":"0.07","chargeableWt":"128"},
#                 {"chargeCode":"1411","currency":"USD","rate":"10","chargeableWt":"1"}
                ]
        self.steps = [
                      {"send" : "iahuaxa","checkpointStr" : "Welcome","readUntill" : "Areas/OFS"},
                      {"send" : "\t","checkpointStr" : "\x1b[4;9H","readUntill" : ""},
                      {"send" : "welcome7","checkpointStr" : "\x1b[0m","readUntill" : ""},
                      {"send" : "\r","checkpointStr" : "OFS Main","readUntill" : "F12=Cancel"},
                      {"send" : "1","checkpointStr" : "\x1b[4m1","readUntill" : ""},
                      {"send" : "\r","checkpointStr" : "CEVA","readUntill" : "F12=Cancel"},
                      {"send" : "2","checkpointStr" : "\x1b[4m2","readUntill" : None},
                      {"send" : "\r","checkpointStr" : "CANADA","readUntill" : "menu"},
                      {"send" : "awbreg","checkpointStr" : "AWBREG","readUntill" : ""},
                      {"send" : "\r","checkpointStr" : "AWB REGISTRATION","readUntill" : "F24-AgtSt"},
                      {"send" : "l","checkpointStr" : "F16-Milestones","readUntill" : ""},
                      {"send" : "PD102-00014521", "checkpointStr" : "PD102-00014521","readUntill" : ""},
                      {"send" : "\r", "checkpointStr" : "[2;64H9","readUntill" : "TrnInv"},
                      {"send" : "\x1B[28~", "checkpointStr" : "ITEMS","readUntill" : "F24"}
                    ]

    def renderScreen(self, data):
            dataA=data.split('\x1b')
            print dataA
            ScreenString=" "*80*25
            startPos=0
            flag=0
            theData=''
            for x in dataA:
                i=0
                if flag == 1:
                    if x[0] == '[' and len(x) > 4:
                        if x[2] ==';':
                            if x[4] == 'H':
                                i=5
                                startPos=int(x[1])*80+int(x[3])-1
                            elif x[4] =='m':
                                i=5
                            elif x[5] == 'H':
                                i=6
                                startPos=int(x[1])*80+int(x[3:5])-1
                        if x[3] == ';':
                            if x[5] == 'H':
                                i=6
                                startPos=int(x[1:3])*80+int(x[4])-1
                            elif x[5] == 'm':
                                i=6
                            elif x[6] == 'H':
                                i=7
                                startPos=int(x[1:3])*80+int(x[4:6])-1
                    if len(x)>2 and (x[2] =='m' or x[2] == 'J'):
                        i=3
                        theData=theData+x[i::]
                    elif len(x)>4 and (x[4] =='m'):
                        i=5
                        theData=theData+x[i::]
                    elif len(x)<4:
                        i=4
                        theData=theData+x[i::]
                    else:
                        theData=x[i::]
                    #print theData
                    ScreenString=ScreenString[0:startPos]+theData+"\n"+ScreenString[startPos+len(theData)::]
                    #print ScreenString
                    #print x
                    #print ''
                if x == '[?7h' or x == '[2J':
                    flag=1
            print ScreenString
            print ScreenString[1::]
            #print theData

    def sendChar(self, char, checkpointStr, errorMsg=None,readUntillStr=None, timeout=2, blow=False, debugFlag=False):
        self.data[0] = ""
        print ("####",repr(char)," = ",repr(checkpointStr))  if self.debugFlag == True else ""
        self.tn.write(str(char)) #
        if not self.checkpoint( checkpointStr, timeout):
            print "Unable to send "+repr(char), " msg: ", errorMsg
            print ("=====",repr(self.data[0]))  if self.debugFlag == True else ""
            if blow:
                exit()
            else:
                return False
        else:
            print ("=====",repr(self.data[0]))  if self.debugFlag == True else ""
            return True

    def getMongoDatabaseObj(self, URL, DB, MONGO_PORT, MONGO_UNAME, MONGO_PASSWD, useDBName=""):
        """
            This function returns mongodb database object.
        """
        connObj = pymongo.Connection(URL, MONGO_PORT)
        try:
            connObj[DB].authenticate(MONGO_UNAME, MONGO_PASSWD)
        except:
            pass
        return connObj[useDBName if useDBName is not "" else DB]

    def get_results(self, query):
        self._db = MySQLdb.connect(cherrypy.config['host'], cherrypy.config['user'], cherrypy.config['passwd'], "ADROIT")
        self._cursor = self._db.cursor()
        # query = "UPDATE process_it_mawbdetail SET createAIDesc='1st page', createAIStatus=1 WHERE mawbNum='" + mawb + "'
        try:
            # Execute the SQL command
            self._cursor.execute(query)
            self._db.commit()
        except:
            self._db.rollback()
            return False
        self._db.close()
        return True

    def checkpoint(self, checkpoint_str, timeout=2):
        if checkpoint_str:
            response_str = self.tn.read_until(checkpoint_str, timeout)
            if checkpoint_str in response_str or (checkpoint_str in repr(response_str)):
                self.data[0] += response_str
                self.data[0] += self.tn.read_eager()
                return True
            else:
                self.data[0] += response_str
                self.data[0] += self.tn.read_eager()
                return False
        else:
            self.data[0] += self.tn.read_until("xxxx",1)
            return True

    def invoice_generation_checkpoint(self, checkpoint_str):
        query = "UPDATE ADROIT.process_it_mawbdetail SET createAIDesc='Unable to reach checkpoint -" + checkpoint_str + " ', createAIStatus=2  WHERE mawbNum IN ('" + mawb + "')"
        if not self.get_results(query):
            return "some Problem in querying the database..aborting, Unable to create AI file!"

    def invoice_generation(self, URL, DB, MONGO_PORT, MONGO_UNAME, MONGO_PASSWD, collectionName):
        if True:
            self.dbObj = self.getMongoDatabaseObj(URL, DB, MONGO_PORT, MONGO_UNAME, MONGO_PASSWD)
            self.tasks = self.dbObj[collectionName].find({"taskName":"InvoiceGeneration", "status":1})
            for task in self.tasks:
                self.tn = telnetlib.Telnet(self.telnetHost)
                self.tn.open(self.telnetHost, self.telnetPort)
                #self.tn.set_debuglevel(10)
                print "Processing: ", task['taskName']

                for index, step in enumerate(self.steps):#task['stepsInfo']:
                    sendChar = step['send']
                    checkpointStr = step['checkpointStr']
                    readUntillStr = step['readUntill']

                    if not self.sendChar(sendChar, checkpointStr, "Unable to send"+sendChar, blow=False):
                        if index == 3:
                            if 'job' in self.data[0]:
                                print "User is allocated to another job!! pressing Enter"
                                self.tn.write('\r')
                        else:
                            print "unable to reach the checkpointStr !!! ",checkpointStr
                            print repr(self.data[0])
                            exit(0)
                    if readUntillStr:
                        print (">>>>",readUntillStr) if self.debugFlag == True else ""
                        self.data[0] += self.tn.read_until(readUntillStr)
                        #self.renderScreen(self.data[0])
                    ###################################################
                    #loop endsssss
                print "response after fetching charges: ",repr(self.data[0])

                if "  \x1b[4m\x1b[0m \x1b[4m \x1b[0m \x1b[4m 1" in self.data[0]:
                    print "First charge will be deleted"
                    delChargeAtFirstLoc = True
                else:
                    delChargeAtFirstLoc = False
                    print "first charge wont be deleted"

                #self.sendChar("M", "lines", "Unable to press M", blow=False)
                #self.sendChar("\r", "F24-Suppl", "Unable to press Enter", blow=True )
                #self.sendChar("\r", "Sort", "Unable to press Enter", blow=True )
                #self.sendChar("\x1B[17~", "Payment T   I/E Print", "Unable to sort charges", blow=False )

                while False:
                    print "=====",repr(self.data[0])  if self.debugFlag == True else ""
                    if delChargeAtFirstLoc or ( "  \x1b[4m\x1b[0m \x1b[4m \x1b[0m \x1b[4m 1" in self.data[0] ) or ("[16;6H" in self.data[0]) :
                        if delChargeAtFirstLoc:
                            print "first charge deleting"
                            delChargeAtFirstLoc = False
                        if ( "  \x1b[4m\x1b[0m \x1b[4m \x1b[0m \x1b[4m 1" in self.data[0] ):
                            print "sorting gave a new charge at first location...deleting"
                        if ( "\x1b[16;" in self.data[0] ):
                            print "Character just after 1 is changed"
                        self.sendChar("D", "F21-Fin", "Unable to press D", blow=True )
                    else:
                        break  #This means no more charges to delete

                cnt = 2
                while False:
                    self.data[0] = ""
                    print "####",repr("\x1B[6~")," = ","xxx"  if self.debugFlag == True else ""
                    self.tn.write(str("\x1B[6~")) #pagedown
                    if not self.checkpoint( "[14;72H"+str(cnt)):
                        print "Unable to page down"
                    print "=====",repr(self.data[0])  if self.debugFlag == True else ""
                    cnt = cnt+1
                    if cnt > 6 :
                        break

                errorFlag = False
                for charge in self.charges:
                    self.sendChar( "A", "\x1b[4mA","Unbale to send A", debugFlag=True)
                    self.sendChar( charge['chargeCode'], charge['chargeCode'])
                    if not self.sendChar( "\r", "enter rate") :
                        if "Not exist" in  self.data[0]:
                            print charge['chargeCode'] + "is not allowed!"
                            self.sendChar( "\x1B\x1BOR")                  #escape F3
                            break
                        else:
                            print "Not an invalid rate either!"

                    self.sendChar( "\x1B[A", "[21;10H")                                     #uparrow
                    self.sendChar( charge['currency'], "\x1b[4m"+charge['currency'])
                    self.sendChar( charge['rate'], charge['rate'])
                    self.sendChar( "\x1B[B", "x1b[1B")                                      #cursordown
                    self.sendChar( "\x1B[Z", "xxx")                                         # \x1B[OI~ \x1B[Z shiftTab
                    self.sendChar( "\x1B[3~"*15, "xxx")                                     #15 times delete
                    self.sendChar( charge['chargeableWt'], charge['chargeableWt'])
                    self.sendChar( "\r", "Rate")

                    # for loop ends

                #self.sendChar("\r", "F11-DosE", "Unable to press enter after entering rate", blow=False )
                #self.sendChar("\x1B[25~", "AgtStl", "", blow=False )   # shift F1 ...return back from charge entering screen
                #self.sendChar("\033_", "Booking no", "", timeout=4, blow=False )   # shift F11 ..."TRANSFER INVOICES...Booking no."
                #self.sendChar("\r", "xxx", "", blow=False )
                #self.sendChar("\r", "xxx", "", blow=False )

                self.sendChar("\033_", "Invtot", "", blow=False ) #"\033!"                 #shift F11

                splitStr = "\x1b[7m\x1b[0m \x1b[7m \x1b[0m \x1b[7m \x1b[0m"
                settelementData = self.data[0].split(splitStr)
                for data in settelementData[2:]:
                    if "\x1b[4mPA" in data:
                        print "modifying------",repr(data)
                        self.sendChar("\x1B[28~", "F23-Fwdr", "", blow=False )           # shift F3
                        #self.sendChar("M", "xxx", "", blow=False )           # shift F3
                        #self.sendChar("\r", "xxx", "", blow=False )
                        #self.sendChar("\x1B[36~", "xxx", "", blow=False )           # shift F9
                        #self.sendChar("\t"*5, "xxx", "", blow=False )           # five times tab
                        #self.sendChar(charge['currency'], "xxx", "", blow=False )           # currency as per customer
                        #self.sendChar("\r", "xxx", "", blow=False )
                        #self.sendChar("\r", "xxx", "", blow=False )
                        #self.sendChar("\r", "xxx", "", blow=False )
                        #self.sendChar("P", "xxx", "", blow=False )
                        #self.sendChar("\r", "xxx", "", blow=False )
                        self.sendChar("E", "xxx", "", blow=False )
                        break
                    else:
                        print "down arrow----",repr(data)
                        self.sendChar("\x1B[B", "xxx", "", blow=False )           # down Arrow



                #dataToBeAnalysed = self.data[0].split(splitStr)[1]
                #print repr(dataToBeAnalysed)
#                 F13 shift F1  # \x1B[25~
#                 F23 shift F11 #   "TRANSFER INVOICES...Booking no."
#                 Enter           "AWB Registration...Agstl"
#                 Enter           "EDI status"

#                 If Status Code is not 4 then
#                     Enter
#                 End if
#                 F15    # \x1B[25~ shift F3
#                 F23    # \x1B[28~ shift F11
#                 Capture Screen
#                 put cursor on payer/horizontally to Text "PA"
#                 F15    shft F3
#                 M
#                 Enter
#                 F21    Sfhit F9
#                 5 times tab
#                 Change currency as per customer type "USD"
#                 Enter
#                 Enter
#                 Enter
#                 P
#                 Enter
#                 E
#                 F13
#                 else
#                     Stop Billing
#                     Msg "Status is not 4 or Shipment is not ready for billing"

                self.sendChar("\x1BOR\x1BOR", "\x1b[24;78HSup", "Unable to press F3", blow=False )   #F3 for back
                self.sendChar("E", "MAIN MENU", "Unable to press E for main menu", blow=True )

                self.tn.close()
        try:
            pass
        except Exception, e:
            print "error", e.message

if __name__ == '__main__':
    URL = "122.248.234.221"
    DB = "DEV_INVOIZE"
    MONGO_PORT = 27018
    MONGO_UNAME = "DEV_DEVELOPER"
    MONGO_PASSWD = "!@dev!0per"
    ofs = TelnetAutomation()
    ofs.invoice_generation(URL, DB, MONGO_PORT, MONGO_UNAME, MONGO_PASSWD, "AutomationTasks")