__author__ = 'vivek.gour'


from pymongo import MongoClient
import pymongo
from bson.son import SON
from bson.code import Code
from bson import ObjectId


class mongodb:
    def __init__(self,hostIP,port):
        self.hostIP=hostIP
        self.port=port
        self.client = MongoClient(self.hostIP, self.port)
        self.db = self.client.Vivek
        self.collection = self.db.BillingSummary
        self.db.BillingSummaryUpdate.remove()
        #self.data[0]['']=[{'':''}]

    def retrieve(self):
        b = []
        for a in self.collection.find({"Category": "Unbilled"}):
            print a
            b.append(ObjectId(a['_id']))
        print b

    def adddata(self):
        self.data=[{}]
        b = 0
        while True:
            a = raw_input('Enter Country :')
            self.data[b]['Country']=a
            a = raw_input('Enter Station :')
            self.data[b]['Station']=a
            a = raw_input('Enter Account Number :')
            self.data[b]['Account_Number']=a
            a = raw_input('Enter Account Name :')
            self.data[b]['Account_Name']=a
            a = raw_input('Enter Category :')
            self.data[b]['Category']=a
            a = raw_input('Enter Sub-Category :')
            self.data[b]['Sub_Category']=a
            a = raw_input('Do you want to Continue (Y/N) :')
            if a == 'N' or a == 'n':
                break
            else:
                b += 1
                self.data = self.data+[{}]

        self.collection.insert(self.data)
        #print self.data

    def aggg(self):
        res = self.collection.aggregate([
            # unwind could be used with list
            #{"$unwind":"$Station"},
            {"$group": {"_id": "$Country", "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1), ("_id", -1)])}])
        print res

    def map(self):
        return Code("function () {"
                    "emit({account:this.Account_Number},{count:1})"
                    "}")

    def reduce(self):
        return Code("function(key, values) {"
                    " var count = 0;"
                    "values.forEach(function(v) {"
                    "count += v['count'];"
                    "});return {count: count};}")
    def update(self):
        while True:
            a = raw_input('For which Country :')
            b = raw_input('For which Station :')
            c = raw_input('For which Account_Number :')
            d = raw_input('For which Account_Name :')
            f = raw_input('For which Category :')
            e = raw_input('Do you want to cont (Y/N) :')
            if e == 'N' or e == 'n':
                break
        self.collection.update({"Country": a, "Station": b, "Account_Number": c, "Account_Name": d, "Category": f},
                               {"$set": {"Category": "Billed", "Sub_Category": 'IN PROCESS'}})

    def results(self):
        result = self.db.BillingSummary.map_reduce(map=self.map(), reduce=self.reduce(), out="BillingSummaryUpdate")
        for doc in result.find():
            print doc


if __name__ == '__main__':
    m = mongodb('172.16.14.127', 27018)
    a = raw_input('Do you want to\n\
                   1. Add Data :\n\
                   2. Aggregate Data :\n\
                   3. Data :\n\
                   4. Update :')
    if a == '1':
        m.adddata()
    elif a == '2':
        m.aggg()
    elif a == '3':
        m.results()
    elif a == '4':
        m.update()
    elif a == '5':
        m.retrieve()
    elif a == '6':
        m.results()
    else:
        print 'Wrong input'
